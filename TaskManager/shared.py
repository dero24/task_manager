class Shared:
    def __init__(self):
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
        
        self.user_tasks = serializer.load(open(save_file, r))
        self.save_config = (save_file,serializer,r,w)
