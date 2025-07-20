import shutil
from pathlib import Path

def recursive_copy(src, dst):
    if not dst.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_dir():
            new_dst = dst / item.name
            new_dst.mkdir(exist_ok=True)
            recursive_copy(item, new_dst)
        else:
            shutil.copy2(item, dst / item.name)

def main():
    src = Path("static")
    dst = Path("public")
    if dst.exists():
        shutil.rmtree(dst)
    recursive_copy(src, dst)

if __name__ == "__main__":
    main()