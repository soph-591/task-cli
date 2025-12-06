from task import db
from task.commands import util

def run(args):
    data = db.read_db("db.json")
    if data:
        if args.task_id not in data:
            print("its not there")
        else:
            del(data[args.task_id])
            db.write_db(data, "db.json")
    else:
        print("Nothing to delete")

def register(subparsers):
    parser = subparsers.add_parser("delete", help="Delete a task")
    util.add_taskid_args(parser, typeof="delete")
    parser.set_defaults(func=run)
