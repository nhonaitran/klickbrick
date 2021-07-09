import pytest
from klickbrick import __main__

def test_parse_args():
    args = __main__.parse_args(['hello', '--name', 'Ai'])
    assert args.hello == 'hello'
    assert args.name == 'Ai'

def test_greet_message():
    assert __main__.greet_message('hello', 'Ai') == 'hello, Ai'
    assert __main__.greet_message('hello', 'World') == 'hello, World'


