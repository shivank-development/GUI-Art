#!/usr/bin/env python3
"""
file_organizer.py

A flexible, safe File Organizer script.

Features:
- Organize files by extension, by modified date (year/month), or by size category.
- Recursive or single-folder operation.
- Dry-run mode to preview changes.
- Move (default) or copy mode.
- Collision-safe naming and undo log to reverse operations.

Usage examples:
    python file_organizer.py --target /path/to/folder --mode ext --recursive
    python file_organizer.py --target . --mode date --date-format %Y-%m --dry-run
    python file_organizer.py --target Downloads --mode size --size-map small:0-1MB,medium:1-10MB,large:10-100MB

Undo last run:
    python file_organizer.py --undo

"""

from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path
from datetime import datetime
import json
import logging
from typing import Dict, Tuple, Optional

# ---------- Configuration ----------
DEFAULT_EXT_CATS: Dict[str, str] = {
    # images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.svg': 'Images', '.webp': 'Images',
    # documents
    '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents', '.md': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents', '.xls': 'Documents', '.xlsx': 'Documents',
    # audio/video
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio', '.mp4': 'Video', '.mkv': 'Video', '.mov': 'Video',
    # archives
    '.zip': 'Archives', '.tar': 'Archives', '.gz': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
    # code
    '.py': 'Code', '.js': 'Code', '.ts': 'Code', '.html': 'Code', '.css': 'Code', '.java': 'Code', '.c': 'Code', '.cpp': 'Code', '.json': 'Code',
}
UNDO_LOG = '.file_organizer_undo.json'

# ---------- Utilities ----------

