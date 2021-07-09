###
###
# nhonaitran@NhonAis-Air  ~/src/klickbrick   master ●  poetry run klickbrick -h
# sys.argv: ['klickbrick', '-h']
# usage: klickbrick [-h] [--name NAME] hello
#
# positional arguments:
#  hello        Greeting command
#
# optional arguments:
#  -h, --help   show this help message and exit
#  --name NAME  The name of person to greet
# nhonaitran@NhonAis-Air  ~/src/klickbrick   master ●  poetry run klickbrick hello
# sys.argv: ['klickbrick', 'hello']
# args: Namespace(hello='hello', name='World')
# hello, World
#  nhonaitran@NhonAis-Air  ~/src/klickbrick   master ●  poetry run klickbrick hello --name Ai
# sys.argv: ['klickbrick', 'hello', '--name', 'Ai']
# args: Namespace(hello='hello', name='Ai')
# hello, Ai
#
# sys.argv: List[str] - a list of elements that go after the 'poetry run' command. notice it includes the program/script name
# args: Namespace -  an instance of Namespace whose properties are the positional and optional arguments parsed from sys.argv
###
###

import argparse
import sys

def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument('hello', type=str, help='Greeting command')
    parser.add_argument('--name', type=str, default='World', help='The name of person to greet')

    return parser.parse_args(args)


def greet_message(hello, name):
    return f"{hello}, {name}"

def main():
    args = parse_args(sys.argv[1:])

    if args.hello:
        print(greet_message(args.hello, args.name))


if __name__ == '__main__':
    main()

