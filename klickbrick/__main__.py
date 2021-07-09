import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('hello', type=str, help='Greeting command')
    parser.add_argument('--name', default='World', help='The name of person to greet')

    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Hello, {args.name}")


if __name__ == '__main__':
    main()

