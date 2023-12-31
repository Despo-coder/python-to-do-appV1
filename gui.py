from functions import get_todos, write_todos
import time
import PySimpleGUI
import sys

label = PySimpleGUI.Text('Type in a Todo')
input_box = PySimpleGUI.InputText(tooltip='Enter To Do Here', key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=get_todos(), key='todos', enable_events=True, size =[45, 10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button('Complete')
exit_button = PySimpleGUI.Button('Exit')


window = PySimpleGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]
                                                    ,[list_box, edit_button, complete_button], [exit_button]], 
                            font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values) 
    match event:
        case 'Add': 
          todos = get_todos()
          new_todo = values['todo'] + '\n'
          todos.append(new_todo) 
          write_todos(todos) 
          window['todos'].update(values=todos)
        case 'Edit': 
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] +'\n'
                existing_todos = get_todos()
                index = existing_todos.index(todo_to_edit)
                existing_todos[index] = new_todo
                write_todos(existing_todos)
                window['todos'].update(values=existing_todos) 
        case 'Complete': 
                todo_to_complete = values['todos'][0]
                existing_todos = get_todos()
                existing_todos.remove(todo_to_complete)
                write_todos(existing_todos)
                window['todos'].update(values=existing_todos) 
                window['todo'].update(value='') 
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
    
        case PySimpleGUI.WIN_CLOSED:
          break
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