import re

def append_task(cur_user, user_tasks):
    while True:
        task = input("Enter task name: ")
        date = input("Enter date to run task (XX-XX-XXXX): ")
        if match := re.search('\d\d-\d\d-\d\d\d\d', date):
            break
        print()
    user_tasks[cur_user].append([task,date])


def create(cur_user, user_tasks):
    
    print("\nCreating a new task...")
    append_task(cur_user, user_tasks)







    
        
    
