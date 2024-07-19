import json
import struct

from alignment import align
from lang_translations import translation_map

sections = []


def detranslate(string):
    string = string.encode("ascii", errors="ignore")
    for (to, original) in translation_map:
        string = string.replace(original, to)
    return string


with open("messdata_eng.json", "r") as f:
    sections = json.load(f)

section_offsets = []
section_encoded_data = b''

for section in sections:

    str_encoded_data = b''
    str_offsets = []
    for string in section:
        # Add the offset to this string to the offsets list
        str_offsets.append(len(str_encoded_data) + len(section) * 4)

        # Add the filler bytes
        str_encoded_data += b'\x00\xFF\x00\xFF'

        # Add the text
        str_encoded_data += detranslate(string) + b'\x00'

        # Pad to the proper length
        str_encoded_data += b'\x00' * (align(len(str_encoded_data), 4) - len(str_encoded_data))

    section_offsets.append(len(section_encoded_data) + len(sections) * 4)

    section_encoded_data += struct.pack('>I', len(section))

    for offset in str_offsets:
        section_encoded_data += struct.pack('>I', offset)

    section_encoded_data += str_encoded_data

    section_encoded_data += b'\x00' * (align(len(section_encoded_data), 4) - len(section_encoded_data))

with open("messdata_eng_out.bin", "wb") as f:
    f.write(struct.pack('>I', len(sections)))
    for offset in section_offsets:
        f.write(struct.pack('>I', offset))
    f.write(section_encoded_data)
