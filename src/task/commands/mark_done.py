from task.commands import util

def run(args):
    pass

def register(subparsers):
     parser = subparsers.add_parser(
         "mark-done", help='Mark a task with "done" status'
     )
     util.add_taskid_args(parser)
