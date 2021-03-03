class User:
    def __init__(self, user_id, name, nickname, mail, password, tasks):
        self.name = name
        self.nickname = nickname
        self.mail = mail
        self.password = password
        self.id = user_id
        self.tasks = tasks

    def get_user_data(self):
        return {'user_id': self.id,
                'Name': self.name,
                'Nickname': self.nickname,
                'Email': self.mail,
                'Password': self.password,
                'tasks': self.tasks}

    def get_user_info(self):
        return {'user_id': self.id,
                'Name': self.name,
                'Nickname': self.nickname,
                'Email': self.mail,
                'Password': self.password}

    def get_user_tasks(self):
        return self.tasks

    def set_task(self, task_param):
        task_id = 1
        while True:
            if task_id in self.tasks.keys():
                task_id += 1
            else:
                break

        self.tasks[task_id] = task_param

    def update_task(self, task_num, task_param):
        self.tasks[task_num].update(task_param)

    def delete_task(self, task_num):
        self.tasks.pop(task_num)
