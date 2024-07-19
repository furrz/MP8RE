import math


def align(number, to_bytes):
    return math.ceil(number / to_bytes) * to_bytes


def align_file(file, to_bytes):
    file.seek(align(file.tell(), to_bytes))
