# Updating the lookbook

Looks are made in batches in a separate breeder folder (renders, research and source notes stay there). Only the shareable export comes into this repo.

1. **Re-export in the breeder.** Rebuild its tag file and sheets, run its share check, and make sure `SHARE_MANIFEST.txt` is current. Private research and source notes are never on the manifest.
2. **Sync.** From the repo root:
   ```
   python3 tools/lookbook_sync.py /path/to/breeder --dry-run
   python3 tools/lookbook_sync.py /path/to/breeder --scan modules/lookbook/README.md CHANGELOG.md
   ```
   It copies only manifest files (each sheet's 1200 px `_small.jpg`, saved as `sheets/<name>.jpg`, and `index.png`), keeps only `share_safe = yes` and `status = live` rows, drops internal fields, and writes `looks.json` and `looks.csv`. It then name-checks every text against the breeder's banned list and stops on any hit.
3. **IDs.** IDs never change. A retired look moves to the `retired` list (ID, date, short note) and its ID is never reused; the sync stops if a live ID matches a retired one or vanishes without being retired.
4. **Review.** Look at the new sheets at full size; update the counts in `README.md` and the token row in `core/which-modules.md` if the README changed.
5. **Release.** Add a CHANGELOG entry (batch number, looks added and retired, size added) and bump the minor version.

Naming rule: looks are named by technique, structure or broad historic era. Never tie a look to a living or recent artist, studio, community, real place or specific work, even as a reference.

Size: each sheet is about 0.4 MB, so 100 new looks add about 7 MB. If the module passes about 50 MB, move the sheets to release assets and keep only `looks.json` and `index.png` in the tree.
