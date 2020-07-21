def task_exist_for_user(cur_user, user_tasks):
    for name,tasks in user_tasks.items():
        for task in tasks:
            task,date = task
            if name == cur_user:
                return True
    return False


def read_by_date(cur_user, user_tasks):
    if not task_exist_for_user(cur_user, user_tasks):
        return
    
    date_input = input("\nEnter the date (XX-XX-XXXX): ")
    print("\n   TASK    DATE")
    num = 1
    for name,tasks in user_tasks.items():
        for task in tasks:
            task,date = task
            if date == date_input and name == cur_user:
                print("{}| {}    {}".format(str(num),task,date))
                num+=1

def read_all(cur_user, user_tasks):
    print("\n   TASK    DATE")
    num = 1
    for name,tasks in user_tasks.items():
        for task in tasks:
            task,date = task
            if name == cur_user:
                print("{}| {}    {}".format(str(num),task,date))
                num+=1
