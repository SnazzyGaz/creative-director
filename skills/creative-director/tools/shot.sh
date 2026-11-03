#!/bin/sh
# shot.sh FILE.html OUTPREFIX  -> OUTPREFIX-390.png, OUTPREFIX-1280.png
for w in 390 1280; do
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=$w,1400 --screenshot="$2-$w.png" "file://$(realpath $1)" >/dev/null 2>&1
done
# 200% zoom check (UI-10): 1280 px window at 2x zoom = 640 CSS px at device scale 2
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=640,1400 --force-device-scale-factor=2 --screenshot="$2-zoom200.png" "file://$(realpath $1)" >/dev/null 2>&1
