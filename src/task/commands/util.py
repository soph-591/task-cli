def add_taskid_args(subparser, typeof="update"):
    """
    TODO: How do I make these mutually exclusive?
    """
    subparser.add_argument(
        "task_id",
        nargs="?",
        help=f"ID of the task to {typeof}",
    )
    subparser.add_argument(
        "--task-id", "-t",
        dest="task_id",
        help=f"ID of the task to {typeof}",
    )

def add_description_args(subparser):
    """
    TODO: How do I make these mutually exclusive?
    """
    subparser.add_argument(
        "description",
        nargs="?",
        help="Task description",
    )
    subparser.add_argument(
        "--description", "-d",
        dest="description",
        help="Task description",
    )
