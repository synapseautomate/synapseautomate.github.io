# FormSubmit / iletişim / teşekkür
Süreç analizi: doğrudan HTML FormSubmit POST, _next talep-alindi.html?submitted=process_analysis.
İletişim: HTML action yok; app-v33.js JS ile FormSubmit POST action ve _next talep-alindi.html ekliyor.
JS kapalı iletişimde garanti edilmiş FormSubmit yolu yok; süreçte JS kapalı pending olmadığı için generate_lead yok.
Teşekkür: data-synapse-success=process_analysis; iletişim URL'sinde submitted yok, generate_lead beklenmez.
Gizlilik sayfası mailto taslağı diyor fakat JS gerçek POST yönlendiriyor — P0.
lead_form_submit gönderim denemesi, generate_lead redirect; ikisi de gerçek e-posta teslimi değil.
Canlı form POST 0 ADET denendi, e-posta teslimi TEST EDİLEMEDİ.
