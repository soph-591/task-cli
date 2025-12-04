def run(args):
    # logic
    pass

def register(subparsers):
    # Update a task
    # task-cli update 1 "Go shopping and cook dinner"
    parser = subparsers.add_parser("update", help="Update a task")
    add_taskid_args(update)
    add_description_args(update)
