from task import db
from task.commands import util

def print_nicely(k, v):
    print(f"ID: {k}\n\tDescription: {v["description"]}\n\tStatus: {v["status"]}\n\tCreated On: {v["createdAt"]}\n\tLast Updated: {v["updatedAt"]}")

def run(args):
    data = db.read_db("db.json")
    if args.status:
        [print_nicely(k, v) for k, v in data.items() if v["status"] == args.status]
    else:
        print(f"args status is {args.status}")
        [print_nicely(k, v) for k, v in data.items()]

def register(subparsers):
    parser = subparsers.add_parser("list", help="List tasks")
    parser.add_argument(
        "status",
        nargs="?",
        default=None,
        choices=["in-progress", "todo", "done"],
        help="Filter tasks by status",
    )
    ## this is broken
    parser.add_argument(
        "--status", "-s", dest="status", help="Filter tasks by status",
        choices=["in-progress", "todo", "done"]
    )
    parser.set_defaults(func=run)
