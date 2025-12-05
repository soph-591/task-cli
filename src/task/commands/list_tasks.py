from task.commands import util

def run(args):
    pass

def register(subparsers):
    parser = subparsers.add_parser("list", help="List tasks")
    parser.add_argument(
        "status",
        nargs="?",
        default=None,
        choices=["in-progress", "todo", "done"],
        help="Filter tasks by status",
    )
    parser.add_argument(
        "--status", "-s", dest="status", help="Filter tasks by status"
    )
