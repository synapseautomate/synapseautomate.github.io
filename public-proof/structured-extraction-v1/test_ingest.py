#!/usr/bin/env python3
from pathlib import Path
import tempfile
from ingest import ingest
from openpyxl import Workbook
from reportlab.pdfgen import canvas


def expect_error(fn, code):
    try:
        fn()
    except ValueError as e:
        assert str(e) == code, (str(e), code)
        return
    raise AssertionError(f'expected {code}')


def main():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        tests = 0
        # 5 normal: PDF / XLSX / EML / CSV / TXT
        p = d / 'a.pdf'
        c = canvas.Canvas(str(p)); c.drawString(72, 720, 'Synthetic order A-1'); c.save()
        assert 'Synthetic order A-1' in ingest(p)['text']; tests += 1

        p = d / 'a.xlsx'
        wb = Workbook(); ws = wb.active; ws.append(['id', 'status']); ws.append([1, 'open']); wb.save(p)
        assert 'open' in ingest(p)['text']; tests += 1

        p = d / 'a.eml'
        p.write_bytes(b'Subject: Test\nContent-Type: text/plain; charset=utf-8\n\nhello')
        assert 'hello' in ingest(p)['text']; tests += 1

        p = d / 'a.csv'; p.write_text('id,status\n1,open\n', encoding='utf-8')
        assert 'status' in ingest(p)['text']; tests += 1

        p = d / 'a.txt'; p.write_text('Siparis #A-1', encoding='utf-8')
        assert 'A-1' in ingest(p)['text']; tests += 1

        # 5 broken / rejected
        p = d / 'empty.txt'; p.write_bytes(b'')
        expect_error(lambda: ingest(p), 'EMPTY_INPUT'); tests += 1

        p = d / 'bad.exe'; p.write_bytes(b'x')
        expect_error(lambda: ingest(p), 'UNSUPPORTED_TYPE'); tests += 1

        p = d / 'dup.txt'; p.write_text('same', encoding='utf-8')
        sha = ingest(p)['metadata']['sha256']
        expect_error(lambda: ingest(p, {sha}), 'DUPLICATE_INPUT'); tests += 1

        p = d / 'bad.json'; p.write_text('{nope', encoding='utf-8')
        expect_error(lambda: ingest(p), 'PARSE_FAILED'); tests += 1

        p = d / 'bad.xlsx'; p.write_bytes(b'not a zip')
        expect_error(lambda: ingest(p), 'PARSE_FAILED'); tests += 1

        print(f'PASS {tests}/10 ingestion tests (5 normal + 5 broken)')


if __name__ == '__main__':
    main()
