import argparse
import importlib
import inspect
from pkgutil import iter_modules

from langtool.lang_pack import lang_pack
from langtool.lang_unpack import lang_unpack
import langtool.encodings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='langtool',
                                     description='Convert Mario Party 5/6/7/8 message files to and from JSON.')

    parser.add_argument('-e', '--encoding', help='Select an encoding to use. Use list-encodings to view all options.', default='mp8_eng')
    subparsers = parser.add_subparsers(help='Sub-command help', dest='command')

    decode_subparser = subparsers.add_parser('decode', help='Decode bin to JSON')
    decode_subparser.add_argument('in_file')
    decode_subparser.add_argument('out_file')

    encode_subparser = subparsers.add_parser('encode', help='Encode JSON to bin')
    encode_subparser.add_argument('in_file')
    encode_subparser.add_argument('out_file')

    list_encodings_subparser = subparsers.add_parser('list-encodings', help='List available encodings.')

    args = parser.parse_args()

    encodings = [m.name for m in iter_modules(langtool.encodings.__path__)]

    if args.encoding not in encodings:
        print("The chosen encoding is invalid. Use list-encodings to view all valid options.")
        exit(1)

    chosen_encoding = importlib.import_module('langtool.encodings.' + args.encoding)

    if args.command is None:
        print("No command was specified. See --help for a list.")
    elif args.command == 'list-encodings':
        print("Available encodings:")
        for enc in encodings:
            print(enc, "\t", importlib.import_module('langtool.encodings.' + enc).__doc__)
    elif args.command == 'decode':
        lang_unpack(args.in_file, args.out_file, chosen_encoding.translation_map)
    elif args.command == 'encode':
        lang_pack(args.in_file, args.out_file, chosen_encoding.translation_map)
