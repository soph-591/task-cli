"""
this is the cli
"""

import argparse
from task.commands import add_task, update_task, delete_task, list_tasks, mark_done, mark_in_progress

TASK_COMMANDS = [add_task, update_task, delete_task, list_tasks, mark_done, mark_in_progress]

def build_parser():
    parser = argparse.ArgumentParser(prog="task", description="A simple task management CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for module in TASK_COMMANDS:
        module.register(subparsers)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
