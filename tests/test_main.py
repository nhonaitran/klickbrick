import unittest
from klickbrick import __main__

class KlickbrickCLI(unittest.TestCase):
    def test_parse_args(self):
        args = __main__.parse_args(['hello', '--name', 'Ai'])
        self.assertEqual(args.hello, 'hello')
        self.assertEqual(args.name, 'Ai')

    def test_greet_message(self):
        self.assertEqual(__main__.greet_message('hello', 'Ai'), 'hello, Ai')
        self.assertEqual(__main__.greet_message('hello', 'World'), 'hello, World')

if __name__ == '__main__':
    unittest.main()

