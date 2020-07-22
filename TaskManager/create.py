import re
from users import Users

class Create:
    def __init__(self, shared, cur_user):
        self.shared = shared
        self.user_tasks = self.shared.user_tasks
        self.save_config = self.shared.save_config
        self.cur_user = cur_user

    def append_task(self):
        while True:
            task = input("Enter task name: ")
            date = input("Enter date to run task (XX-XX-XXXX): ")
            if match := re.search('\d\d-\d\d-\d\d\d\d', date):
                break
            print()
        print("append_tasks before:",self.user_tasks)
        self.user_tasks[self.cur_user].append([task,date])
        print("append_tasks after:",self.user_tasks)

    def create(self):
        print("\nCreating a new task...")
        self.append_task()







    
        
    
