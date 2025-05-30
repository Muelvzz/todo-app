from functions import get_todos, write_todos
import time

now = time.strftime("%b-%d, %Y %H:%M")
print(f"The day is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.title()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()

            user_action = user_action[5:]
            for index, item in enumerate(todos):
                if user_action in item:

                    new_todo = input("Enter new todo: ")
                    todos[index] = new_todo + '\n'

                    write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        number = int(user_action[9:])
        try:
            todos = get_todos()

            todo_to_remove = todos[number - 1]
            todos.pop(number - 1)

            write_todos(todos)

            message = f"{todo_to_remove.strip('\n')} has been removed"
            print(message)
        except IndexError:
            print("There is no item in that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("unknown input")
