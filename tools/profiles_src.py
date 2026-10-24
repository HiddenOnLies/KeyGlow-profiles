"""Source for the gallery profiles made by the maintainer. Writes one JSON file per profile into profiles/.

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

# Second batch: profiles that react to typing (each press takes the next color in the list)
INTERACTIVE = {
    "paint-splash": ("Paint Splash", "Every key you press splashes a different color across the board.",
                     ["reactive", "neon"], [
        L("solid", color="#08080c"),
        L("reactive", colors=["#ff2a6d", "#ffb400", "#05d9e8", "#7cff4f", "#b84dff"], style="ripple",
          duration=1.4, speed=0.7),
    ]),
    "sonar": ("Sonar", "A radar sweep in the dark; each key sends out a ping.",
              ["animated", "reactive"], [
        L("solid", color="#001408"),
        L("scanner", blend="add", opacity=0.6, color="#00ff60", background="#000000", speed=0.2, width=0.08, angle=0),
        L("reactive", blend="add", colors=["#80ffb0"], style="ripple", duration=1.6, speed=0.5),
    ]),
    "equalizer": ("Equalizer", "Typing lights whole rows like the bars of a music equalizer.",
                  ["reactive", "neon"], [
        L("gradient", opacity=0.25, colors=["#00e5ff", "#ff00c8"], angle=0),
        L("reactive", colors=["#00e5ff", "#7a5cff", "#ff00c8", "#ff7a00"], style="row", duration=0.7),
    ]),
    "shockwave": ("Shockwave", "A fast white blast from every key over a deep red glow.",
                  ["reactive", "gaming"], [
        L("solid", color="#2a0006"),
        L("reactive", blend="add", colors=["#ffffff"], style="ripple", duration=0.5, speed=2.0),
        L("reactive", colors=["#ff3040"], style="key", duration=0.4),
    ]),
    "typing-rainbow": ("Typing Rainbow", "Each key you press takes the next color of the rainbow.",
                       ["reactive", "productivity"], [
        L("solid", color="#0c0c14"),
        L("reactive", colors=["#ff0040", "#ff8000", "#ffe000", "#40ff40", "#00c0ff", "#4040ff", "#c000ff"],
          style="key", duration=2.2),
    ]),
    "ghost-trail": ("Ghost Trail", "Keys stay lit for a long while after you press them, then fade away.",
                    ["reactive", "chill"], [
        L("solid", color="#04060c"),
        L("reactive", colors=["#a8c8ff"], style="key", duration=7.0),
    ]),
    "pond": ("Pond", "Calm dark water; every key drops a stone and its ripples spread.",
             ["animated", "reactive", "nature", "chill"], [
        L("plasma", colors=["#021030", "#04305a", "#063f4a", "#020c24"], speed=0.08, scale=1.1),
        L("reactive", blend="add", colors=["#8fd8ff"], style="ripple", duration=2.0, speed=0.55),
    ]),
    "negative": ("Negative", "A bright keyboard where the keys you press go dark and slowly light up again.",
                 ["reactive"], [
        L("gradient", colors=["#00e5ff", "#b0f8ff", "#00e5ff"], angle=0),
        L("reactive", colors=["#000000"], style="key", duration=1.8),
    ]),
    "magma-typing": ("Magma Typing", "Lava along the bottom; typing sends white-hot waves through it.",
                     ["animated", "reactive"], [
        L("solid", color="#1a0300"),
        L("fire", colors=["#000000", "#800000", "#ff3000", "#ff9000"], speed=0.6, height=0.5),
        L("reactive", blend="add", colors=["#ffd080"], style="ripple", duration=0.9, speed=1.1),
    ]),
    "neon-pulse": ("Neon Pulse", "Cyan rows and magenta keys flash over a dim neon gradient.",
                   ["animated", "reactive", "neon"], [
        L("color_wave", opacity=0.35, colors=["#ff00c8", "#00e5ff", "#ff00c8"], speed=0.08, angle=0),
        L("reactive", blend="add", opacity=0.6, colors=["#00e5ff"], style="row", duration=0.5),
        L("reactive", colors=["#ff00c8"], style="key", duration=0.9),
    ]),
    "fireworks": ("Fireworks", "A night sky with stars; every key launches a colored burst.",
                  ["animated", "reactive", "seasonal"], [
        L("solid", color="#02020e"),
        sparkle(["#ffffff", "#ffe0a0"], density=0.05, period=2.0, seed=21),
        L("reactive", blend="add", colors=["#ff3060", "#ffd020", "#40c0ff", "#60ff80", "#e060ff"],
          style="ripple", duration=1.0, speed=0.9),
        L("reactive", blend="add", colors=["#ffffff"], style="key", duration=0.3),
    ]),
}

# Third batch. NEW_EFFECTS need KeyGlow 0.4 (swirl, comet, bounce, glitch, cross/burst key presses);
# older versions skip them. MORE uses effects every version has.
NEW_EFFECTS = {
    "hypnosis": ("Hypnosis", "A black and white spiral that never stops turning.",
                 ["animated"], [
        L("swirl", colors=["#ffffff", "#000000"], speed=0.25, twist=1.2),
    ]),
    "galaxy-spiral": ("Galaxy Spiral", "Purple and blue spiral arms with stars; keys burst into light.",
                      ["animated", "reactive"], [
        L("swirl", colors=["#3a00a0", "#ff2a8a", "#0030c0", "#06001a"], speed=0.05, twist=1.6, center=[0.5, 0.55]),
        sparkle(["#ffffff"], density=0.05, period=2.5, seed=31),
        L("reactive", blend="add", colors=["#c0a0ff"], style="burst", duration=0.7, speed=0.6),
    ]),
    "pinwheel": ("Pinwheel", "The whole rainbow turning around the middle of the keyboard.",
                 ["animated", "neon"], [
        L("swirl", colors=["#ff0000", "#ff8000", "#ffff00", "#00ff00", "#00ffff", "#0040ff", "#8000ff", "#ff00c0"],
          speed=0.2),
    ]),
    "snake": ("Snake", "A green snake slithers across every row; your keys flash as it goes.",
              ["animated", "reactive", "gaming"], [
        L("comet", color="#40ff40", background="#001400", speed=0.12, length=0.22),
        L("reactive", colors=["#ffe000"], style="key", duration=0.5),
    ]),
    "shooting-star": ("Shooting Star", "A white comet crossing a starry blue night.",
                      ["animated", "chill"], [
        L("gradient", colors=["#000a30", "#06205a"], angle=90),
        sparkle(["#ffffff", "#a0c0ff"], density=0.05, period=3.0, seed=17),
        L("comet", blend="add", color="#ffffff", background="#000000", speed=0.08, length=0.28),
    ]),
    "pong": ("Pong", "A ball bouncing around a black table; keys burst on contact with your fingers.",
             ["animated", "reactive", "gaming"], [
        L("bounce", color="#ffffff", background="#000000", speed=0.35, size=0.08),
        L("reactive", blend="add", colors=["#00ff80"], style="burst", duration=0.4, speed=0.8),
    ]),
    "sunball": ("Sunball", "A big warm sun drifting and bouncing over an orange sky.",
                ["animated", "chill"], [
        L("gradient", colors=["#1a0400", "#4a1000"], angle=90),
        L("bounce", blend="add", color="#ffe060", background="#000000", speed=0.12, size=0.2),
    ]),
    "signal-lost": ("Signal Lost", "Cyan and magenta glitches; every key lights its row and column.",
                    ["animated", "reactive", "neon"], [
        L("glitch", colors=["#00e5ff", "#ff00c8", "#ffffff"], background="#05000a", density=0.3, speed=0.6),
        L("reactive", blend="add", colors=["#ffffff"], style="cross", duration=0.35),
    ]),
    "cyber-glitch": ("Cyber Glitch", "A neon wave that keeps breaking up.",
                     ["animated", "neon"], [
        L("color_wave", colors=["#ff00c8", "#7000ff", "#00e5ff", "#ff00c8"], speed=0.1),
        L("glitch", blend="add", opacity=0.8, colors=["#ffffff", "#ffe000"], background="#000000",
          density=0.15, speed=0.8, seed=8),
    ]),
    "crosshair": ("Crosshair", "Red WASD; every key you press draws a crosshair through it.",
                  ["reactive", "gaming"], [
        L("solid", color="#0a0002"),
        L("solid", keys=["@wasd"], color="#ff1030"),
        L("reactive", blend="add", colors=["#ff3040"], style="cross", duration=0.45),
        L("reactive", colors=["#ffffff"], style="key", duration=0.3),
    ]),
    "supernova": ("Supernova", "A starfield where every key explodes into a colored disc.",
                  ["animated", "reactive"], [
        L("solid", color="#02020c"),
        sparkle(["#ffffff", "#ffd0a0"], density=0.06, period=2.0, seed=41),
        L("reactive", blend="add", colors=["#ff3000", "#ffb000", "#ff00a0", "#40a0ff"], style="burst",
          duration=0.8, speed=0.9),
    ]),
}

MORE = {
    "candy-rain": ("Candy Rain", "Pink, yellow and mint drops falling on a dark purple background.",
                   ["animated"], [
        L("rain", colors=["#ff4fb0", "#ffd000", "#30ffb0"], background="#2a0040", speed=0.5, density=1.0, length=0.5),
    ]),
    "thermal-camera": ("Thermal Camera", "Heat-vision colors moving slowly; typing makes the keys hot.",
                       ["animated", "reactive"], [
        L("plasma", colors=["#000020", "#3000a0", "#b0007a", "#ff3000", "#ffc000"], speed=0.1, scale=1.2),
        L("reactive", colors=["#ffffc0", "#ffc000"], style="ripple", duration=0.8, speed=1.0),
    ]),
    "deep-focus": ("Deep Focus", "Calm warm white for long work sessions; letters a little brighter.",
                   ["static", "productivity"], [
        L("solid", color="#2a1a0a"),
        L("solid", keys=["@letters"], color="#ffb060"),
        L("breathing", blend="multiply", colors=["#ffffff"], period=10.0, min=0.7),
    ]),
    "metronome": ("Metronome", "A thin white line ticking back and forth over a soft pulse.",
                  ["animated", "chill"], [
        L("heartbeat", color="#300818", bpm=60, min=0.4),
        L("scanner", blend="add", color="#ffffff", background="#000000", speed=0.5, width=0.04),
    ]),
}

# Fourth batch: more combinations of the KeyGlow 0.4 effects
BATCH4 = {
    "radar": ("Radar", "A single green arm sweeps around the keyboard like a radar screen; keys show up as blips.",
              ["animated", "reactive", "gaming"], [
        L("swirl", colors=["#40ff60", "#002a08", "#000a02", "#000a02", "#000a02", "#00200a"], speed=0.25),
        L("reactive", blend="add", colors=["#c0ffc0"], style="burst", duration=0.6, speed=0.5),
    ]),
    "whirlpool": ("Whirlpool", "Deep blue water spiraling into the middle; typing throws up foam.",
                  ["animated", "reactive", "nature"], [
        L("swirl", colors=["#002a6a", "#00a0d0", "#001a40", "#0060a0"], speed=0.12, twist=-2.2),
        L("reactive", blend="add", colors=["#e0ffff"], style="burst", duration=0.5, speed=0.6),
    ]),
    "twin-comets": ("Twin Comets", "A cyan and a magenta comet chasing each other across the rows.",
                    ["animated", "neon"], [
        L("solid", color="#04000c"),
        L("comet", blend="add", color="#00e5ff", background="#000000", speed=0.1, length=0.2),
        L("comet", blend="add", color="#ff00c8", background="#000000", speed=0.07, length=0.25),
    ]),
    "disco-ball": ("Disco Ball", "A turning rainbow with colored sparks flying everywhere.",
                   ["animated", "neon"], [
        L("swirl", opacity=0.45, colors=["#ff0040", "#ffe000", "#00ff80", "#0080ff", "#c000ff"], speed=0.3),
        L("starlight", blend="add", colors=["#ffffff", "#ff40c0", "#40e0ff", "#ffe040"], background="#000000",
          density=0.3, period=0.8, seed=51),
    ]),
    "breakout": ("Breakout", "Rainbow bricks along the top and a ball bouncing below them.",
                 ["animated", "reactive", "gaming"], [
        L("solid", color="#020208"),
        L("gradient", keys=["@fn_row", "@numbers"], colors=["#ff2020", "#ff9000", "#ffe000", "#20ff40", "#2080ff", "#a020ff"]),
        L("bounce", blend="add", color="#ffffff", background="#000000", speed=0.4, size=0.09),
        L("reactive", colors=["#ffffff"], style="key", duration=0.3),
    ]),
    "static-tv": ("Static TV", "Grey snow and flickering lines, like a TV with no signal.",
                  ["animated"], [
        L("glitch", colors=["#ffffff", "#9a9a9a", "#5a5a5a"], background="#141414", density=0.9, speed=1.5, seed=13),
    ]),
    "matrix-glitch": ("Matrix Glitch", "Falling green code that keeps breaking up.",
                      ["animated", "neon"], [
        L("rain", colors=["#00ff40", "#a0ffa0"], background="#001a06", speed=0.7, density=1.0, length=0.5),
        L("glitch", blend="add", opacity=0.7, colors=["#40ff80", "#ffffff"], background="#000000",
          density=0.12, speed=0.9, seed=27),
    ]),
    "heartline": ("Heartline", "A slow red heartbeat; every key draws a pink cross through it.",
                  ["animated", "reactive"], [
        L("heartbeat", color="#ff0030", bpm=62, min=0.12),
        L("reactive", blend="add", colors=["#ff80c0"], style="cross", duration=0.5),
    ]),
    "lava-blobs": ("Lava Blobs", "Two warm blobs drifting and bouncing through dark red lava.",
                   ["animated", "chill"], [
        L("plasma", colors=["#200200", "#5a0a00", "#300400"], speed=0.08, scale=1.0),
        L("bounce", blend="add", color="#ff6000", background="#000000", speed=0.09, size=0.2),
        L("bounce", blend="add", color="#ffb000", background="#000000", speed=0.06, size=0.15),
    ]),
    "kaleidoscope": ("Kaleidoscope", "A rainbow spiral under flowing color, always changing.",
                     ["animated", "neon"], [
        L("swirl", colors=["#ff0080", "#ffb000", "#00e5ff", "#7000ff"], speed=0.18, twist=2.0),
        L("plasma", blend="screen", opacity=0.5, colors=["#000000", "#ff00a0", "#000000", "#00c0ff"], speed=0.2, scale=1.2),
    ]),
    "electric-storm": ("Electric Storm", "Bolts of blue-white static over a violet sky; keys crackle when pressed.",
                       ["animated", "reactive"], [
        L("gradient", colors=["#1a0040", "#3a0070"], angle=90),
        L("glitch", blend="add", colors=["#a0c0ff", "#ffffff"], background="#000000", density=0.22, speed=1.2, seed=33),
        L("reactive", blend="add", colors=["#c0d8ff"], style="ripple", duration=0.5, speed=1.6),
    ]),
    "zen-garden": ("Zen Garden", "Soft sand-colored rings spreading slowly; each key adds a ripple.",
                   ["animated", "reactive", "chill"], [
        L("ripple", colors=["#d0a060", "#806030"], background="#140c04", speed=0.08, thickness=0.18),
        L("reactive", blend="add", colors=["#ffe0b0"], style="ripple", duration=2.0, speed=0.4),
    ]),
    "ocean-swell": ("Ocean Swell", "Blue swells rolling from top to bottom; typing breaks them into foam.",
                    ["animated", "reactive", "nature"], [
        L("color_wave", colors=["#001a50", "#0070c0", "#00b0d0", "#001a50"], speed=0.08, angle=90, wavelength=1.2),
        L("reactive", blend="add", colors=["#ffffff"], style="burst", duration=0.6, speed=0.7),
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
    for stem, (name, desc, tags, layers) in INTERACTIVE.items():
        write(stem, name, ME, desc, tags, layers)
    for stem, (name, desc, tags, layers) in {**NEW_EFFECTS, **MORE}.items():
        write(stem, name, ME, desc, tags, layers)
    for stem, (name, desc, tags, layers) in BATCH4.items():
        write(stem, name, ME, desc, tags, layers)
    for stem, (name, source, desc, tags, layers) in THEMES.items():
        write(stem, name, f"{ME} · colors from {source} (MIT)", desc, ["theme", *tags], layers)
    print(f"{len(ORIGINALS) + len(INTERACTIVE) + len(NEW_EFFECTS) + len(MORE) + len(BATCH4) + len(THEMES)} profiles in {OUT}")


if __name__ == "__main__":
    main()
