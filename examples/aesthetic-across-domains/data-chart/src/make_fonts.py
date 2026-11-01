"""Static instances of the repo's variable fonts for matplotlib (which only uses a variable font's default).
Writes to /tmp/aad-static-fonts/."""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
OUT = "/tmp/aad-static-fonts"; os.makedirs(OUT, exist_ok=True)
JOBS = [("editorial-serif/newsreader/Newsreader[opsz,wght].ttf", {"opsz": 36, "wght": 560}, "Newsreader-36-560.ttf"),
        ("humanist-sans/sourcesans3/SourceSans3[wght].ttf", {"wght": 400}, "SourceSans3-400.ttf"),
        ("humanist-sans/sourcesans3/SourceSans3[wght].ttf", {"wght": 600}, "SourceSans3-600.ttf")]
for src, loc, name in JOBS:
    f = TTFont(os.path.join(REPO, "fonts", src))
    s = instancer.instantiateVariableFont(f, loc, overlap=instancer.OverlapMode.REMOVE)
    s.save(os.path.join(OUT, name)); print(name)
