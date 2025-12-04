def run(args):
    # logic
    pass

def register(subparsers):
    # Mark a task as in progress or done
    # task-cli mark-in-progress 1
    parser = subparsers.add_parser(
        "mark-in-progress", help='Mark a task with "in-progress" status'
    )
    add_taskid_args(parser)
