import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


sl.title("My To-do List")
sl.subheader("Melbin's Personal Today List")
sl.write('You can add, edit, and complete task...')

for index, task in enumerate(todos):
    checkbox = sl.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[task]
        sl.rerun()

sl.text_input(label=' ', placeholder='Enter task',
              on_change=add_todo, key='new_todo')
