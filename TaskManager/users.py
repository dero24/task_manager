class Users:
    def __init__(self, shared):
        self.shared = shared
        self.user_tasks = self.shared.user_tasks
        self.save_config = self.shared.save_config
        print("USERS:",self.user_tasks)


    def add_user(self):
        save_file,serializer,_,w = self.save_config
        while True:
            try:
                input_name = str(input("Please enter your user name: "))
                #  if current user
                for name,tasks in self.user_tasks.items():
                    if input_name == name:
                        print("Loading user data..")
                        print("add_user:",self.user_tasks)
                        return name
                print("Creating new user")
                self.user_tasks[input_name] = []
                serializer.dump(self.user_tasks, open(save_file, w))
                return input_name
            except ValueError as e:
                print(e)
        
                        

    def load_user(self):
        self.save()
        self.read_users()
        while True:
            input_name = input("Which user would you like to load?")
            for name,tasks in self.user_tasks.items():
                if str(input_name) == name:
                    return name
            else:
                print("Please enter a user name from above\n")


    def read_users(self):
        for name,tasks in self.user_tasks.items():
            print(name)


    def save(self):
        save_file,serializer,_,w = self.save_config
        serializer.dump(self.user_tasks, open(save_file, w))


    
        
    
