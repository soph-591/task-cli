from task.commands import util

def run(args):
    pass

def register(subparsers):
    parser = subparsers.add_parser("delete", help="Delete a task")
    util.add_taskid_args(parser, typeof="delete")
