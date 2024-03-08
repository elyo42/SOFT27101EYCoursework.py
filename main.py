import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from loginpage import Ui_MainWindowLogin
from memberpage import Ui_MainWindowUser
from managerpage import Ui_MainWindowManager
from button_mappings import (projectBoxSQL, login, projectListSQL, projectOverviewTasksSQL, projectOverviewProjectDetailsSQL,
                             manageProjectsSQL, closeProjectsSQL, reopenProjectsSQL, employeeBoxSQL, taskListSQL, taskDetailsSQL,
                             updateTaskCompletionSQL, updateTaskUserSQL, updateTaskDeadlineSQL, closeTaskSQL, reopenTaskSQL,
                             writeCommentSQL, commentsSQL, newProjectSQL, newTaskSQL, newUserSQL, changeUserPrivilegeSQL
                              ,resetPasswordSQL, deleteUserSQL, homePageManagerSQL, taskOwnerSQL, homePageUserSQL, getUserEmailTaskSQL
                             , getUserEmailProjectSQL)
from classes import Project_Overview_Project, Project_Overview_Tasks
import datetime


class AdminWindow(QMainWindow):
    '''
    this class inherits the manager page UI and handles the functions that the widgets for the admin page rely on.
    '''
    def __init__(self, employee_id):
        super().__init__()
        self.employee_id = employee_id
        self.ui = Ui_MainWindowManager()
        self.ui.setupUi(self)

        self.ui.logoutButton.clicked.connect(self.open_login_page)
        self.ui.projectTypeInput.currentIndexChanged.connect(self.updateProjectList)
        self.initProjectList()
        self.ui.projectList.currentItemChanged.connect(self.populateProjectOverview)
        self.ui.currentProjectNewDeadlineButton.clicked.connect(self.updateProjectDeadline)
        self.ui.currentProjectCloseButton.clicked.connect(self.closeProject)
        self.ui.currentProjectReopenButton.clicked.connect(self.reopenProject)
        self.initProjectsBox()
        self.initEmployeeBox()
        self.ui.selectTaskProjectInput.currentIndexChanged.connect(self.updateTasksList)
        self.ui.selectTaskEmployeeInput.currentIndexChanged.connect(self.updateTasksList)
        self.ui.selectTaskTypeInput.currentIndexChanged.connect(self.updateTasksList)
        self.initTaskList()
        self.ui.openTaskList.currentItemChanged.connect(self.populateTaskDetails)
        self.ui.openTaskList.currentItemChanged.connect(self.populateCommentBox)
        self.ui.openTaskCompletionChangeButton.clicked.connect(self.updateTaskCompletion)
        self.initTaskNewUserBox()
        self.ui.manageTaskNewUserButton.clicked.connect(self.updateTaskUser)
        self.ui.manageTaskDeadlineButton.clicked.connect(self.updateTaskDeadline)
        self.ui.currentTaskCloseButton.clicked.connect(self.closeTask)
        self.ui.currentTaskReopenButton.clicked.connect(self.reopenTask)
        self.ui.sendCommentBetton.clicked.connect(self.writeComment)
        self.ui.sendCommentBetton.clicked.connect(self.refreshCommentBox)
        self.ui.newProjectSubmitButton.clicked.connect(self.createProject)
        self.initNewTaskProjectBox()
        self.initNewTaskEmployeeBox()
        self.ui.newTaskSubmitButton.clicked.connect(self.createTask)
        self.ui.newEmployeeSubmitButton.clicked.connect(self.createEmployee)
        self.initManageEmployeeBox()
        self.ui.setPrivilegesButton.clicked.connect(self.changeUserPrivilege)
        self.ui.resetPasswordButton.clicked.connect(self.resetUserPassword)
        self.ui.deleteUserButton.clicked.connect(self.deleteUser)
        self.ui.changePasswordButton.clicked.connect(self.changeOwnPassword)
        self.setHomeDetails()
        self.ui.chaseUpdateButton.clicked.connect(self.chaseUpdateRequest)











    def initProjectList(self):
        '''
        Initialize the Project List
        :return: project list
        '''
        self.populateProjectList('All')
        self.show()
    def populateProjectList(self, project_type):
        '''
        populate project list based on project type
        :param project_type: selection from project type box
        :return: project list
        '''
        projects = projectListSQL(project_type)
        self.ui.projectList.clear()

        for project in projects:
            self.ui.projectList.addItem(f'{project[1]} | {project[0]}')

    def updateProjectList(self):
        '''
        update project when project type changes
        :return: project list
        '''
        project_type = self.ui.projectTypeInput.currentText()
        self.populateProjectList(project_type)


    def populateProjectOverview(self, selected_project):
        '''
        populate project details when a project list item is selected
        :param selected_project: project list item clicked
        :return: project details
        '''
        if selected_project:
            project_id = int(selected_project.text().split(' | ')[0].strip())

            project_details = projectOverviewProjectDetailsSQL(project_id)
            self.ui.projectNameLabel1.setText(project_details.get_project_name())
            self.ui.projectDescriptionLabel.setText(project_details.get_project_description())
            self.ui.projectDeadlineLabel.setText(project_details.get_project_deadline())
            self.ui.projectCompletionLabel.setText(str(project_details.get_project_completion()))
            self.ui.manageProjectNameLabel.setText(project_details.get_project_name())
            self.ui.currentProjectDeadlinelabel.setText(project_details.get_project_deadline())

            tasks = projectOverviewTasksSQL(project_id)
            self.ui.projectOverviewTaskTable.setRowCount(len(tasks))
            for row, task in enumerate(tasks):
                self.ui.projectOverviewTaskTable.setItem(row, 0, QTableWidgetItem(task.get_task_name()))
                self.ui.projectOverviewTaskTable.setItem(row, 1, QTableWidgetItem(task.get_employee_name()))
                self.ui.projectOverviewTaskTable.setItem(row, 2, QTableWidgetItem(task.get_task_deadline()))
                self.ui.projectOverviewTaskTable.setItem(row, 3, QTableWidgetItem(task.get_task_completion()))

    def updateProjectDeadline(self):
        '''
        Updates the selected project deadline to entered date function for set deadline button
        :return:
        '''
        selected_project = self.ui.projectList.currentItem()
        if selected_project:
            project_id = int(selected_project.text().split(' | ')[0].strip())
            selected_date = self.ui.currentProjectNewDeadlineInput.date().toString('yyyy-MM-dd')
            manageProjectsSQL(project_id, selected_date)
            self.updateProjectList()
            self.ui.projectDeadlineLabel.setText(selected_date)
            self.ui.currentProjectDeadlinelabel.setText(selected_date)


    def closeProject(self):
        '''
        Closes the selected project
        :return:
        '''
        selected_project = self.ui.projectList.currentItem()
        if selected_project:
            project_id = int(selected_project.text().split(' | ')[0].strip())
            closeProjectsSQL(project_id)
            email = getUserEmailProjectSQL(project_id)
            with open('email_template.txt', 'w') as file:
                for i in email:
                    file.write(f'To - {i[0]}\n From - system@ttcorp.com\n Subject - Task Closed\n Body - Hello {i[1]}\n '
                               f'The following task has been closed ({selected_project.text()}). \n\nThank you for you hard work.')
            self.updateProjectList()
            QMessageBox.information(None, None, 'Project Closed')

    def reopenProject(self):
        '''
        Reopens the selected project
        :return:
        '''
        selected_project = self.ui.projectList.currentItem()
        if selected_project:
            project_id = int(selected_project.text().split(' | ')[0].strip())
            reopenProjectsSQL(project_id)
            self.updateProjectList()
            QMessageBox.information(None, None, 'Project Reopened')



    def initProjectsBox(self):
        '''
        Initializes the project combobox with project details
        :return:
        '''
        self.populateProjectsBox()
        self.show()

    def initEmployeeBox(self):
        '''
        Initializes the employee combobox with employee details
        :return:
        '''
        self.populateEmployeeBox()
        self.show()

    def populateProjectsBox(self):
        '''
        Populates the project combobox with project details
        :return:
        '''
        projects = projectBoxSQL()
        self.ui.selectTaskProjectInput.clear()
        self.ui.selectTaskProjectInput.addItem('0 | All')
        for project in projects:
            self.ui.selectTaskProjectInput.addItem(f'{project[1]} | {project[0]}')
        self.ui.selectTaskProjectInput.setCurrentIndex(0)


    def populateEmployeeBox(self):
        '''
        Populates the employee combobox with employee details
        :return:
        '''
        employees = employeeBoxSQL()
        self.ui.selectTaskEmployeeInput.clear()
        self.ui.selectTaskEmployeeInput.addItem('0 | All')
        for employee in employees:
            self.ui.selectTaskEmployeeInput.addItem(f'{employee[1]} | {employee[0]}')
        self.ui.selectTaskEmployeeInput.setCurrentIndex(0)


    def initTaskList(self):
        '''
        Initializes the task list combobox with all tasks
        :return:
        '''
        self.populateTasksList('0','0','All')
        self.show()

    def populateTasksList(self, project_id, employee_id, task_status):
        '''
        populates the task list with the selected criteria from the comboboxes
        :param project_id: id of the project to view tasks for
        :param employee_id: id of the employee to view tasks for
        :param task_status: task type of tasks to view
        :return:
        '''
        tasks = taskListSQL(project_id, employee_id, task_status)
        self.ui.openTaskList.clear()
        for task in tasks:
            self.ui.openTaskList.addItem(f'{task[1]} | {task[0]}')

    def updateTasksList(self):
        '''
        Updates the task list when selection criteria changes
        :return:
        '''
        project_id = self.ui.selectTaskProjectInput.currentText().split(' | ')[0].strip()
        employee_id = self.ui.selectTaskEmployeeInput.currentText().split(' | ')[0].strip()
        task_status = self.ui.selectTaskTypeInput.currentText()
        self.populateTasksList(project_id, employee_id, task_status)

    def populateTaskDetails(self,selected_task):
        '''
        Populates the task details based on the selected task
        :param selected_task: task details selected from task list
        :return:
        '''
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            task_details = taskDetailsSQL(task_id)
            task_owner = taskOwnerSQL(task_id)
            self.ui.openTaskTitleLabel1.setText(task_details.get_task_name())
            self.ui.taskDescLabel.setText(task_details.get_task_desc())
            self.ui.openTaskDeadline.setText(task_details.get_task_deadline())
            self.ui.openTaskCompletionLabel.setText(task_details.get_task_completion())
            self.ui.openTaskTitleLabel2.setText(task_details.get_task_name())
            self.ui.currentTaskHeaderLabel.setText(task_details.get_task_name())
            self.ui.openTaskOwnerLabel.setText(task_owner)

    def updateTaskCompletion(self):
        '''
        Updates the task completion of the selected task to entered value
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            new_completion_text = self.ui.openTaskCompletionChangeBox.text()
            try:
                new_completion = int(new_completion_text)
                if 0 <= new_completion <= 100:
                    updateTaskCompletionSQL(task_id, new_completion)
                    self.ui.openTaskCompletionLabel.setText(new_completion)
                    self.systemComment(task_id, f'Task completion set at {new_completion}')
                    QMessageBox.information(None, None, "Completion Set.")
                else:
                    QMessageBox.information(None, None, "Please enter a valid percent (0-100).")
            except ValueError:
                QMessageBox.information(None, None, "Please enter a valid integer.")

    def chaseUpdateRequest(self):
        '''
        sends email to task owner of selected task to provide an update
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            employee_id = int(self.ui.openTaskOwnerLabel.text().split(' | ')[0].strip())
            email = getUserEmailTaskSQL(employee_id)
            with open('email_template.txt', 'w') as file:
                file.write(f'To - {email[0]}\n From - system@ttcorp.com\n Subject - Update Request\n Body - Hello {email[1]}\n'
                           f'Please provide an update for the following task ({selected_task.text()}).'
                           f' \n\nThank you.')
            QMessageBox.information(None, None, "Request sent.")



    def initTaskNewUserBox(self):
        '''
        initialize select employee box for selected task
        :return:
        '''
        self.populateTaskNewUserBox()
        self.show()

    def populateTaskNewUserBox(self):
        '''
        populate employee box for selected task
        :return:
        '''
        employees = employeeBoxSQL()
        self.ui.currentTaskNewEmployeeInput.clear()
        self.ui.currentTaskNewEmployeeInput.addItem('Select User')
        for employee in employees:
            self.ui.currentTaskNewEmployeeInput.addItem(employee[0])
        self.ui.currentTaskNewEmployeeInput.setCurrentIndex(0)

    def updateTaskDeadline(self):
        '''
        update deadline of selected task to entered date
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            selected_date = self.ui.currentTaskNewDeadlineInput.date().toString('yyyy-MM-dd')
            updateTaskDeadlineSQL(task_id, selected_date)
            self.ui.openTaskDeadline.setText(selected_date)
            self.systemComment(task_id,f'Task Deadline changed to {selected_date}')
            QMessageBox.information(None, None, 'New Deadline Set')

    def updateTaskUser(self):
        '''
        update user of selected task to selected user
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = selected_task.text().split(' | ')[0].strip()
            selected_user = self.ui.currentTaskNewEmployeeInput.currentText()
            employee_id = updateTaskUserSQL(task_id, selected_user)
            email = getUserEmailTaskSQL(employee_id)
            self.updateTasksList()
            self.systemComment(task_id,f'Task Owner changed to {selected_user}')
            with open('email_template.txt', 'w') as file:
                file.write(f'To - {email[0]}\n From - system@ttcorp.com\n Subject - Task Assigned\n Body - Hello {email[1]}'
                           f'The following task has been assigned to you - ({selected_task.text()}). '
                           f'\n\nPlease log in for more details.')
            QMessageBox.information(None, None, 'New User Set')

    def closeTask(self):
        '''
        Closes the selected task
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = selected_task.text().split(' | ')[0].strip()
            closeTaskSQL(task_id)
            employee_id = int(self.ui.openTaskOwnerLabel.text().split(' | ')[0].strip())
            email = getUserEmailTaskSQL(employee_id)
            with open('email_template.txt', 'w') as file:
                file.write(f'To - {email[0]}\n From - system@ttcorp.com\n Subject - Task Closed\n Body - Hello {email[1]}'
                           f'The following task has been closed ({selected_task.text()}). \n\nThank you for you hard work.')
            self.updateTasksList()
            self.systemComment(task_id,f'Task Closed by user {self.employee_id}')
            QMessageBox.information(None, None, 'Task Closed')


    def reopenTask(self):
        '''
        Reopen the selected task
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = selected_task.text().split(' | ')[0].strip()
            reopenTaskSQL(task_id)
            self.updateTasksList()
            self.systemComment(task_id,f'Task Reopened by user {self.employee_id}')
            QMessageBox.information(None,None, 'Task Reopened')

    def writeComment(self):
        '''
        create a comment for the selected task from the entered text
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            employee_id = self.employee_id
            comment_text = self.ui.commentLineEdit.text()
            current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writeCommentSQL(task_id, employee_id, comment_text, current_date_time)

    def refreshCommentBox(self):
        '''
        refresh the comment box to show all comments for selected task
        :return:
        '''
        self.ui.commentLineEdit.clear
        self.populateCommentBox()

    def systemComment(self, task_id, comment_text):
        '''
        create comment for system user
        :param task_id: id of the task the comment is for
        :param comment_text: text of the comment
        :return:
        '''
        employee_id = 0
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writeCommentSQL(task_id, employee_id, comment_text, current_date_time)
        self.refreshCommentBox()




    def populateCommentBox(self):
        '''
        populate the comment box to show all comments for selected task
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            comments = commentsSQL(task_id)
            self.ui.commentBox.clear()
            for comment in comments:
                self.ui.commentBox.append(comment.__str__())

    def createProject(self):
        '''
        create new project using the inputs on the create project tab
        :return:
        '''
        project_name = self.ui.newProjectNameInput.text()
        project_desc = self.ui.newProjectDescInput.toPlainText()
        project_deadline = self.ui.newProjectDeadlineInput.date().toString('yyyy-MM-dd')
        newProjectSQL(project_name, project_desc, project_deadline)
        QMessageBox.information(None, None, 'Project Created')
        self.populateNewTaskProjectBox()
        self.ui.newProjectNameInput.clear()
        self.ui.newProjectDescInput.clear()
        self.populateProjectsBox()
        self.populateNewTaskProjectBox()
        self.updateProjectList()

    def initNewTaskProjectBox(self):
        '''
        initialize project select box for new tasks
        :return:
        '''
        self.populateNewTaskProjectBox()
        self.show()

    def initNewTaskEmployeeBox(self):
        '''
        initialize employee select box for new tasks
        :return:
        '''
        self.populateNewTaskEmployeeBox()
        self.show()

    def populateNewTaskProjectBox(self):
        '''
        populate project select box for new tasks
        :return:
        '''
        projects = projectBoxSQL()
        self.ui.newTaskProjectInput.clear()
        self.ui.newTaskProjectInput.addItem('Select Project')
        for project in projects:
            self.ui.newTaskProjectInput.addItem(f'{project[1]} | {project[0]}')
        self.ui.newTaskProjectInput.setCurrentIndex(0)


    def populateNewTaskEmployeeBox(self):
        '''
        populate employee select box for new tasks
        :return:
        '''
        employees = employeeBoxSQL()
        self.ui.newTaskEmployeeInput.clear()
        self.ui.newTaskEmployeeInput.addItem('Select User')
        for employee in employees:
            self.ui.newTaskEmployeeInput.addItem(f'{employee[1]} | {employee[0]}')
        self.ui.newTaskEmployeeInput.setCurrentIndex(0)

    def createTask(self):
        '''
        create new task from inputs on the create task tab and send email to assigned user
        :return:
        '''
        try:
            project_id = int(self.ui.newTaskProjectInput.currentText().split(' | ')[0].strip())
            employee_id = int(self.ui.newTaskEmployeeInput.currentText().split(' | ')[0].strip())
            task_name = self.ui.newTaskNameInput.text()
            task_desc = self.ui.newTaskDescInput.toPlainText()
            task_deadline = self.ui.newTaskDeadlineInput.date().toString('yyyy-MM-dd')
            if task_name != '' or task_desc != '':
                new_task_id = newTaskSQL(project_id, employee_id, task_name, task_desc, task_deadline)
                QMessageBox.information(None, None, 'Project Created')
                email = getUserEmailTaskSQL(employee_id)
                self.populateNewTaskProjectBox()
                self.ui.newTaskNameInput.clear()
                self.ui.newTaskDescInput.clear()
                self.updateTasksList()
                self.systemComment(new_task_id, f'Task created by user {self.employee_id}')
                with open('email_template.txt', 'w') as file:
                    file.write(
                        f'To - {email[0]}\n From - system@ttcorp.com\n Subject - New Task\n Body - Hello {email[1]}'
                        f'The following task has been assigned to you - ({task_name}). \n\nPlease log in for more details.')

            else:
                QMessageBox.information(None, None, 'Task input invalid')
        except:
            QMessageBox.information(None, None, 'Task input invalid')

    def createEmployee(self):
        '''
        Create a new employee using inputs in the create employee tab and send welcome email to new user
        :return:
        '''
        try:
            employee_id = int(self.ui.newEmployeeIdInput.text())
            user_name = self.ui.newEmployeeNameInput.text()
            user_email = self.ui.newEmployeeEmailInput.text()
            admin_flag = int(self.ui.radioButton.isChecked())
            newUserSQL(employee_id, user_name, user_email, admin_flag)
            QMessageBox.information(None, None, 'New user created')
            with open('email_template.txt', 'w') as file:
                file.write(f'To - {user_email}\n From - system@ttcorp.com\n Subject - Welcome\n Body - Hello {user_name}'
                           f'\nYour profile has been created. Your username and password are set as your employee number'
                           f' {employee_id}. Please log in and change your password.')
            self.populateNewTaskEmployeeBox()
            self.populateEmployeeBox()
            self.populateManageEmployeeBox()
        except:
            QMessageBox.information(None, None, 'Invalid input')


    def initManageEmployeeBox(self):
        '''
        Initialize the employee select box for manage employee tab
        :return:
        '''
        self.populateManageEmployeeBox()
        self.show()

    def populateManageEmployeeBox(self):
        '''
        populate the employee select box for manage employee tab
        :return:
        '''
        employees = employeeBoxSQL()
        self.ui.setPrivilegesUserInput.clear()
        self.ui.setPrivilegesUserInput.addItem('Select User')
        for employee in employees:
            self.ui.setPrivilegesUserInput.addItem(f'{employee[1]} | {employee[0]}')
        self.ui.setPrivilegesUserInput.setCurrentIndex(0)


    def changeUserPrivilege(self):
        '''
        Change the admin flag for selected employee
        :return:
        '''
        employee_id = int(self.ui.setPrivilegesUserInput.currentText().split(' | ')[0].strip())
        new_privilege = self.ui.setPrivilegesInput.currentText()
        if new_privilege == 'User':
            admin_flag = 0
        else:
            admin_flag = 1
        changeUserPrivilegeSQL(employee_id, admin_flag)
        QMessageBox.information(None, None, 'User Privilege changed')

    def resetUserPassword(self):
        '''
        Reset the password to employee_id for selected employee
        :return:
        '''
        employee_id = int(self.ui.setPrivilegesUserInput.currentText().split(' | ')[0].strip())
        resetPasswordSQL(employee_id, employee_id)
        QMessageBox.information(None, None, 'Password has been reset')

    def deleteUser(self):
        '''
        Delete the selected employee
        :return:
        '''
        employee_id = int(self.ui.setPrivilegesUserInput.currentText().split(' | ')[0].strip())
        admin_id = self.employee_id
        deleteUserSQL(employee_id, admin_id)
        QMessageBox.information(None, None, 'User has been deleted. Please reassign tasks.')
        self.populateNewTaskEmployeeBox()
        self.populateEmployeeBox()
        self.populateManageEmployeeBox()

    def setHomeDetails(self):
        '''
        Set the home details of the admin
        :return:
        '''
        employee_id = self.employee_id
        details = homePageManagerSQL(employee_id)
        self.ui.homeWelcomeLabel.setText(f'Welcome {details.get_employee_name()}!')
        self.ui.overdueProjectsLabel.setText(f'There are {details.get_overdue_project_count()} overdue projects.')
        self.ui.overdueTasksLabel.setText(f'There are {details.get_overdue_task_count()} overdue tasks.')
        self.ui.approvalProjectLabel.setText(f'There are {details.get_approval_project_count()} projects waiting for '
                                             f'approval before closure')
        self.ui.approvalProjectsLabel.setText(f'There are {details.get_approval_task_count()} tasks waiting for '
                                              f'approval before closure')

    def changeOwnPassword(self):
        '''
        Change the of the logged-in user to entered field
        :return:
        '''
        check1 = self.ui.changePasswordInput1.text()
        check2 = self.ui.changePasswordInput2.text()
        if check1 == check2 and check1 != '':
            resetPasswordSQL(self.employee_id, check1)
            QMessageBox.information(None, None, 'Password has been changed')
        else:
            QMessageBox.information(None, None, 'Please enter valid password')

    def open_login_page(self):
        '''
        Open the login when user logs out
        :return:
        '''
        self.login_page = LoginWindow()
        self.login_page.show()
        self.close()





