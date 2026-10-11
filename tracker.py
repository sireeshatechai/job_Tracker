# tracker.py - entry point: parses commands
import argparse
import sys

import db


def cmd_add(args):
    new_id = db.add_application(args.company, args.role, args.link, args.notes)
    print(f"Added application #{new_id}: {args.role} at {args.company}")
def print_table(rows):
    header = f"{'ID':<4} {'Company':<18} {'Role':<24} {'Status':<10} {'Applied':<10}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{r['id']:<4} {r['company'][:18]:<18} {r['role'][:24]:<24} "
            f"{r['status']:<10} {r['applied_date'] or '':<10}"
        )


def cmd_list(args):
    rows = db.list_applications(args.status)
    if not rows:
        print("No applications found.")
        return
    print_table(rows)

def build_parser():
    parser = argparse.ArgumentParser(description="Job application tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a new application")
    add.add_argument("--company", required=True)
    add.add_argument("--role", required=True)
    add.add_argument("--link")
    add.add_argument("--notes")
    add.set_defaults(func=cmd_add)

    ls = sub.add_parser("list", help="list applications")
    ls.add_argument("--status", choices=db.STATUSES)
    ls.set_defaults(func=cmd_list)

    return parser


def main():
    db.create_table()
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()