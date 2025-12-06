from task import db, task
from task.commands import util

def run(args):
    data = db.read_db("db.json")
    task_id = db.next_id(data)
    data[task_id] = task.new_task(args.description)
    print(f"Task added successfully (ID: {task_id})")
    db.write_db(data, "db.json")

def register(subparsers):
    parser = subparsers.add_parser(
        "add", help='Add a new task. The task will be added with "todo" status'
    )
    util.add_description_args(parser)
    parser.set_defaults(func=run)
