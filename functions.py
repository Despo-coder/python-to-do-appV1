def get_todos(filepath='../todos.txt'):
   with open(filepath,'r') as local_file:
      todos_local=local_file.readlines()
   return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
   with open(filepath,'w') as file:
     file.writelines(todos_arg)
   

if __name__ == "__main__":
   print(get_todos) 