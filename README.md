# KeyGlow community gallery

Lighting profiles for [KeyGlow](https://github.com/HiddenOnLies/KeyGlow), shared by the
community. They show up in the app under *Profiles → Community*.

![The gallery's profiles](docs/preview.png)

## How KeyGlow uses it

- The app downloads **[`gallery.json`](gallery.json)**, one file with every profile, at most once
  a day. *Community → Check for new* downloads it right away.
- It's cached, so the gallery works offline, and every profile is **validated** before use.
  Profiles are plain JSON data, never code. A copy ships with the app for the first start.
- It can be turned off in KeyGlow: *Settings → Download new profiles from the KeyGlow community gallery*.

## Adding your profile

**From KeyGlow** (easiest): open your profile, then *⋯ → Share to community gallery…*. Fill in
your name, a one-sentence description and some tags, and press *Open GitHub*: GitHub opens with
the file ready. Press *Propose changes* and *Create pull request* (you need a free GitHub account;
GitHub makes a copy of the gallery for you).

**By hand:**

1. Your profiles are `.json` files in `Documents\KeyGlow\Perfiles`.
2. Fill in `author` (your name or GitHub user), a one-sentence `description` and a few `tags`:
   `animated`, `static`, `reactive` (reacts to typing), `gaming`, `chill`, `nature`, `neon`,
   `productivity`, `seasonal`, `theme`.
3. Add it to [`profiles/`](profiles) with a short lowercase file name (`my-profile.json`) and open
   a pull request.

The automatic check validates the profile, and once it's accepted [`gallery.json`](gallery.json)
is rebuilt by itself. To check it on your PC first (needs KeyGlow from source:
`pip install git+https://github.com/HiddenOnLies/KeyGlow`):

```bash
keyglow gallery profiles
```

Good gallery profiles:

- **Look different** from what's already here and from KeyGlow's built-in presets.
- **Work on any keyboard**: use key groups (`@wasd`, `@arrows`, `@numbers`…) or effects that
  cover the whole board, not a fixed list of LED numbers.
- **Look good on real LEDs**: pastel colors turn almost white on a keyboard, and very dark ones
  turn off. Test on your keyboard if you can.
- **Interactive profiles** use *On key press* layers (`reactive`): the key itself, a ripple
  from it, its whole row, its row and column (`cross`) or a burst from it (`burst`). With several colors, each press takes the next one. Stack them with
  `add` blending over a calm background.
- Don't use the `image` effect: it reads a file on your PC, so it can't be shared.

Themes are welcome when the palette's license allows it; add the palette and its license to
[`CREDITS.md`](CREDITS.md) (`tools/make_credits.py`).

## License

[MIT](LICENSE). By contributing a profile you agree to share it under the same license. The
theme palettes belong to their authors and are used under the MIT License; see
[`CREDITS.md`](CREDITS.md).
