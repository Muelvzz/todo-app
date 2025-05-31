import os

FILEPATH = r"todos.txt"


def get_todos(filepath=FILEPATH):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file_local:
            pass
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        todos = file.writelines(todos_arg)
