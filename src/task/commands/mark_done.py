from task.commands import util

def run(args):
    pass

def register(subparsers):
     # task-cli mark-done 1
     parser = subparsers.add_parser(
         "mark-done", help='Mark a task with "done" status'
     )
     util.add_taskid_args(parser)
