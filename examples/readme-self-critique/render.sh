#!/bin/sh
# render.sh OUTPREFIX : render README.md with GitHub's own markdown API (needs gh, logged in) and
# github-markdown-css, then screenshot with headless Chrome at 1280 and 390 px.
R=$(cd "$(dirname "$0")/../.." && pwd); T=$(mktemp -d)
curl -sL -o $T/gh.css https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css
python3 -c "import json;print(json.dumps({'text':open('$R/README.md').read(),'mode':'markdown'}))" > $T/req.json
gh api markdown --input $T/req.json > $T/body.html
{ echo "<html><head><meta charset=utf-8><link rel=stylesheet href=\"file://$T/gh.css\"><style>body{margin:0}.markdown-body{box-sizing:border-box;max-width:1012px;margin:0 auto;padding:32px}@media(max-width:767px){.markdown-body{padding:16px}}</style></head><body><article class=markdown-body>"
  cat $T/body.html; echo "</article></body></html>"; } > "$R/_render.html"
for w in 1280 390; do
  google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --virtual-time-budget=5000 \
    --window-size=$w,4200 --screenshot="$1-$w.png" "file://$R/_render.html" >/dev/null 2>&1
done
rm -rf "$R/_render.html" $T
