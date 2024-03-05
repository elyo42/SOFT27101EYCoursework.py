class Project_Overview_Project:
    def __init__(self, project_name, project_description, project_deadline, project_completion):
        self.project_name = project_name
        self.project_description = project_description
        self.project_deadline = project_deadline
        self.project_completion = project_completion
    def get_project_name(self):
        return self.project_name
    def get_project_description(self):
        return self.project_description
    def get_project_deadline(self):
        return self.project_deadline
    def get_project_completion(self):
        return self.project_completion


class Project_Overview_Tasks:
    def __init__(self, task_name, employee_name, task_deadline, task_completion):
        self.task_name = task_name
        self.employee_name = employee_name
        self.task_deadline = task_deadline
        self.task_completion = task_completion
    def get_task_name(self):
        return self.task_name
    def get_task_deadline(self):
        return self.task_deadline
    def get_task_completion(self):
        return str(self.task_completion)
    def get_employee_name(self):
        return self.employee_name

class Task_Details:
    def __init__(self, task_name, task_desc, task_deadline, task_completion):
        self.task_name = task_name
        self.task_desc = task_desc
        self.task_deadline = task_deadline
        self.task_completion = task_completion
    def get_task_name(self):
        return self.task_name
    def get_task_desc(self):
        return self.task_desc
    def get_task_completion(self):
        return str(self.task_completion)
    def get_task_deadline(self):
        return self.task_deadline

class Comment:
    def __init__(self, employee_name, comment_text, sent_datetime):
        self.employee_name = employee_name
        self.comment_text = comment_text
        self.sent_datetime = sent_datetime
    def __str__(self):
        return f'[{self.sent_datetime}] | [{self.employee_name}] --- {self.comment_text}'

