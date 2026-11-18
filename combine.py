"""Merge the two reports into one tabbed, self-contained HTML page.
usage: python combine.py TEXT_REPORT.html FILE_REPORT.html OUT.html [title]
"""
import sys, html, pathlib
a, b, out = sys.argv[1:4]
title = sys.argv[4] if len(sys.argv) > 4 else "Αναφορά ελέγχου AI"
rd = lambda p: html.escape(pathlib.Path(p).read_text(encoding="utf-8"), quote=True)
page = f"""<!doctype html><html lang="el"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<style>
:root{{--bg:#fff;--fg:#1a1a1a;--mut:#666;--ac:#2a5bd7;--bd:#ddd}}
@media(prefers-color-scheme:dark){{:root{{--bg:#16181c;--fg:#e8e8e8;--mut:#9aa;--ac:#7aa2ff;--bd:#333}}}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px system-ui,sans-serif}}
input.tb{{position:absolute;opacity:0;pointer-events:none}}
nav label{{border-bottom:3px solid transparent;color:var(--mut);padding:8px 12px;cursor:pointer}}
#t0:checked~nav label[for=t0],#t1:checked~nav label[for=t1]{{color:var(--ac);border-color:var(--ac)}}
#t0:checked~.f0,#t1:checked~.f1{{display:block}}
header{{padding:12px 16px;border-bottom:1px solid var(--bd)}}
h1{{font-size:17px;margin:0 0 4px}} p{{margin:0;color:var(--mut);font-size:13px}}
nav{{display:flex;gap:4px;padding:8px 16px 0;border-bottom:1px solid var(--bd)}}
nav button{{background:none;border:0;border-bottom:3px solid transparent;color:var(--mut);padding:8px 12px;font:inherit;cursor:pointer}}
nav button[aria-selected=true]{{color:var(--ac);border-color:var(--ac)}}
iframe{{border:0;width:100%;height:calc(100vh - 120px);min-height:600px;background:#fff;display:none}}
</style></head><body>
<header><h1>{html.escape(title)}</h1>
<p>Ανάγνωση editor (Mode B) + έλεγχος μεταδεδομένων αρχείου. Δεν αποτελεί απόδειξη για τίποτα και δεν προβλέπει το αποτέλεσμα Turnitin/GPTZero. Περιέχει ολόκληρο το κείμενο: κράτα το ιδιωτικό.</p></header>
<input class="tb" type="radio" name="t" id="t0" checked><input class="tb" type="radio" name="t" id="t1">
<nav><label for="t0">Ανάγνωση κειμένου</label><label for="t1">Μεταδεδομένα αρχείου</label></nav>
<iframe class="f0" srcdoc="{rd(a)}"></iframe><iframe class="f1" srcdoc="{rd(b)}"></iframe></body></html>"""
pathlib.Path(out).write_text(page, encoding="utf-8")
print("wrote", out, len(page)//1024, "KB")
