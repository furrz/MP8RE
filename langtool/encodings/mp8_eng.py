"""Mario Party 8 English Encoding Map"""
translation_map = [
    (b'_', b'/'),
    (b'{', b':'),
    (b'\x0E\x0D', b'{ICON_MINUS}'),
    (b'\x0E\x0C', b'{ICON_PLUS}'),
    (b'\x0E\x0F', b'{ICON_DPAD}'),
    (b'\x0E\x05', b'{ICON_DPAD_LEFT_RIGHT}'),
    (b'\x0E\x03', b'{ICON_ARROW_UP}'),
    (b'\x0E\x0B', b'{ICON_2}'),
    (b'\x0E\x0A', b'{ICON_1}'),
    (b'\x0E\x08', b'{ICON_A_BUTTON}'),
    (b'\x0E\x09', b'{ICON_B_BUTTON}'),
    (b'\x0E\x07', b'{ICON_WIIMOTE}'),
    (b'\x1E\x07',  b'{COLOUR_YELLOW}'),
    (b'\x1E\x06',  b'{COLOUR_CYAN}'),
    (b'\x1E\x05',  b'{COLOUR_GREEN}'),
    (b'\x1E\x08', b'{COLOUR_RESET}'),
    (b'\x1C\x02', b'{SFX_01}'),  # Ballyhoo: 'Hi!'
    (b'\x1C\x02', b'{SFX_02}'),  # Ballyhoo: 'Howdy!'
    (b'\x1C\x03', b'{SFX_03}'),  # Ballyhoo: 'Welcome to the Star Carnival!'
    (b'\x1C\x04', b'{SFX_04}'),  # Ballyhoo: 'See ya!'
    (b'\x1C\x05', b'{SFX_05}'),  # Ballyhoo: Nyoo-nyoo (fast, raising tone)
    (b'\x1C\x06', b'{SFX_06}'),  # Ballyhoo: Nyoo-nyoo (slow, lowering tone)
    (b'\x1C\x07', b'{SFX_07}'),  # Ballyhoo: Obla-hee
    (b'\x1C\x08', b'{SFX_08}'),  # Ballyhoo: Alright!
    (b'\x1C\x09', b'{SFX_09}'),  # Hat: Haaa-hahaha! (Raspy laugh)
    (b'\x1C\x0A', b'{SFX_0A}'),  # Ballyhoo: Hah-haa!
    (b'\x1C\x0B', b'{SFX_0B}'),  # Ballyhoo: Haa-haa-haaa!
    (b'\x1C\x0C', b'{SFX_0C}'),  # Ballyhoo: Nooo! / Ohhh!
    (b'\x1C\x0D', b'{SFX_0D}'),  # Ballyhoo: Bada-boom!
    (b'\x1C\x0E', b'{SFX_0E}'),  # Ballyhoo: Goooood luck!
    (b'\x1C\x0F', b'{SFX_0F}'),  # Ballyhoo: Woah!
    (b'\x1C\x10', b'{SFX_10}'),  # Hat: Huh (?)
    (b'\x1C\x11', b'{SFX_11}'),  # Hat: Bye-bye (?)
    (b'\x1C\x12', b'{SFX_12}'),  # Hat: oeeoo (?)
    (b'\x1C\x13', b'{SFX_13}'),  # Hat: ehehaeuu (?)
    (b'\x1C\x14', b'{SFX_14}'),  # Hat: auauseeh (?)
    (b'\x1F\x01', b'{STR_PARAM_1}'),
    (b'\x1F\x02', b'{STR_PARAM_2}'),
    (b'\x1F\x03', b'{STR_PARAM_3}'),
    (b'\x1F\x04', b'{STR_PARAM_4}'),
    (b'\x19\x01', b'{NUM_PARAM_1}'),
    (b'\x91', 'ä'.encode('utf-8')),
    (b'\x93', 'ü'.encode('utf-8')),
    (b'\x9F', 'ñ'.encode('utf-8')),
    (b'\x9A', 'í'.encode('utf-8')),
    (b'\x99', 'ì'.encode('utf-8')),
    (b'?', b'{RIGHT_ARROW}'),
    (b'\x0E', b'{ICON_}'),
    (b'\x1C', b'{SFX_}'),
    (b'\x0F', b'{BTN_START}'),
    (b'\x0D', b'{BTN_START_ALT}'),
    (b'\x1A', b'{BTN_END}'),
    (b'\x10', b' '),
    (b'\x85', b'.'),
    (b'\\', b'\''),
    (b'=', b'-'),
    (b'[', b'['),
    (b'\xC2', b'!'),
    (b'\xC3', b'?'),
    (b'\x82', b','),
    (b'\xFF', b'{WAIT_A_PRESS}'),
    (b'\x1B', b'\t'),
]
