from task.commands import util

def run(args):
    # logic goes here
    description = args.description
    pass

def register(subparsers):
    # Add a new task
    # task-cli add "Go shopping"
    parser = subparsers.add_parser(
        "add", help='Add a new task. The task will be added with "todo" status'
    )
    util.add_description_args(parser)
    parser.set_defaults(func=run)
