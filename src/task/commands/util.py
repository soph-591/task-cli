def add_taskid_args(subparser, typeof="update"):
    subparser.add_argument(
        "task_id",
        nargs="?",
        help=f"ID of the task to {typeof}",
    )

def add_description_args(subparser):
    subparser.add_argument(
        "description",
        nargs="?",
        help="Task description",
    )
