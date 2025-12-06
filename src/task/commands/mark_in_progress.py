from task import db
from task.commands import util

def run(args):
    data = db.read_db("db.json")
    if data:
        if args.task_id in data:
            data[args.task_id]["status"] = "in-progress"
            db.write_db(data, "db.json")
        else:
            print("ID {args.task_id} doesn't exist")
    else:
        print("list empty")

def register(subparsers):
    parser = subparsers.add_parser(
        "mark-in-progress", help='Mark a task with "in-progress" status'
    )
    util.add_taskid_args(parser)
    parser.set_defaults(func=run)
