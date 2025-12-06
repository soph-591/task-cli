from datetime import datetime
from task import db
from task.commands import util

def run(args):
    data = db.read_db("db.json")
    data[args.task_id]["description"] = args.description
    data[args.task_id]["updatedAt"] = datetime.isoformat(datetime.now())
    db.write_db(data, "db.json")

def register(subparsers):
    parser = subparsers.add_parser("update", help="Update a task")
    util.add_taskid_args(parser)
    util.add_description_args(parser)
    parser.set_defaults(func=run)
