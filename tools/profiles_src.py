"""Source for the first gallery profiles. Writes one JSON file per profile into profiles/.

Kept only as a record of how the first batch was made; contributors just add JSON files.
Run from the repository root: python tools/profiles_src.py
"""

import json
from pathlib import Path

ME = "HiddenOnLies"
OUT = Path(__file__).resolve().parent.parent / "profiles"


def L(effect, keys=None, blend=None, opacity=None, **params):
    layer = {"effect": effect, "params": params}
    if keys:
        layer["keys"] = keys
    if blend:
        layer["blend"] = blend
    if opacity is not None:
        layer["opacity"] = opacity
    return layer


def sparkle(colors, density=0.07, period=3.0, seed=1, opacity=None):
    return L("starlight", blend="add", opacity=opacity, colors=colors, background="#000000",
             density=density, period=period, seed=seed)


ORIGINALS = {
    "thunderstorm": ("Thunderstorm", "Blue rain with a lightning flash every few seconds.",
                     ["animated", "nature"], [
        L("rain", colors=["#3f6cff", "#9cc0ff"], background="#0a1232", speed=0.8, density=0.9, length=0.4),
        L("heartbeat", blend="add", opacity=0.8, color="#dfe8ff", bpm=9, min=0.0),
    ]),
    "bioluminescence": ("Bioluminescence", "A dark sea that glows where you type.",
                        ["animated", "reactive", "nature"], [
        L("plasma", colors=["#001826", "#00453f", "#007a6a", "#001020"], speed=0.12, scale=1.2),
        sparkle(["#40ffe0", "#7cc8ff"], density=0.06, period=3.5),
        L("reactive", colors=["#30ffd0"], style="ripple", duration=1.2, speed=0.8),
    ]),
    "ember_keys": ("Ember Keys", "Low flames along the bottom; the keys you press glow like embers.",
                   ["animated", "reactive"], [
        L("solid", color="#0c0402"),
        L("fire", colors=["#000000", "#6a0800", "#ff3a00", "#ffa000"], speed=0.8, height=0.4),
        L("reactive", colors=["#ff6a00", "#ffb000"], style="key", duration=1.6),
    ]),
    "coral_reef": ("Coral Reef", "Coral and turquoise drifting slowly, with rising bubbles of light.",
                   ["animated", "nature", "chill"], [
        L("color_wave", colors=["#ff5a4a", "#ff9070", "#00b3a6", "#00708a", "#ff5a4a"],
          speed=0.06, angle=30, wavelength=1.6),
        sparkle(["#ffffff", "#c0f8ff"], density=0.05, period=2.5, seed=3),
    ]),
    "glacier": ("Glacier", "Deep blue to ice white, with a slow shine passing over it.",
                ["animated", "chill"], [
        L("gradient", colors=["#8adcff", "#2a7aff", "#06206a"], angle=90),
        L("scanner", blend="add", opacity=0.55, color="#ffffff", background="#000000",
          speed=0.12, width=0.12, angle=25),
    ]),
    "amber_terminal": ("Amber Terminal", "An old amber monitor: dim glow, a refresh line and bright keys as you type.",
                       ["animated", "reactive", "productivity"], [
        L("solid", color="#3a1800"),
        L("scanner", blend="add", opacity=0.45, color="#ff9a00", background="#000000",
          speed=0.25, width=0.06, angle=90),
        L("reactive", colors=["#ffb000"], style="key", duration=0.9),
    ]),
    "firefly_meadow": ("Firefly Meadow", "A dark green field at night with fireflies blinking.",
                       ["animated", "nature", "chill"], [
        L("gradient", colors=["#0c4a1c", "#18702c", "#06300f"], angle=90),
        sparkle(["#e0ff40", "#ffd000"], density=0.07, period=3.5, seed=7),
    ]),
    "nebula": ("Nebula", "Violet and magenta clouds with distant stars.",
               ["animated"], [
        L("plasma", colors=["#26004a", "#8000ff", "#ff2a8a", "#0030a0"], speed=0.1, scale=1.3),
        sparkle(["#ffffff"], density=0.05, period=2.5, seed=11),
    ]),
    "lighthouse": ("Lighthouse", "A warm beam sweeping across a dark night sea.",
                   ["animated", "chill"], [
        L("solid", color="#020a1c"),
        L("scanner", blend="add", color="#fff0b0", background="#000000", speed=0.18, width=0.25, angle=0),
    ]),
    "reactor": ("Reactor", "Green rings pulse out of the core; typing sends out more.",
                ["animated", "reactive", "gaming"], [
        L("solid", color="#001a06"),
        L("ripple", blend="add", center=[0.5, 0.6], colors=["#50ff70", "#00a020"], speed=0.5, thickness=0.1),
        L("breathing", blend="add", opacity=0.3, colors=["#00ff40"], period=3.0, min=0.1),
        L("reactive", colors=["#b0ffb0"], style="ripple", duration=0.8, speed=1.2),
    ]),
    "heat_trail": ("Heat Trail", "Every key you press glows red-hot and cools down slowly.",
                   ["reactive", "productivity"], [
        L("solid", color="#050a22"),
        L("reactive", colors=["#ff3000", "#ff7000"], style="key", duration=4.0),
    ]),
    "coder": ("Coder", "Key groups in distinct colors for programming, with a soft flash on each key.",
              ["static", "reactive", "productivity"], [
        L("solid", color="#2a2a50"),
        L("solid", keys=["@modifiers"], color="#7a5cff"),
        L("solid", keys=["@numbers"], color="#00a8ff"),
        L("solid", keys=["@fn_row"], color="#ff8a00"),
        L("solid", keys=["@arrows", "@nav"], color="#00ff9a"),
        L("reactive", colors=["#ffffff"], style="key", duration=0.5),
    ]),
    "arena": ("Arena", "Pulsing WASD, gold ability keys and a shockwave on every press.",
              ["animated", "reactive", "gaming"], [
        L("solid", color="#0a0010"),
        L("breathing", keys=["@wasd"], colors=["#ff2050"], period=1.6, min=0.35),
        L("solid", keys=["@numbers"], color="#ffb000"),
        L("reactive", colors=["#ff2050", "#ffb000"], style="ripple", duration=0.7, speed=1.4),
    ]),
    "snowfall": ("Snowfall", "Slow white flakes falling on a cold night.",
                 ["animated", "chill", "seasonal"], [
        L("rain", colors=["#ffffff", "#bcd8ff"], background="#0c1c40", speed=0.25, density=0.7, length=0.15),
    ]),
}

