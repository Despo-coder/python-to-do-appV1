from functions import get_todos, write_todos
import time
import PySimpleGUI
import sys

label = PySimpleGUI.Text('Type in a Todo')
input_box = PySimpleGUI.InputText(tooltip='Enter To Do Here', key='todo')
add_button = PySimpleGUI.Button('Add')

window = PySimpleGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]], 
                            font=('Helvetica', 10))
while True:
    event, values = window.read()
    match event:
        case 'Add':
          todos = get_todos()
          new_todo= values['todo'] + '\n'
          todos.append(new_todo) 
          write_todos(todos) 
        case PySimpleGUI.WIN_CLOSED:
          break
# event, values = window.read()  
# print(event)
# print(values) 
window.close()


# while True:
#     user_input = input("Choose 1 to add  2 to show 3 to edit 4 to complete a todo 5 to exit: \n")
#     user_input = user_input.strip()
    

#     match user_input:
#         case '1' : 
#             todo = input("\nEnter a Todo")+'\n'
#             #with open('todos.txt', 'r') as file:
#             todos = get_todos()
#             todos.append(todo)
#             write_todos(todos, 'todos.txt')
            
#         case '2':
#            current_time = time.strftime("%c - %H:%M:%S")
#            print(current_time)
#            todos = get_todos()
#         #    new_todos = []           
#         #    for i in todos:
#         #       new_item=i.strip('\n')
#         #       new_todos.append(new_item)
#            #new_todos = [ item.strip('\n') for item in todos]
#            for index, value in enumerate(todos):
#               value = value.strip('\n')
#               print(f"{index +1}: {value}")
              
#         case '3':
#             todos = get_todos()
#             for index, item in enumerate(todos, start=1):
#                print(f"{index}: {item}")
#             edit_number = int(input('\nWhich Number to edit:  '))
#             edit_number -= 1
#             with open ('todos.txt', 'r') as file:
#                todos=file.readlines()
#             new_item = input("Add edited item\n")
#             todos[edit_number] = new_item +'\n'
#             write_todos(todos, 'todos.txt')
            
#         case '4':
#           try:
#             todos = get_todos()
#             for index, item in enumerate(todos, start=1):
#                print(f"{index}: {item}")
#             complete = int(input("Enter number to mark as complete"))
#             complete -= 1
#             todos = get_todos()
#             value = todos[complete]
#             todos.pop(complete)
#             write_todos(todos, 'todos.txt')
#             print(f"Task {value} was removed successfully!")
#           except:
#            print('Enter Valid Number/Entry')
#            continue
#         case '5':
#           break      