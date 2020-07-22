import re
from read import Read
from users import Users

class Edit:
    def __init__(self, shared, cur_user):
        self.shared = shared
        self.user_tasks = self.shared.user_tasks
        self.save_config = self.shared.save_config
        self.cur_user = cur_user

    def modify_task(self, index):
        while True:
            task = input("Enter task name: ")
            date = input("Enter date to run task (XX-XX-XXXX): ")
            if match := re.search('\d\d-\d\d-\d\d\d\d', date):
                break
            print()
        self.user_tasks[self.cur_user][index-1] = [task,date]


    def modify(self):
        if not self.user_tasks:
            return
        read = Read(self.shared,self.cur_user)
        read.read_all()
        while True:
            try:
                task_input = int(input("\nEnter the task number would you like to modify: "))
                if 1 <= task_input <= len(self.user_tasks):
                    self.modify_task(task_input)
                    break
            except ValueError:
                print("Enter a valid task number")

        print("Task Modified")


    def remove(self):
        if not self.user_tasks:
            return
        read = Read(self.shared,self.cur_user)
        read.read_all()
        while True:
            try:
                task_input = int(input("\nEnter the task number would you like to remove: "))
                if 1 <= task_input <= len(list(self.user_tasks.keys())):
                    self.user_tasks[self.cur_user].pop(task_input-1)
                    break
            except Exception as e:
                print("Enter a valid task number")
                print(e)

        print("Task Removed")





    
        
    
