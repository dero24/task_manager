from users import Users

class Read:
    def __init__(self, shared, cur_user):
        self.shared = shared
        self.user_tasks = self.shared.user_tasks
        self.save_config = self.shared.save_config
        self.cur_user = cur_user

    def task_exist_for_user(self):
        for name,tasks in self.user_tasks.items():
            for task in tasks:
                task,date = task
                if name == self.cur_user:
                    return True
        return False


    def read_by_date(self):
        if not self.task_exist_for_user():
            return
        
        date_input = input("\nEnter the date (XX-XX-XXXX): ")
        print("\n   TASK    DATE")
        num = 1
        for name,tasks in self.user_tasks.items():
            for task in tasks:
                task,date = task
                if date == date_input and name == self.cur_user:
                    print("{}| {}    {}".format(str(num),task,date))
                    num+=1

    def read_all(self):
        print("\n   TASK    DATE")
        num = 1
        for name,tasks in self.user_tasks.items():
            for task in tasks:
                task,date = task
                if name == self.cur_user:
                    print("{}| {}    {}".format(str(num),task,date))
                    num+=1
