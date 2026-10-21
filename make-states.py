#!/usr/bin/env python3
"""Write one static SVG per severity level into states/ from each cone-*.svg."""
import pathlib

out = pathlib.Path("states"); out.mkdir(exist_ok=True)
for src in pathlib.Path(".").glob("cone-*.svg"):
    svg = src.read_text()
    for level, label in enumerate(["nothing", "yellow", "orange", "red"]):
        (out / f"{src.stem}-{label}.svg").write_text(
            svg.replace('data-level="3"', f'data-level="{level}"', 1))
