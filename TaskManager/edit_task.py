import re
from read import *

def modify_task(cur_user, index, user_tasks):
    while True:
        task = input("Enter task name: ")
        date = input("Enter date to run task (XX-XX-XXXX): ")
        if match := re.search('\d\d-\d\d-\d\d\d\d', date):
            break
        print()
    user_tasks[cur_user][index-1] = [task,date]


def modify(cur_user, user_tasks):
    if user_tasks:
        read_all(cur_user, user_tasks)
        while True:
            try:
                task_input = int(input("\nEnter the task number would you like to modify: "))
                if 1 <= task_input <= len(user_tasks):
                    modify_task(cur_user,task_input, user_tasks)
                    break
            except ValueError:
                print("Enter a valid task number")

        print("Task Modified")


def remove(cur_user, user_tasks):
    if user_tasks:
        read_all(cur_user, user_tasks)
        while True:
            try:
                task_input = int(input("\nEnter the task number would you like to remove: "))
                if 1 <= task_input <= len(list(user_tasks.keys())):
                    user_tasks[cur_user].pop(task_input-1)
                    break
            except Exception as e:
                print("Enter a valid task number")
                print(e)

        print("Task Removed")





    
        
    
