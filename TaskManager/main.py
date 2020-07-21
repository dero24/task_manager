#  Robert DeRosa
#  Python Advanced: Task Manager Modules
#  --Task Manager with Uses--
from main_menu import *
from create_task import *
from edit_task import *
from read import *
from users import *

config = "json"
if config == "json":
    import json as serializer
    w,r = 'wt','rt'
elif config == "pickle":
    import pickle as serializer
    w,r = 'wb','rb'
else:
    raise ImportError

save_file = "usertasks.txt"
user_tasks = serializer.load(open(save_file, r))

save_config = (save_file,serializer,r,w)


def Main():
    cur_user = add_user(user_tasks,save_config)
    while True:
        print(f"\nCurrent User: {cur_user}")
        choice = main_menu(cur_user,user_tasks)

        if choice == 0:
            break
        if choice == 1:
            create(cur_user, user_tasks)
        if choice == 2:
            read_by_date(cur_user, user_tasks)
        if choice == 3:
            read_all(cur_user, user_tasks)
        if choice == 4:
            modify(cur_user, user_tasks)
        if choice == 5:
            remove(cur_user, user_tasks)
        if choice == 6:
            cur_user = add_user(user_tasks, save_config)
        if choice == 7:
            cur_user = load_user(user_tasks, save_config)
        if choice == 8:
            save(save_config)
    
Main()

print("-Program Complete-")





    
        
    
