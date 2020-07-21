def add_user(user_tasks, save_config):
    save_file,serializer,_,w = save_config
    while True:
        try:
            input_name = str(input("Please enter your user name: "))
            #  if current user
            for name,tasks in user_tasks.items():
                if input_name == name:
                    print("Loading user data..")
                    return name
            print("Creating new user")
            user_tasks[input_name] = []
            serializer.dump(user_tasks, open(save_file, w))
            return input_name
        except ValueError as e:
            print(e)
    
                    

def load_user(user_tasks,save_config):
    save(user_tasks,save_config)
    read_users(user_tasks)
    while True:
        input_name = input("Which user would you like to load?")
        for name,tasks in user_tasks.items():
            if str(input_name) == name:
                return name
        else:
            print("Please enter a user name from above\n")


def read_users(user_tasks):
    for name,tasks in user_tasks.items():
        print(name)


def save(user_tasks, save_config):
    save_file,serializer,_,w = save_config
    serializer.dump(user_tasks, open(save_file, w))





    
        
    
