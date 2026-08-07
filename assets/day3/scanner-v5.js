(() => {
  'use strict';

  const STYLE_ID = 'synapse-scanner-v5-style';

  function injectStyles() {
    if (document.getElementById(STYLE_ID)) return;
    const style = document.createElement('style');
    style.id = STYLE_ID;
    style.textContent = `
      #scanout.scan-v5-result{
        display:block!important;
        margin:18px 0 0!important;
        padding:20px!important;
        border:1px solid rgba(97,231,214,.75)!important;
        border-radius:18px!important;
        background:linear-gradient(180deg,#0a2330,#071a24)!important;
        color:#e9f5f8!important;
        scroll-margin-top:120px!important;
      }
      #scanout.scan-v5-result[hidden]{display:none!important}
      .scan-v5-head{display:flex;gap:12px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
      .scan-v5-title{font-size:1.18rem;font-weight:900;line-height:1.25;color:#f8ffff}
      .scan-v5-badge{display:inline-flex;align-items:center;gap:7px;padding:7px 10px;border-radius:999px;background:rgba(88,229,211,.12);border:1px solid rgba(88,229,211,.35);color:#78ecdd;font-size:.82rem;font-weight:800}
      .scan-v5-summary{margin:12px 0 0;color:#cfe0e7;line-height:1.6}
      .scan-v5-meta{display:grid;grid-template-columns:1fr;gap:8px;margin:16px 0;padding:14px;border-radius:14px;background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.08)}
      .scan-v5-meta b{color:#fff}
      .scan-v5-grid{display:grid;grid-template-columns:1fr;gap:10px;margin:16px 0}
      .scan-v5-item{padding:13px 14px;border-radius:13px;background:#0d2b3b;border:1px solid #234960}
      .scan-v5-item strong{display:block;color:#fff;margin-bottom:4px}
      .scan-v5-state{font-size:.88rem;font-weight:800;color:#83eadf}
      .scan-v5-state.neutral{color:#c5d4dc}
      .scan-v5-note{margin:16px 0 0;padding-top:14px;border-top:1px solid rgba(255,255,255,.10);color:#aebfc8;line-height:1.55}
      .scan-v5-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
      .scan-v5-actions a{flex:1 1 220px;text-align:center}
      .scan-v5-toast{
        position:fixed;left:16px;right:16px;bottom:22px;z-index:9999;
        max-width:560px;margin:auto;padding:14px 16px;border-radius:14px;
        background:#0b2632;border:1px solid #50dece;color:#f4ffff;
        box-shadow:0 16px 50px rgba(0,0,0,.35);font-weight:800;
        opacity:0;transform:translateY(18px);transition:.22s ease;pointer-events:none
      }
      .scan-v5-toast.show{opacity:1;transform:translateY(0)}
      #scan-submit.scan-v5-busy{opacity:.78;cursor:wait}
      @media (min-width:700px){.scan-v5-grid{grid-template-columns:1fr 1fr}}
    `;
    document.head.appendChild(style);
  }

  function toast(message) {
    let el = document.getElementById('scan-v5-toast');
    if (!el) {
      el = document.createElement('div');
      el.id = 'scan-v5-toast';
      el.className = 'scan-v5-toast';
      el.setAttribute('role', 'status');
      el.setAttribute('aria-live', 'polite');
      document.body.appendChild(el);
    }
    el.textContent = message;
    el.classList.add('show');
    window.clearTimeout(el._t);
    el._t = window.setTimeout(() => el.classList.remove('show'), 2200);
  }

  const esc = value => String(value).replace(/[&<>"']/g, c => ({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
  }[c]));

  function renderError(out, title, body) {
    out.hidden = false;
    out.className = 'scan-v5-result';
    out.setAttribute('role','alert');
    out.innerHTML = `
      <div class="scan-v5-head">
        <div class="scan-v5-title">${esc(title)}</div>
        <span class="scan-v5-badge">Kontrol gerekli</span>
      </div>
      <p class="scan-v5-summary">${esc(body)}</p>`;
    toast('Kontrol sonucu hazır — aşağıdaki kutuya gidiliyor.');
    requestAnimationFrame(() => out.scrollIntoView({behavior:'smooth', block:'center'}));
  }

  function renderResult(out, parsed, typeValue) {
    const https = parsed.protocol === 'https:';
    const rows = [
      ['1. Erişilebilirlik', 'Tam tarama gerekli'],
      ['2. Yapılandırılmış veri', 'Tam tarama gerekli'],
      ['3. Ürün / hizmet gerçekleri', 'Tam tarama gerekli'],
      ['4. Fiyat / stok / kapsam', 'Tam tarama gerekli'],
      ['5. Politika / güven bilgileri', 'Tam tarama gerekli'],
      ['6. İşlem / sonraki adım', 'Tam tarama gerekli'],
      ['7. Doğrulanabilirlik', https ? 'HTTPS doğrulandı; içerik taraması gerekli' : 'HTTPS yok; içerik taraması gerekli']
    ];

    out.hidden = false;
    out.className = 'scan-v5-result';
    out.setAttribute('role','status');
    out.setAttribute('aria-live','polite');
    out.innerHTML = `
      <div class="scan-v5-head">
        <div>
          <div class="scan-v5-title">Ön kontrol tamamlandı</div>
          <p class="scan-v5-summary">Girilen adres teknik olarak ayrıştırıldı. İçerik taranmadan puan veya uygunluk iddiası üretilmedi.</p>
        </div>
        <span class="scan-v5-badge">Sonuç hazır ✓</span>
      </div>

      <div class="scan-v5-meta">
        <div><b>Alan adı:</b> ${esc(parsed.hostname)}</div>
        <div><b>İçerik türü:</b> ${esc(typeValue || 'Belirtilmedi')}</div>
        <div><b>Bağlantı:</b> ${https ? 'HTTPS kullanılıyor ✓' : 'HTTP — HTTPS önerilir'}</div>
        <div><b>Hazırlık skoru:</b> İçerik taranmadan puan verilmez</div>
      </div>

      <div class="scan-v5-grid">
        ${rows.map(([name,state]) => `
          <div class="scan-v5-item">
            <strong>${esc(name)}</strong>
            <span class="scan-v5-state ${state.startsWith('Tam') ? 'neutral' : ''}">${esc(state)}</span>
          </div>`).join('')}
      </div>

      <p class="scan-v5-note"><b>Bu sonuç ne anlama geliyor?</b><br>
      Bu sayfa statik GitHub Pages üzerinde çalıştığı için üçüncü taraf sitenin HTML'ini güvenilir biçimde crawl etmez.
      Buradaki ön kontrol yalnız URL'nin geçerliliğini, alan adını, protokolü ve seçilen içerik türünü doğrular.
      Gerçek 7 kategorili analizde sayfanın HTML'i, yapılandırılmış verisi, kanıt URL'leri ve kullanıcıya açık içerikleri incelenir.</p>

      <div class="scan-v5-actions">
        <a class="btn primary" href="/surec-analizi.html">Tam site analizi iste</a>
      </div>`;

    toast('Ön kontrol tamamlandı — sonuç ekranına gidiliyor.');
    requestAnimationFrame(() => out.scrollIntoView({behavior:'smooth', block:'center'}));
  }

  function init() {
    injectStyles();

    const oldForm = document.getElementById('scan');
    if (!oldForm) return;

    /* Clone removes all previously attached submit/click listeners. */
    const form = oldForm.cloneNode(true);
    oldForm.replaceWith(form);
    form.removeAttribute('onsubmit');

    const input = form.querySelector('#url') || form.querySelector('input[type="url"]') || form.querySelector('input');
    const type = form.querySelector('#type') || form.querySelector('select');
    const button = form.querySelector('button[type="submit"]') || form.querySelector('button');

    if (!input || !button) return;

    button.id = 'scan-submit';
    button.type = 'submit';
    button.removeAttribute('onclick');
    button.textContent = 'Ön kontrolü başlat';

    let out = document.getElementById('scanout');
    if (!out) {
      out = document.createElement('div');
      out.id = 'scanout';
    }

    /* Physically move result directly below the submit button. */
    button.insertAdjacentElement('afterend', out);
    out.hidden = true;
    out.className = 'scan-v5-result';
    out.innerHTML = '';

    /* Replace stale helper text where present. */
    const helperCandidates = Array.from(form.querySelectorAll('p,.small'));
    helperCandidates.forEach(p => {
      if (/statik demo|uzak siteyi|gerçek tarama/i.test(p.textContent || '')) {
        p.textContent = 'Ön kontrol sonucu butonun hemen altında gösterilir. Tam 7 kategorili analiz, sayfanın gerçek içeriği incelenerek yapılır.';
      }
    });

    form.addEventListener('submit', event => {
      event.preventDefault();
      event.stopImmediatePropagation();

      const raw = (input.value || '').trim();
      if (!raw) {
        renderError(out, 'Web adresi gerekli', 'https:// ile başlayan bir site veya sayfa adresi girin.');
        input.focus();
        return;
      }

      let parsed;
      try {
        parsed = new URL(raw);
      } catch (_) {
        renderError(out, 'Adres biçimini kontrol edin', 'Örnek: https://ornek.com/hizmetler');
        input.focus();
        return;
      }

      if (!['https:','http:'].includes(parsed.protocol)) {
        renderError(out, 'Geçerli bir web adresi girin', 'Yalnız http veya https adresleri desteklenir.');
        return;
      }

      const original = button.textContent;
      button.disabled = true;
      button.classList.add('scan-v5-busy');
      button.textContent = 'Kontrol ediliyor…';
      toast('Ön kontrol başlatıldı…');

      window.setTimeout(() => {
        renderResult(out, parsed, type ? type.value : '');
        button.disabled = false;
        button.classList.remove('scan-v5-busy');
        button.textContent = 'Tekrar kontrol et';
      }, 450);
    }, true);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, {once:true});
  } else {
    init();
  }
})();