from pathlib import Path

ROOT = Path(".").cwd()
MIRRORS = ROOT.joinpath("mirrors")

def get_mirror_path(mirror_name: str) -> Path:
    return MIRRORS.joinpath(f"{mirror_name}.mirror")
