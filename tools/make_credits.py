"""Writes CREDITS.md: the palettes the theme profiles use, with their MIT license texts.

Run from the repository root: python tools/make_credits.py
"""

from pathlib import Path

MIT = """Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# (palette, profile file, source repository, copyright line from its LICENSE)
SOURCES = [
    ("Catppuccin", "catppuccin-mocha.json", "https://github.com/catppuccin/palette",
     "Copyright (c) 2021 Catppuccin"),
    ("Dracula", "dracula.json", "https://github.com/dracula/dracula-theme",
     "Copyright (c) 2023 Dracula Theme"),
    ("Nord", "nord.json", "https://github.com/nordtheme/nord",
     "Copyright (c) 2016-present Sven Greb <development@svengreb.de> (https://www.svengreb.de)"),
    ("Gruvbox", "gruvbox.json", "https://github.com/gruvbox-community/gruvbox",
     "Copyright (c) 2018 Pavel Pertsev"),
    ("Tokyo Night", "tokyo-night.json", "https://github.com/enkia/tokyo-night-vscode-theme",
     "Copyright (c) 2018-present Enkia"),
    ("Rosé Pine", "rose-pine.json", "https://github.com/rose-pine/neovim",
     "Copyright (c) 2023 Rosé Pine"),
    ("Solarized", "solarized.json", "https://github.com/altercation/solarized",
     "Copyright (c) 2011 Ethan Schoonover"),
    ("Everforest", "everforest.json", "https://github.com/sainnhe/everforest",
     "Copyright (c) 2019 sainnhe"),
]


def main():
    out = ["# Credits", "",
           "The theme profiles use colors from the palettes below, each under the MIT License. Some",
           "colors are made more saturated so they show on LEDs; the designs (effects and layers) are",
           "KeyGlow's own.", "",
           "| Palette | Profile | Source |", "|---|---|---|"]
    out += [f"| {n} | [`{f}`](profiles/{f}) | {u} |" for n, f, u, _ in SOURCES]
    for n, _, _, c in SOURCES:
        out += ["", f"## {n}", "", "```", "MIT License", "", c, "", MIT, "```"]
    root = Path(__file__).resolve().parent.parent
    (root / "CREDITS.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
