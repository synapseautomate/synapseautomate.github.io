# Synapse Measurement v1

Purpose: connect distribution, on-site value delivery, qualified inbound and payment with one event vocabulary.

Executive events: asset_view → tool_start → tool_complete → lead_form_submit → paid_conversion.

`paid_conversion` remains human-confirmed until an authorized payment integration exists. Browser events are vendor-neutral and push to `dataLayer` / `gtag` when a collector is installed. Form attribution is captured in hidden form fields immediately.

No raw customer data, secrets, legal/health content or payment data belongs in event payloads.
