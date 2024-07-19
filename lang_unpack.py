import json
import pprint
import struct
import io
from alignment import align_file

from lang_translations import translation_map

sections = []

with open("messdata_eng.bin", "rb") as f:
    (num_sections,) = struct.unpack(">I", f.read(4))

    # skip section offsets
    f.seek(num_sections * 4, io.SEEK_CUR)


    for i in range(num_sections):
        align_file(f, 4)

        (num_strings,) = struct.unpack(">I", f.read(4))

        f.seek(num_strings * 4, io.SEEK_CUR)

        strings = []

        for j in range(num_strings):
            align_file(f, 4)
            f.seek(4, io.SEEK_CUR)  # skip the 00FF00FF
            data = b''

            while True:
                more_data = f.read(1)

                if not more_data:
                    print("Error: ran out of data for string. File may be invalid.")
                    exit(1)

                if more_data[0] == 0:
                    break

                data += more_data

            for (original, to) in translation_map:
                data = data.replace(original, to)

            strings.append(data.decode('ASCII', errors='ignore'))

        sections.append(strings)

    pprint.pp(sections)


with open("messdata_eng.json", "w") as f:
    json.dump(sections, f, indent=4)

