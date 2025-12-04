def run(args):
    # logic
    pass

def register(subparsers):
    # Delete a task
    # task-cli delete 1
    parser = subparsers.add_parser("delete", help="Delete a task")
    add_taskid_args(parser, typeof="delete")
