import streamlit as sl
import functions

todos = functions.get_todos()

sl.title("My To-do List")
sl.subheader("Melbin's Personal Today List")
sl.write('You can add, edit, and complete task...')

for task in todos:
    sl.checkbox(task)

sl.text_input(label='', placeholder='Enter task')
