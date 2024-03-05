import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from loginpage import Ui_MainWindowLogin
from memberpage import Ui_MainWindowUser
from managerpage import Ui_MainWindowManager
from button_mappings import projectBoxSQL, login, projectListSQL, projectOverviewTasksSQL, projectOverviewProjectDetailsSQL, manageProjectsSQL, closeProjectsSQL, reopenProjectsSQL
from classes import Project_Overview_Project, Project_Overview_Tasks


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowManager()
        self.ui.setupUi(self)

        self.ui.logoutButton.clicked.connect(self.open_login_page)
        self.ui.projectTypeInput.currentIndexChanged.connect(self.updateProjectList)
        self.initProjectList()
        self.ui.projectList.currentItemChanged.connect(self.populateProjectOverview)
        self.ui.currentProjectNewDeadlineButton.clicked.connect(self.updateProjectDeadline)
        self.ui.currentProjectCloseButton.clicked.connect(self.closeProject)
        self.ui.currentProjectReopenButton.clicked.connect(self.reopenProject)



    def initProjectList(self):
        self.populateProjectList('All')
        self.show()
    def populateProjectList(self, project_type):
        projects = projectListSQL(project_type)
        self.ui.projectList.clear()

        for project in projects:
            self.ui.projectList.addItem(project[0])
    def updateProjectList(self):
        project_type = self.ui.projectTypeInput.currentText()
        self.populateProjectList(project_type)


    def populateProjectOverview(self, selected_project):
        if selected_project:
            project_name = selected_project.text()

            project_details = projectOverviewProjectDetailsSQL(project_name)
            self.ui.projectNameLabel1.setText(project_details.get_project_name())
            self.ui.projectDescriptionLabel.setText(project_details.get_project_description())
            self.ui.projectDeadlineLabel.setText(project_details.get_project_deadline())
            self.ui.projectCompletionLabel.setText(str(project_details.get_project_completion()))
            self.ui.manageProjectNameLabel.setText(project_details.get_project_name())
            self.ui.currentProjectDeadlinelabel.setText(project_details.get_project_deadline()) ###

            tasks = projectOverviewTasksSQL(project_name)
            self.ui.projectOverviewTaskTable.setRowCount(len(tasks))
            for row, task in enumerate(tasks):
                self.ui.projectOverviewTaskTable.setItem(row, 0, QTableWidgetItem(task.get_task_name()))
                self.ui.projectOverviewTaskTable.setItem(row, 1, QTableWidgetItem(task.get_employee_name()))
                self.ui.projectOverviewTaskTable.setItem(row, 2, QTableWidgetItem(task.get_task_deadline()))
                self.ui.projectOverviewTaskTable.setItem(row, 3, QTableWidgetItem(task.get_task_completion()))

    def updateProjectDeadline(self):
        selected_project = self.ui.projectList.currentItem()
        if selected_project:
            project_name = selected_project.text()
            selected_date = self.ui.currentProjectNewDeadlineInput.date().toString('yyyy-MM-dd')
            manageProjectsSQL(project_name, selected_date)


    def closeProject(self):
        selected_project = self.ui.projectList.currentItem()
        if selected_project:
            project_name = selected_project.text()
            closeProjectsSQL(project_name)

    def reopenProject(self):
        selected_project = self.ui.projectList.currentItem()
        if selected_project:
            project_name = selected_project.text()
            reopenProjectsSQL(project_name)



    def initProjectsBox(self):
        pass

    def populateProjectsBox(self, employee_name):
        emplo
        self.ui.selectTaskProjectInput.addItem('All')


    def open_login_page(self):
        self.login_page = LoginWindow()
        self.login_page.show()
        self.close()

class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowUser()
        self.ui.setupUi(self)

        self.ui.logoutButton.clicked.connect(self.open_login_page)

    def open_login_page(self):
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
        username = self.ui.loginUsernameInput.text()
        password = self.ui.loginPasswordInput.text()
        user = login(username, password)
        if user == 1:
            self.open_admin_page()
        elif user == 2:
            self.open_user_page()
        else:
            pass

    def open_user_page(self):
        self.user_page = UserWindow()
        self.user_page.show()
        self.close()

    def open_admin_page(self):
        self.admin_page = AdminWindow()
        self.admin_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LoginWindow()
    mainWindow.show()
    app.exec_()