# Well-known themes (palettes used under the MIT License, see CREDITS.md), each with its own design
THEMES = {
    "catppuccin_mocha": ("Catppuccin Mocha", "Catppuccin", "Mauve, pink, blue and teal flowing softly; lavender ripples as you type.",
                         ["animated", "reactive"], [
        L("solid", color="#1e1e2e"),
        L("plasma", colors=["#8a4dff", "#1e1e2e", "#ff5ab8", "#161a40", "#3a7dff", "#1e1e2e", "#20c8b0"], speed=0.08, scale=0.8),
        L("reactive", colors=["#b4befe"], style="ripple", duration=0.9),
    ]),
    "dracula": ("Dracula", "Dracula", "Purple to pink, with green, cyan and yellow sparks.",
                ["animated", "reactive"], [
        L("gradient", colors=["#bd93f9", "#ff79c6"], angle=0),
        sparkle(["#50fa7b", "#8be9fd", "#f1fa8c"], density=0.08, period=2.0, seed=4),
        L("reactive", colors=["#8be9fd"], style="key", duration=0.6),
    ]),
    "nord": ("Nord", "Nord", "Frost blues and aurora green moving like northern lights.",
             ["animated", "chill"], [
        L("color_wave", colors=["#2a5cb0", "#3f8ad8", "#30bcd8", "#30d0b0", "#70d060", "#2a5cb0"],
          speed=0.05, angle=10, wavelength=1.5),
        L("breathing", blend="add", opacity=0.15, colors=["#eceff4"], period=7.0, min=0.0),
    ]),
    "gruvbox": ("Gruvbox", "Gruvbox", "Warm red, orange and yellow like a campfire; aqua on the keys you press.",
                ["animated", "reactive"], [
        L("plasma", colors=["#cc241d", "#fe8019", "#fabd2f", "#d65d0e"], speed=0.2, scale=1.1),
        L("reactive", colors=["#8ec07c"], style="key", duration=0.8),
    ]),
    "tokyo_night": ("Tokyo Night", "Tokyo Night", "Neon rain over a night city; orange where you type.",
                    ["animated", "reactive"], [
        L("rain", colors=["#7aa2f7", "#bb9af7", "#7dcfff"], background="#1c2350", speed=0.45, density=0.85, length=0.3),
        L("reactive", colors=["#ff9e64"], style="key", duration=0.7),
    ]),
    "rose_pine": ("Rosé Pine", "Rosé Pine", "Love, gold, rose, iris and pine drifting very slowly.",
                  ["animated", "chill"], [
        L("color_wave", colors=["#ff3f7f", "#ffaa30", "#ff7a8a", "#a070ff", "#1f8fb0", "#ff3f7f"],
          speed=0.035, angle=20, wavelength=2.0),
    ]),
    "solarized": ("Solarized", "Solarized", "All eight Solarized accents rolling across the keyboard.",
                  ["animated"], [
        L("color_wave", colors=["#b58900", "#cb4b16", "#dc322f", "#d33682", "#6c71c4", "#268bd2",
                                "#2aa198", "#859900", "#b58900"], speed=0.06, angle=0, wavelength=1.2),
    ]),
    "everforest": ("Everforest", "Everforest", "Soft forest greens with golden fireflies.",
                   ["animated", "nature", "chill"], [
        L("plasma", colors=["#80c040", "#30c088", "#2a6a22", "#40a8a0"], speed=0.07, scale=1.0),
        sparkle(["#dbbc7f", "#e69875"], density=0.06, period=3.0, seed=9),
    ]),
}


def write(stem, name, author, description, tags, layers):
    doc = {"format": "keyglow/1", "name": name, "author": author, "description": description,
           "tags": tags, "layers": layers}
    (OUT / f"{stem.replace('_', '-')}.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                                                         encoding="utf-8", newline="\n")


def main():
    OUT.mkdir(exist_ok=True)
    for stem, (name, desc, tags, layers) in ORIGINALS.items():
        write(stem, name, ME, desc, tags, layers)
    for stem, (name, source, desc, tags, layers) in THEMES.items():
        write(stem, name, f"{ME} · colors from {source} (MIT)", desc, ["theme", *tags], layers)
    print(f"{len(ORIGINALS) + len(THEMES)} profiles in {OUT}")


if __name__ == "__main__":
    main()
