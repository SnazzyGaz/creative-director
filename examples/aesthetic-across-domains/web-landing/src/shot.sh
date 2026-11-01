#!/bin/sh
# shot.sh FILE.html OUTPREFIX HEIGHT1280 HEIGHT390 : full-page-ish captures at 1280 and 390, plus 200% zoom
c="google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars"
$c --window-size=1280,$3 --screenshot="$2-1280.png" "file://$(realpath $1)" >/dev/null 2>&1
$c --window-size=390,$4 --force-device-scale-factor=2 --screenshot="$2-390.png" "file://$(realpath $1)" >/dev/null 2>&1
$c --window-size=640,900 --force-device-scale-factor=2 --screenshot="$2-zoom200.png" "file://$(realpath $1)" >/dev/null 2>&1
