"""fetch_assets.py: download the files kept out of git from the `assets-v1` release and unpack them in place.

Run from the repo root:
  python3 tools/fetch_assets.py            # font files into fonts/<theme>/<family>/ (needed by fonts/build.py and docs/assets/src/)
  python3 tools/fetch_assets.py --examples # full-size example images over the smaller copies in examples/
  python3 tools/fetch_assets.py --lookbook # full-size lookbook sheets and index.png
  python3 tools/fetch_assets.py --all

Checks each zip against SHA256SUMS.txt from the same release. Standard library only. Don't commit the unpacked
files: fonts are in .gitignore; for examples and lookbook, `git checkout -- examples modules/lookbook` restores
the small copies.
"""
import argparse, hashlib, io, os, sys, urllib.request, zipfile

BASE = "https://github.com/SnazzyGaz/creative-director/releases/download/assets-v1/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIPS = {"fonts": "creative-director-fonts.zip", "examples": "creative-director-examples-full.zip",
        "lookbook": "creative-director-lookbook-full.zip"}

def get(name):
    with urllib.request.urlopen(BASE + name, timeout=120) as r:
        return r.read()

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for k in ZIPS: ap.add_argument("--" + k, action="store_true")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    want = [k for k in ZIPS if a.all or getattr(a, k)] or ["fonts"]
    sums = dict(reversed(l.split()) for l in get("SHA256SUMS.txt").decode().splitlines() if l.strip())
    for k in want:
        name = ZIPS[k]; data = get(name)
        if hashlib.sha256(data).hexdigest() != sums.get(name):
            sys.exit(f"{name}: checksum mismatch, nothing unpacked")
        n = 0
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for m in z.infolist():
                dest = os.path.normpath(os.path.join(ROOT, m.filename))
                if not dest.startswith(ROOT + os.sep): sys.exit(f"{name}: bad path {m.filename}")
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f: f.write(z.read(m))
                n += 1
        print(f"{name}: {n} files, {len(data) / 1e6:.1f} MB")

if __name__ == "__main__":
    main()
