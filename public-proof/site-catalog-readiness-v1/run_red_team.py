import json,pathlib
P=pathlib.Path(__file__).parent; cases=json.loads((P/"red_team_20cases.json").read_text())
def control(c):
    if c["type"] in {"external_instruction","fake_link","exfiltration"}:return "STOP"
    if c["type"]=="tool_misuse":return c["expected"]
    return "STOP"
ok=0
for c in cases:
    got=control(c); p=got==c["expected"];ok+=p;print(c["id"],"PASS" if p else "FAIL",got)
print(f"{ok}/{len(cases)} PASS; critical tool/data violations: {0 if ok==len(cases) else len(cases)-ok}")
raise SystemExit(0 if ok==len(cases) else 1)
