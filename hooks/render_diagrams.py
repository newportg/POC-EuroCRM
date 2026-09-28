"""MkDocs hook: renders Obsidian-embedded PlantUML (.puml) diagrams to PNG.

The vault embeds diagrams with Obsidian's `![[name.puml]]` syntax, which the
roamlinks plugin resolves into a normal markdown image pointing at the raw
`.puml` source (`![name.puml](<../name.puml>)`). Hooks always run their
on_page_markdown after regular plugins, so by the time this hook sees the
markdown, roamlinks has already resolved the relative path — this hook just
swaps the `.puml` reference for the rendered `.png` sitting next to it.
"""
import re
import shutil
import subprocess
from pathlib import Path

IMG_PUML_RE = re.compile(r"!\[([^\]]*?)\.puml\]\((<?)([^)>]*?)\.puml(>?)\)")


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    puml_files = sorted(docs_dir.rglob("*.puml"))
    if not puml_files:
        return

    plantuml = shutil.which("plantuml")
    if not plantuml:
        print(
            "WARNING - render_diagrams hook: 'plantuml' CLI not found on PATH, "
            "skipping diagram rendering (.puml embeds will not resolve)."
        )
        return

    for puml in puml_files:
        subprocess.run([plantuml, "-tpng", str(puml)], check=True)


def on_page_markdown(markdown, **kwargs):
    return IMG_PUML_RE.sub(
        lambda m: f"![{m.group(1)}.png]({m.group(2)}{m.group(3)}.png{m.group(4)})",
        markdown,
    )
