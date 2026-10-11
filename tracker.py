# tracker.py - entry point: parses commands
import argparse
import sys

import db


def cmd_add(args):
    new_id = db.add_application(args.company, args.role, args.link, args.notes)
    print(f"Added application #{new_id}: {args.role} at {args.company}")


def build_parser():
    parser = argparse.ArgumentParser(description="Job application tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a new application")
    add.add_argument("--company", required=True)
    add.add_argument("--role", required=True)
    add.add_argument("--link")
    add.add_argument("--notes")
    add.set_defaults(func=cmd_add)

    return parser


def main():
    db.create_table()
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()