"""shout: print a text file in capitals."""
import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(prog="shout", description="Print a text file in capitals.")
    parser.add_argument("file", help="the text file to read")
    args = parser.parse_args(argv)
    with open(args.file, encoding="utf-8") as stream:
        sys.stdout.write(stream.read().upper())
    return 0


if __name__ == "__main__":
    sys.exit(main())