class UserWindow(QMainWindow):
    def __init__(self, employee_id):
        super().__init__()
        self.employee_id = employee_id
        self.ui = Ui_MainWindowUser()
        self.ui.setupUi(self)

        self.ui.logoutButton.clicked.connect(self.open_login_page)
        self.ui.projectTypeInput.currentIndexChanged.connect(self.updateProjectList)
        self.initProjectList()
        self.ui.projectList.currentItemChanged.connect(self.populateProjectOverview)
        self.initProjectsBox()
        self.initEmployeeBox()
        self.ui.selectTaskProjectInput.currentIndexChanged.connect(self.updateTasksList)
        self.ui.selectTaskEmployeeInput.currentIndexChanged.connect(self.updateTasksList)
        self.ui.selectTaskTypeInput.currentIndexChanged.connect(self.updateTasksList)
        self.initTaskList()
        self.ui.openTaskList.currentItemChanged.connect(self.populateTaskDetails)
        self.ui.openTaskList.currentItemChanged.connect(self.populateCommentBox)
        self.ui.openTaskCompletionChangeButton.clicked.connect(self.updateTaskCompletion)
        self.ui.sendCommentBetton.clicked.connect(self.writeComment)
        self.ui.sendCommentBetton.clicked.connect(self.refreshCommentBox)
        self.ui.changePasswordButton.clicked.connect(self.changeOwnPassword)
        self.setHomeDetails()

    def initProjectList(self):
        '''
        Initialize the project list
        :return:
        '''
        self.populateProjectList('All')
        self.show()

    def populateProjectList(self, project_type):
        '''
        Populate the project list based on project type
        :param project_type: project type from type combo box
        :return:
        '''
        projects = projectListSQL(project_type)
        self.ui.projectList.clear()

        for project in projects:
            self.ui.projectList.addItem(f'{project[1]} | {project[0]}')

    def updateProjectList(self):
        '''
        Update the project list based on selected project type
        :return:
        '''
        project_type = self.ui.projectTypeInput.currentText()
        self.populateProjectList(project_type)

    def populateProjectOverview(self, selected_project):
        '''
        populate the project details based on selected project from list
        :param selected_project: project selected from the list
        :return:
        '''
        if selected_project:
            project_id = int(selected_project.text().split(' | ')[0].strip())

            project_details = projectOverviewProjectDetailsSQL(project_id)
            self.ui.projectNameLabel1.setText(project_details.get_project_name())
            self.ui.projectDescriptionLabel.setText(project_details.get_project_description())
            self.ui.projectDeadlineLabel.setText(project_details.get_project_deadline())
            self.ui.projectCompletionLabel.setText(str(project_details.get_project_completion()))

            tasks = projectOverviewTasksSQL(project_id)
            self.ui.projectOverviewTaskTable.setRowCount(len(tasks))
            for row, task in enumerate(tasks):
                self.ui.projectOverviewTaskTable.setItem(row, 0, QTableWidgetItem(task.get_task_name()))
                self.ui.projectOverviewTaskTable.setItem(row, 1, QTableWidgetItem(task.get_employee_name()))
                self.ui.projectOverviewTaskTable.setItem(row, 2, QTableWidgetItem(task.get_task_deadline()))
                self.ui.projectOverviewTaskTable.setItem(row, 3, QTableWidgetItem(task.get_task_completion()))

    def initProjectsBox(self):
        '''
        Initializes the project select box for task tab
        :return:
        '''
        self.populateProjectsBox()
        self.show()

    def initEmployeeBox(self):
        '''
        Initializes the employee select box for task tab
        :return:
        '''
        self.populateEmployeeBox()
        self.show()

    def populateProjectsBox(self):
        '''
        Populates the project select box for task tab
        :return:
        '''
        projects = projectBoxSQL()
        self.ui.selectTaskProjectInput.clear()
        self.ui.selectTaskProjectInput.addItem('0 | All')
        for project in projects:
            self.ui.selectTaskProjectInput.addItem(f'{project[1]} | {project[0]}')
        self.ui.selectTaskProjectInput.setCurrentIndex(0)

    def populateEmployeeBox(self):
        '''
        Populates the employee select box for task
        :return:
        '''
        employees = employeeBoxSQL()
        self.ui.selectTaskEmployeeInput.clear()
        self.ui.selectTaskEmployeeInput.addItem('0 | All')
        for employee in employees:
            self.ui.selectTaskEmployeeInput.addItem(f'{employee[1]} | {employee[0]}')
        self.ui.selectTaskEmployeeInput.setCurrentIndex(0)

    def initTaskList(self):
        '''
        Initializes the task list
        :return:
        '''
        self.populateTasksList('0', '0', 'All')
        self.show()

    def populateTasksList(self, project_id, employee_id, task_status):
        '''
        Populates the task list based on selected criteria
        :param project_id: id for selected project
        :param employee_id: id for selected employee
        :param task_status: task type
        :return:
        '''
        tasks = taskListSQL(project_id, employee_id, task_status)
        self.ui.openTaskList.clear()
        for task in tasks:
            self.ui.openTaskList.addItem(f'{task[1]} | {task[0]}')

    def updateTasksList(self):
        '''
        Updates the task list based on selected criteria
        :return:
        '''
        project_id = self.ui.selectTaskProjectInput.currentText().split(' | ')[0].strip()
        employee_id = self.ui.selectTaskEmployeeInput.currentText().split(' | ')[0].strip()
        task_status = self.ui.selectTaskTypeInput.currentText()
        self.populateTasksList(project_id, employee_id, task_status)

    def populateTaskDetails(self, selected_task):
        '''
        Populates the task details based on selected task
        :param selected_task: task selected from task list
        :return:
        '''
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            task_details = taskDetailsSQL(task_id)
            task_owner = taskOwnerSQL(task_id)
            self.ui.openTaskTitleLabel1.setText(task_details.get_task_name())
            self.ui.taskDescLabel.setText(task_details.get_task_desc())
            self.ui.openTaskDeadline.setText(task_details.get_task_deadline())
            self.ui.openTaskCompletionLabel.setText(task_details.get_task_completion())
            self.ui.openTaskTitleLabel2.setText(task_details.get_task_name())
            self.ui.openTaskOwnerLabel.setText(task_owner)


    def updateTaskCompletion(self):
        '''
        Updates the task completion for tasks the user owns
        :return:
        '''
        if int(self.ui.openTaskOwnerLabel.text().split(' | ')[0].strip()) == self.employee_id:
            selected_task = self.ui.openTaskList.currentItem()
            if selected_task:
                task_id = int(selected_task.text().split(' | ')[0].strip())
                new_completion_text = self.ui.openTaskCompletionChangeBox.text()
                try:
                    new_completion = int(new_completion_text)
                    if 0 <= new_completion <= 100:
                        updateTaskCompletionSQL(task_id, new_completion)
                        self.ui.openTaskCompletionLabel.setText(str(new_completion))
                        self.systemComment(task_id, f'Task completion set at {new_completion}')
                        QMessageBox.information(None, None, "Completion Set.")
                    else:
                        QMessageBox.information(None, None, "Please enter a valid percent (0-100).")
                except ValueError:
                    QMessageBox.information(None, None, "Please enter a valid integer.")
        else:
            QMessageBox.information(None, None, "You can't edit this task.")

    def writeComment(self):
        '''
        create a comment for selected task if user owns task
        :return:
        '''
        if int(self.ui.openTaskOwnerLabel.text().split(' | ')[0].strip()) == self.employee_id:
            selected_task = self.ui.openTaskList.currentItem()
            if selected_task:
                task_id = int(selected_task.text().split(' | ')[0].strip())
                employee_id = self.employee_id
                comment_text = self.ui.commentLineEdit.text()
                current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writeCommentSQL(task_id, employee_id, comment_text, current_date_time)
        else:
            QMessageBox.information(None, None, "You can't comment on this task.")

    def refreshCommentBox(self):
        '''
        refresh comment box
        :return:
        '''
        self.ui.commentLineEdit.clear
        self.populateCommentBox()

    def systemComment(self, task_id, comment_text):
        '''
        create system comment
        :param task_id: id for task the comment is for
        :param comment_text: text of the comment
        :return:
        '''
        employee_id = 0
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writeCommentSQL(task_id, employee_id, comment_text, current_date_time)
        self.refreshCommentBox()

    def populateCommentBox(self):
        '''
        populate comment box for selected task
        :return:
        '''
        selected_task = self.ui.openTaskList.currentItem()
        if selected_task:
            task_id = int(selected_task.text().split(' | ')[0].strip())
            comments = commentsSQL(task_id)
            self.ui.commentBox.clear()
            for comment in comments:
                self.ui.commentBox.append(comment.__str__())

    def setHomeDetails(self):
        '''
        set home details for logged-in user
        :return:
        '''
        employee_id = self.employee_id
        details = homePageUserSQL(employee_id)
        self.ui.homeWelcomeLabel.setText(f'Welcome {details.get_employee_name()}!')
        self.ui.projectLabel.setText(f'You are currently assigned to {details.get_project_count()} open projects.')
        self.ui.taskLabel.setText(f'You currently have {details.get_task_count()} open tasks.')
        self.ui.overdueTasksLabel.setText(f'You currently have {details.get_overdue_task_count()} overdue tasks')


    def changeOwnPassword(self):
        '''
        change password for logged-in user
        :return:
        '''
        check1 = self.ui.changePasswordInput1.text()
        check2 = self.ui.changePasswordInput2.text()
        if check1 == check2 and check1 != '':
            resetPasswordSQL(self.employee_id, check1)
            QMessageBox.information(None, None, 'Password has been changed')
        else:
            QMessageBox.information(None, None, 'Please enter valid password')

    def open_login_page(self):
        '''
        open login when user logs out
        :return:
        '''
        self.login_page = LoginWindow()
        self.login_page.show()
        self.close()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        '''
        logs user into correct page based on admin flag or rejects if the user details don't match database
        :return:
        '''
        username = self.ui.loginUsernameInput.text()
        password = self.ui.loginPasswordInput.text()
        user = login(username, password)
        if user is not None:
            if user[2] == 1:
                self.open_admin_page(user[0])
            elif user[2] == 0:
                self.open_user_page(user[0])
        else:
            pass

    def open_user_page(self, employee_id):
        '''
        opens user window
        :param employee_id:
        :return:
        '''
        self.user_page = UserWindow(employee_id)
        self.user_page.show()
        self.close()

    def open_admin_page(self, employee_id):
        '''
        opens admin window
        :param employee_id:
        :return:
        '''
        self.admin_page = AdminWindow(employee_id)
        self.admin_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoginWindow()
    mainWindow.show()
    app.exec_()
