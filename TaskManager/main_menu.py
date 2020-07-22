def main_menu_funct():
    while True:
        try:
            print('''
1) Create a new task
2) List all task by date
3) List all user_tasks
4) Modify a task
5) Remove a task
6) Create a new user
7) Load a new user
8) Save
0) Quit\n
''')
            
            selection = int(input("Select an option above: "))
            if selection < 8:
                return selection
        except ValueError:
            pass




    
        
    