def human_size(bytesize: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytesize < 1024.0:
            return f"{bytesize:.2f}{unit}"
        bytesize /= 1024.0
    return f"{bytesize:.2f}PB"


def ensure_unique_destination(dest: Path) -> Path:
    """If dest exists, append a counter to filename before the suffix."""
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    counter = 1
    while True:
        new_name = f"{stem} ({counter}){suffix}"
        candidate = parent / new_name
        if not candidate.exists():
            return candidate
        counter += 1


def load_size_map(size_map_str: str) -> Dict[str, Tuple[int, int]]:
    # Expect format: name:min-max,name2:min-max (sizes can be like 0-1MB,1-10MB)
    def parse_size(s: str) -> int:
        s = s.strip().upper()
        if s.endswith('KB'):
            return int(float(s[:-2]) * 1024)
        if s.endswith('MB'):
            return int(float(s[:-2]) * 1024**2)
        if s.endswith('GB'):
            return int(float(s[:-2]) * 1024**3)
        return int(float(s))

    result = {}
    for part in size_map_str.split(','):
        if not part.strip():
            continue
        name, rng = part.split(':', 1)
        lo, hi = rng.split('-', 1)
        result[name.strip()] = (parse_size(lo), parse_size(hi))
    return result

# ---------- Core logic ----------

class Organizer:
    def __init__(self, target: Path, dry_run: bool=False, recursive: bool=False, copy: bool=False, ext_map: Optional[Dict[str,str]]=None):
        self.target = target
        self.dry_run = dry_run
        self.recursive = recursive
        self.copy = copy
        self.ext_map = {k.lower(): v for k, v in (ext_map or DEFAULT_EXT_CATS).items()}
        self.undo_records = []
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger('file_organizer')

    def iter_files(self):
        if self.recursive:
            for p in self.target.rglob('*'):
                if p.is_file() and p.name != UNDO_LOG:
                    yield p
        else:
            for p in self.target.iterdir():
                if p.is_file() and p.name != UNDO_LOG:
                    yield p

    def perform_move(self, src: Path, dest_dir: Path) -> Path:
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name
        dest = ensure_unique_destination(dest)
        self.logger.info(f"{ 'COPY' if self.copy else 'MOVE'}: {src} -> {dest}")
        if not self.dry_run:
            if self.copy:
                shutil.copy2(src, dest)
            else:
                shutil.move(str(src), str(dest))
        # record undo: dest -> src
        self.undo_records.append({'from': str(dest), 'to': str(src)})
        return dest

    def save_undo(self):
        if not self.undo_records:
            return
        path = self.target / UNDO_LOG
        if self.dry_run:
            self.logger.info(f"Dry-run: not writing undo log ({path})")
            return
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({'time': datetime.now().isoformat(), 'actions': self.undo_records}, f, indent=2)
        self.logger.info(f"Undo log written to: {path}")

    def undo(self):
        path = self.target / UNDO_LOG
        if not path.exists():
            self.logger.error("No undo log found.")
            return
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        actions = data.get('actions', [])
        # reverse the actions: move from -> to
        for act in reversed(actions):
            src = Path(act['from'])
            dest = Path(act['to'])
            if not src.exists():
                self.logger.warning(f"Skipping undo; source missing: {src}")
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest_unique = ensure_unique_destination(dest)
            self.logger.info(f"UNDO: {src} -> {dest_unique}")
            if not self.dry_run:
                shutil.move(str(src), str(dest_unique))
        # remove undo log
        if not self.dry_run:
            try:
                path.unlink()
                self.logger.info("Undo log removed.")
            except Exception:
                pass

    def by_extension(self):
        for f in self.iter_files():
            cat = self.ext_map.get(f.suffix.lower(), 'Others')
            dest_dir = self.target / cat
            self.perform_move(f, dest_dir)
        self.save_undo()

    def by_date(self, date_format: str = '%Y-%m'):
        for f in self.iter_files():
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            folder = mtime.strftime(date_format)
            dest_dir = self.target / folder
            self.perform_move(f, dest_dir)
        self.save_undo()

    def by_size(self, size_map: Dict[str, Tuple[int,int]]):
        for f in self.iter_files():
            size = f.stat().st_size
            chosen = None
            for name, (lo, hi) in size_map.items():
                if lo <= size <= hi:
                    chosen = name
                    break
            if chosen is None:
                chosen = 'OtherSizes'
            dest_dir = self.target / chosen
            self.perform_move(f, dest_dir)
        self.save_undo()


# ---------- CLI ----------

def parse_args():
    p = argparse.ArgumentParser(description='File Organizer - group files into folders by extension, date or size')
    p.add_argument('--target', '-t', type=str, default='.', help='Target folder (default: current directory)')
    p.add_argument('--mode', '-m', choices=['ext', 'date', 'size'], default='ext', help='Organizing mode')
    p.add_argument('--recursive', '-r', action='store_true', help='Process files recursively')
    p.add_argument('--dry-run', action='store_true', help='Show actions without performing moves')
    p.add_argument('--copy', action='store_true', help='Copy instead of move')
    p.add_argument('--date-format', default='%Y-%m', help='Date format for --mode date (default: %%Y-%%m)')
    p.add_argument('--size-map', help='Size map for --mode size: name:min-max[,name2:min-max], sizes like 0-1MB,1-10MB')
    p.add_argument('--undo', action='store_true', help='Undo last operation (uses undo log in target)')
    p.add_argument('--ext-map', help='Optional JSON file path providing extension->category mapping')
    return p.parse_args()


def main():
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    if not target.exists() or not target.is_dir():
        print(f"Target not found or not a directory: {target}")
        sys.exit(1)

    ext_map = None
    if args.ext_map:
        try:
            with open(args.ext_map, 'r', encoding='utf-8') as f:
                ext_map = json.load(f)
        except Exception as e:
            print(f"Failed to load ext-map JSON: {e}")
            sys.exit(1)

    org = Organizer(target=target, dry_run=args.dry_run, recursive=args.recursive, copy=args.copy, ext_map=ext_map)

    if args.undo:
        org.undo()
        return

    if args.mode == 'ext':
        org.by_extension()
    elif args.mode == 'date':
        org.by_date(date_format=args.date_format)
    elif args.mode == 'size':
        if not args.size_map:
            print('Size mode requires --size-map specification (example: small:0-1MB,medium:1-10MB)')
            sys.exit(1)
        size_map = load_size_map(args.size_map)
        org.by_size(size_map)

if __name__ == '__main__':
    main()
