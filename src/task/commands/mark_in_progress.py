from task.commands import util

def run(args):
    # logic
    pass

def register(subparsers):
    parser = subparsers.add_parser(
        "mark-in-progress", help='Mark a task with "in-progress" status'
    )
    util.add_taskid_args(parser)
