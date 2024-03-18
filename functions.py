def get_todos(filepath="Files/todos.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(filepath, todos):
    with open(filepath, 'w') as file:
        file.writelines(todos)

print(__name__)

if __name__=="__main__":
    print("Hello")
    print(get_todos())