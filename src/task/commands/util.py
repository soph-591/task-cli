 def add_taskid_args(subparser, typeof="update"):
     subparser.add_argument("task-id", nargs=None, help=f"ID of the task to {typeof}")
     subparser.add_argument(
         "--task-id", "-t", dest="task-id", help="ID of the task to {typeof}", required=True
     )
 
 def add_description_args(subparser):
     subparser.add_argument("description", nargs=None, help="Task description")
     subparser.add_argument(
         "--description", "-d", dest="description", help="Task description", required=True
     )
