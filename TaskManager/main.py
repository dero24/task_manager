#  Robert DeRosa
#  Python Advanced: Task Manager Classes
#  --Task Manager with Uses--

from shared import Shared
from main_menu import main_menu_funct
from users import Users
from create import Create
from edit import Edit
from read import Read

shared = Shared()
users = Users(shared)



def main():
    cur_user = users.add_user()
    while True:
        create = Create(shared,cur_user)
        edit = Edit(shared,cur_user)
        read = Read(shared,cur_user)
        
        print(f"\nCurrent User: {cur_user}")
        choice = main_menu_funct()

        if choice == 0:
            break
        if choice == 1:
            create.create()
        if choice == 2:
            read.read_by_date()
        if choice == 3:
            read.read_all()
        if choice == 4:
            edit.modify()
        if choice == 5:
            edit.remove()
        if choice == 6:
            cur_user = users.add_user()
        if choice == 7:
            cur_user = users.load_user()
        if choice == 8:
            save()
    
main()

print("-Program Complete-")





    
        
    
