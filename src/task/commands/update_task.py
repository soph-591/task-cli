from task.commands import util

def run(args):
    # logic
    pass

def register(subparsers):
    parser = subparsers.add_parser("update", help="Update a task")
    util.add_taskid_args(parser)
    util.add_description_args(parser)
