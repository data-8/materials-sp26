#!/usr/bin/env python3
"""
Sync myst.yml TOC with notebooks on disk.
Finds lec/lecNN/, lab/labNN/, hw/hwNN/, project/projectNN/projectNN.ipynb, and sandbox/sandbox.ipynb,
builds the table of contents in order, and updates myst.yml.
Run from repository root. Exits 0 if no change, 2 on error.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
MYST_PATH = REPO_ROOT / "myst.yml"

EXIT_SUCCESS = 0
EXIT_ERROR = 2


def find_numbered_notebooks(parent_dir: str, prefix: str, title_fmt: str) -> list[dict]:
    """Find all prefixNN/prefixNN.ipynb under parent_dir, sorted by NN."""
    base = REPO_ROOT / parent_dir
    if not base.is_dir():
        return []
    pattern = re.compile(rf"^{prefix}(\d+)$")
    entries = []
    for path in sorted(base.iterdir()):
        if not path.is_dir():
            continue
        m = pattern.match(path.name)
        if not m:
            continue
        num = m.group(1)
        nb = path / f"{path.name}.ipynb"
        if nb.is_file():
            rel = str(nb.relative_to(REPO_ROOT))
            title = title_fmt.format(num=int(num), znum=num.zfill(2))
            entries.append({"title": title, "file": rel})
    # Sort by number
    entries.sort(key=lambda e: int(re.search(r"\d+", e["file"]).group()))
    return entries


def find_flat_numbered_notebooks(parent_dir: str, file_prefix: str, title_fmt: str) -> list[dict]:
    """Find all parent_dir/file_prefixN.ipynb (flat), sorted by N."""
    base = REPO_ROOT / parent_dir
    if not base.is_dir():
        return []
    pattern = re.compile(rf"^{re.escape(file_prefix)}(\d+)\.ipynb$")
    entries = []
    for path in base.iterdir():
        if not path.is_file() or path.suffix != ".ipynb":
            continue
        m = pattern.match(path.name)
        if not m:
            continue
        num = m.group(1)
        rel = str(path.relative_to(REPO_ROOT))
        title = title_fmt.format(num=int(num), znum=num.zfill(2))
        entries.append({"title": title, "file": rel})
    entries.sort(key=lambda e: int(re.search(r"\d+", e["file"]).group()))
    return entries


def main() -> int:
    if not MYST_PATH.is_file():
        print(f"Error: {MYST_PATH} not found", file=sys.stderr)
        return EXIT_ERROR

    toc = []

    # Intro (no title, just file)
    intro = REPO_ROOT / "intro.md"
    if intro.exists():
        toc.append({"file": "intro.md"})

    # Lectures
    lectures = find_numbered_notebooks("lec", "lec", "Lecture {znum}")
    if lectures:
        toc.append({"title": "Lectures", "children": lectures})

    # Labs
    labs = find_numbered_notebooks("lab", "lab", "Lab {znum}")
    if labs:
        toc.append({"title": "Labs", "children": labs})

    # Homework
    homework = find_numbered_notebooks("hw", "hw", "Homework {znum}")
    if homework:
        toc.append({"title": "Homework", "children": homework})

    # Projects (nested: project/project01/project01.ipynb, same as lec/lab/hw)
    projects = find_numbered_notebooks("project", "project", "Project {znum}")
    if projects:
        toc.append({"title": "Projects", "children": projects})

    # Sandbox
    sandbox_nb = REPO_ROOT / "sandbox" / "sandbox.ipynb"
    if sandbox_nb.exists():
        toc.append({
            "title": "Sandbox",
            "children": [{"title": "Sandbox", "file": "sandbox/sandbox.ipynb"}],
        })

    try:
        with open(MYST_PATH, "r") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error: invalid YAML in {MYST_PATH}: {e}", file=sys.stderr)
        return EXIT_ERROR

    if data is None:
        data = {}
    if "project" not in data:
        data["project"] = {}

    old_toc = data["project"].get("toc", [])
    if old_toc == toc:
        return EXIT_SUCCESS

    data["project"]["toc"] = toc
    with open(MYST_PATH, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return EXIT_SUCCESS


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(EXIT_ERROR)
