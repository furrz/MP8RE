# Mario Party 8 RE and Language Tools

The scripts in this repository can be used to convert Mario Party 8's language data ("mess" files) to and from a more
human-readable JSON format.

Note that these scripts assume the US english-release character set is being used, so some adjustments will be needed
for certain accented characters which appear in other language versions to work correctly.

## Usage

To convert message data to JSON:
 - Place the source file in this directory, named `messdata_eng.bin`.
 - Run `lang_unpack.py`.
 - The output JSON will be placed in `messdata_eng.json`.

To convert back to the original binary format:
 - Edit `messdata_eng.json` as desired.
 - Run `lang_pack.py`.
 - The output data will be placed in `messdata_eng_out.bin`.

**Important:** Do not rearrange, add or remove sections or strings from the JSON file.
Mario Party 8 depends on these strings to be in the specific order they appear in.

## Special Characters and Codes

The character set used for Mario Party 8 is non-standard and contains a number of special control
sequences. For convenience, these sequences are converted to `{THESE_SPECIAL_SYMBOLS}`.

Additionally, many strings of dialogue spoken by characters start with a tab character (`\t`).
If you do not include this on each line, their text will overlap with their character portrait.

Here are the symbols and their meanings:

- `{ICON_MINUS}`: Icon of the wiimote minus button.
- `{ICON_DPAD}`: Icon of the wiimote dpad.
- `{ICON_DPAD_LEFT_RIGHT}`: Icon of the wiimote dpad with left and right buttons highlighted in blue.
- `{ICON_ARROW_UP}`: An up arrow.
- `{ICON_2}`: Icon of the wiimote 2 button.
- `{ICON_1}`: Icon of the wiimote 1 button.
- `{ICON_A_BUTTON}`: Icon of the wiimote A button.
- `{ICON_B_BUTTON}`: Icon of the wiimote B button.
- `{ICON_WIIMOTE}`: Icon of the wiimote held at an angle.
- `{COLOUR_YELLOW}`: Sets the text colour to yellow.
- `{COLOUR_CYAN}`: Sets the text colour to cyan.
- `{COLOUR_GREEN}`: Sets the text colour to green.
- `{COLOUR_RESET}`: Sets the text colour back to the default white.
- `{DLG_START_1C05}`: Odd byte sequences sometimes seen at the start of dialogue lines. Unknown purpose.
- `{DLG_START_1C07}`: Odd byte sequences sometimes seen at the start of dialogue lines. Unknown purpose.
- `{DLG_START_1C09}`: Odd byte sequences sometimes seen at the start of dialogue lines. Unknown purpose.
- `{DLG_START_1C0A}`: Odd byte sequences sometimes seen at the start of dialogue lines. Unknown purpose.
- `{STR_PARAM_1}`: A string parameter substituted by the game at runtime.
- `{NUM_PARAM_1}`: A numerical parameter substituted by the game at runtime. If, immediately after this, you include a space and one of these words, it will be dynamically made plural when the number is not 1:
  - `coin` / `Coin`
  - `star` / `Star`
  - `orb` / `Orb`
  - `space` / `Space`
  - `point` / `Point`
  - `stern` / `Stern`
  - `kapsel` / `Kapsel`
  - `punkt` / `Punkt`
  - `feld` / `Feld`
  - `toile` / `Toile`
  - `capsule` / `Capsule`
  - `case` / `Case`
  - `stella` / `Stella`
  - `gettone` / `Gettone`
  - `pallina` / `Pallina`
  - `punto` / `Punto`
  - `spazio` / `Spazio`
  - `moneda` / `Moneda`
  - `casilla` / `Casilla`
  - Other words containing characters unavailable in the English encoding have been excluded from this list.
- `{RIGHT_ARROW}`: A right arrow.
- `{ICON_}`: The icon prefix byte, used when the next byte is not recognized in this list yet as a real icon.
- `{BTN_START}`: Signifies the beginning of the text for an on-screen button. Often appears in pairs, e.g. Yes / No buttons.
- `{BTN_START_ALT}`: An alternative to `{BTN_START}`, for unknown reasons.
- `{BTN_END}`: Signifies the end of the text for an on-screen button.
- `{WAIT_A_PRESS}`: Waits for the A button to be pressed before clearing the dialogue and continuing. Necessary to avoid dismissing dialogue instantly.



