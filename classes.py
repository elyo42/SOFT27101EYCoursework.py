class Project_Overview_Project:
    '''
    A class for storing project details
    '''
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
    '''
    A class for storing task details for a project
    '''
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
    '''
    A class for storing task details for a selected task
    '''
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
    '''
    A class for creating string representations of comments
    '''
    def __init__(self, employee_name, comment_text, sent_datetime):
        self.employee_name = employee_name
        self.comment_text = comment_text
        self.sent_datetime = sent_datetime
    def __str__(self):
        return f'[{self.sent_datetime}] | [{self.employee_name}] --- {self.comment_text}'

class HomePageManager:
    '''
    A class for storing home pages details for an admin
    '''
    def __init__(self, employee_name, overdue_task_count, overdue_project_count, approval_task_count, approval_project_count):
        self.employee_name = employee_name
        self.overdue_task_count = overdue_task_count
        self.overdue_project_count = overdue_project_count
        self.approval_task_count = approval_task_count
        self.approval_project_count = approval_project_count
    def get_employee_name(self):
        return self.employee_name
    def get_overdue_task_count(self):
        return self.overdue_task_count
    def get_overdue_project_count(self):
        return self.overdue_project_count
    def get_approval_task_count(self):
        return self.approval_task_count
    def get_approval_project_count(self):
        return self.approval_project_count

class HomePageUser:
    '''
    A class for storing home pages details for a user
    '''
    def __init__(self, employee_name, task_count, project_count, overdue_task_count):
        self.employee_name = employee_name
        self.task_count = task_count
        self.project_count = project_count
        self.overdue_task_count = overdue_task_count
    def get_employee_name(self):
        return self.employee_name
    def get_task_count(self):
        return self.task_count
    def get_project_count(self):
        return self.project_count
    def get_overdue_task_count(self):
        return self.overdue_task_count


