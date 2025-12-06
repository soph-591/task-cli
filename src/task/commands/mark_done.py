from task import db
from task.commands import util

def run(args):
    data = db.read_db("db.json")
    data[args.task_id]["status"] = "done"
    db.write_db(data, "db.json")

def register(subparsers):
     parser = subparsers.add_parser(
         "mark-done", help='Mark a task with "done" status'
     )
     util.add_taskid_args(parser)
     parser.set_defaults(func=run)
