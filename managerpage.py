# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfacemanager.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowManager(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QWidget(self.centralwidget)
        self.Header.setObjectName("Header")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.Header)
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.homeWelcomeLabel = QtWidgets.QLabel(self.homeTab)
        self.homeWelcomeLabel.setGeometry(QtCore.QRect(140, 70, 371, 41))
        self.homeWelcomeLabel.setObjectName("homeWelcomeLabel")
        self.overdueProjectsLabel = QtWidgets.QLabel(self.homeTab)
        self.overdueProjectsLabel.setGeometry(QtCore.QRect(150, 140, 331, 51))
        self.overdueProjectsLabel.setObjectName("overdueProjectsLabel")
        self.overdueTasksLabel = QtWidgets.QLabel(self.homeTab)
        self.overdueTasksLabel.setGeometry(QtCore.QRect(150, 290, 331, 51))
        self.overdueTasksLabel.setObjectName("overdueTasksLabel")
        self.approvalProjectLabel = QtWidgets.QLabel(self.homeTab)
        self.approvalProjectLabel.setGeometry(QtCore.QRect(140, 210, 331, 51))
        self.approvalProjectLabel.setObjectName("approvalProjectLabel")
        self.approvalProjectsLabel = QtWidgets.QLabel(self.homeTab)
        self.approvalProjectsLabel.setGeometry(QtCore.QRect(150, 370, 331, 51))
        self.approvalProjectsLabel.setObjectName("approvalProjectsLabel")
        self.tabWidget.addTab(self.homeTab, "")
        self.projectTab = QtWidgets.QWidget()
        self.projectTab.setObjectName("projectTab")
        self.projectList = QtWidgets.QListWidget(self.projectTab)
        self.projectList.setGeometry(QtCore.QRect(20, 100, 141, 351))
        self.projectList.setObjectName("projectList")
        self.projectDetailsTabs = QtWidgets.QTabWidget(self.projectTab)
        self.projectDetailsTabs.setGeometry(QtCore.QRect(200, 9, 551, 471))
        self.projectDetailsTabs.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.projectDetailsTabs.setObjectName("projectDetailsTabs")
        self.projectOverviewTab = QtWidgets.QWidget()
        self.projectOverviewTab.setObjectName("projectOverviewTab")
        self.projectNameLabel1 = QtWidgets.QLabel(self.projectOverviewTab)
        self.projectNameLabel1.setGeometry(QtCore.QRect(60, 10, 281, 51))
        self.projectNameLabel1.setObjectName("projectNameLabel1")
        self.projectDescriptionLabel = QtWidgets.QLabel(self.projectOverviewTab)
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(70, 50, 311, 71))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.projectCompletionLabel = QtWidgets.QLabel(self.projectOverviewTab)
        self.projectCompletionLabel.setGeometry(QtCore.QRect(300, 370, 161, 61))
        self.projectCompletionLabel.setObjectName("projectCompletionLabel")
        self.projectDeadlineLabel = QtWidgets.QLabel(self.projectOverviewTab)
        self.projectDeadlineLabel.setGeometry(QtCore.QRect(60, 380, 181, 41))
        self.projectDeadlineLabel.setObjectName("projectDeadlineLabel")
        self.projectOverviewTaskTable = QtWidgets.QTableWidget(self.projectOverviewTab)
        self.projectOverviewTaskTable.setGeometry(QtCore.QRect(60, 120, 411, 231))
        self.projectOverviewTaskTable.setObjectName("projectOverviewTaskTable")
        self.projectOverviewTaskTable.setColumnCount(4)
        self.projectOverviewTaskTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.projectOverviewTaskTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.projectOverviewTaskTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.projectOverviewTaskTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.projectOverviewTaskTable.setHorizontalHeaderItem(3, item)
        self.projectDetailsTabs.addTab(self.projectOverviewTab, "")
        self.manageProjectTab = QtWidgets.QWidget()
        self.manageProjectTab.setObjectName("manageProjectTab")
        self.manageProjectNameLabel = QtWidgets.QLabel(self.manageProjectTab)
        self.manageProjectNameLabel.setGeometry(QtCore.QRect(120, 40, 241, 41))
        self.manageProjectNameLabel.setObjectName("manageProjectNameLabel")
        self.currentProjectDeadlineHeader = QtWidgets.QLabel(self.manageProjectTab)
        self.currentProjectDeadlineHeader.setGeometry(QtCore.QRect(80, 130, 91, 16))
        self.currentProjectDeadlineHeader.setObjectName("currentProjectDeadlineHeader")
        self.currentProjectDeadlinelabel = QtWidgets.QLabel(self.manageProjectTab)
        self.currentProjectDeadlinelabel.setGeometry(QtCore.QRect(230, 130, 71, 16))
        self.currentProjectDeadlinelabel.setObjectName("currentProjectDeadlinelabel")
        self.currentProjectNewDeadlineHeader = QtWidgets.QLabel(self.manageProjectTab)
        self.currentProjectNewDeadlineHeader.setGeometry(QtCore.QRect(70, 190, 101, 31))
        self.currentProjectNewDeadlineHeader.setObjectName("currentProjectNewDeadlineHeader")
        self.currentProjectNewDeadlineInput = QtWidgets.QDateEdit(self.manageProjectTab)
        self.currentProjectNewDeadlineInput.setGeometry(QtCore.QRect(220, 190, 110, 22))
        self.currentProjectNewDeadlineInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 3, 4), QtCore.QTime(0, 0, 0)))
        self.currentProjectNewDeadlineInput.setObjectName("currentProjectNewDeadlineInput")
        self.currentProjectCloseButton = QtWidgets.QPushButton(self.manageProjectTab)
        self.currentProjectCloseButton.setGeometry(QtCore.QRect(100, 370, 75, 23))
        self.currentProjectCloseButton.setObjectName("currentProjectCloseButton")
        self.currentProjectNewDeadlineButton = QtWidgets.QPushButton(self.manageProjectTab)
        self.currentProjectNewDeadlineButton.setGeometry(QtCore.QRect(180, 260, 75, 23))
        self.currentProjectNewDeadlineButton.setObjectName("currentProjectNewDeadlineButton")
        self.currentProjectReopenButton = QtWidgets.QPushButton(self.manageProjectTab)
        self.currentProjectReopenButton.setGeometry(QtCore.QRect(310, 370, 91, 23))
        self.currentProjectReopenButton.setObjectName("currentProjectReopenButton")
        self.projectDetailsTabs.addTab(self.manageProjectTab, "")
        self.projectHeaderLabel = QtWidgets.QLabel(self.projectTab)
        self.projectHeaderLabel.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.projectHeaderLabel.setObjectName("projectHeaderLabel")
        self.projectTypeLabel = QtWidgets.QLabel(self.projectTab)
        self.projectTypeLabel.setGeometry(QtCore.QRect(20, 10, 121, 21))
        self.projectTypeLabel.setObjectName("projectTypeLabel")
        self.projectTypeInput = QtWidgets.QComboBox(self.projectTab)
        self.projectTypeInput.setGeometry(QtCore.QRect(20, 40, 141, 22))
        self.projectTypeInput.setObjectName("projectTypeInput")
        self.projectTypeInput.addItem("")
        self.projectTypeInput.addItem("")
        self.projectTypeInput.addItem("")
        self.projectTypeInput.addItem("")
        self.tabWidget.addTab(self.projectTab, "")
        self.openTaskTab = QtWidgets.QWidget()
        self.openTaskTab.setObjectName("openTaskTab")
        self.openProjectHeaderLabel = QtWidgets.QLabel(self.openTaskTab)
        self.openProjectHeaderLabel.setGeometry(QtCore.QRect(30, 10, 121, 31))
        self.openProjectHeaderLabel.setObjectName("openProjectHeaderLabel")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.openTaskTab)
        self.tabWidget_2.setGeometry(QtCore.QRect(220, 20, 521, 481))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.openTaskDetailsTab = QtWidgets.QWidget()
        self.openTaskDetailsTab.setObjectName("openTaskDetailsTab")
        self.openTaskTitleLabel1 = QtWidgets.QLabel(self.openTaskDetailsTab)
        self.openTaskTitleLabel1.setGeometry(QtCore.QRect(90, 20, 301, 31))
        self.openTaskTitleLabel1.setObjectName("openTaskTitleLabel1")
        self.taskDescLabel = QtWidgets.QLabel(self.openTaskDetailsTab)
        self.taskDescLabel.setGeometry(QtCore.QRect(70, 70, 401, 61))
        self.taskDescLabel.setObjectName("taskDescLabel")
        self.openTaskDeadline = QtWidgets.QLabel(self.openTaskDetailsTab)
        self.openTaskDeadline.setGeometry(QtCore.QRect(80, 210, 101, 61))
        self.openTaskDeadline.setObjectName("openTaskDeadline")
        self.openTaskCompletionLabel = QtWidgets.QLabel(self.openTaskDetailsTab)
        self.openTaskCompletionLabel.setGeometry(QtCore.QRect(340, 210, 111, 61))
        self.openTaskCompletionLabel.setObjectName("openTaskCompletionLabel")
        self.openTaskCompletionChangeBox = QtWidgets.QLineEdit(self.openTaskDetailsTab)
        self.openTaskCompletionChangeBox.setGeometry(QtCore.QRect(200, 300, 113, 20))
        self.openTaskCompletionChangeBox.setObjectName("openTaskCompletionChangeBox")
        self.openTaskCompletionChangeButton = QtWidgets.QPushButton(self.openTaskDetailsTab)
        self.openTaskCompletionChangeButton.setGeometry(QtCore.QRect(344, 300, 111, 23))
        self.openTaskCompletionChangeButton.setObjectName("openTaskCompletionChangeButton")
        self.openTaskOwnerLabel = QtWidgets.QLabel(self.openTaskDetailsTab)
        self.openTaskOwnerLabel.setGeometry(QtCore.QRect(150, 370, 181, 16))
        self.openTaskOwnerLabel.setObjectName("openTaskOwnerLabel")
        self.chaseUpdateButton = QtWidgets.QPushButton(self.openTaskDetailsTab)
        self.chaseUpdateButton.setGeometry(QtCore.QRect(310, 370, 75, 23))
        self.chaseUpdateButton.setObjectName("chaseUpdateButton")
        self.tabWidget_2.addTab(self.openTaskDetailsTab, "")
        self.openTaskCommentTab = QtWidgets.QWidget()
        self.openTaskCommentTab.setObjectName("openTaskCommentTab")
        self.openTaskTitleLabel2 = QtWidgets.QLabel(self.openTaskCommentTab)
        self.openTaskTitleLabel2.setGeometry(QtCore.QRect(60, 20, 361, 41))
        self.openTaskTitleLabel2.setObjectName("openTaskTitleLabel2")
        self.commentLineEdit = QtWidgets.QLineEdit(self.openTaskCommentTab)
        self.commentLineEdit.setGeometry(QtCore.QRect(30, 370, 251, 41))
        self.commentLineEdit.setObjectName("commentLineEdit")
        self.sendCommentBetton = QtWidgets.QPushButton(self.openTaskCommentTab)
        self.sendCommentBetton.setGeometry(QtCore.QRect(330, 370, 121, 41))
        self.sendCommentBetton.setObjectName("sendCommentBetton")
        self.commentBox = QtWidgets.QTextEdit(self.openTaskCommentTab)
        self.commentBox.setGeometry(QtCore.QRect(30, 90, 451, 261))
        self.commentBox.setReadOnly(True)
        self.commentBox.setObjectName("commentBox")
        self.tabWidget_2.addTab(self.openTaskCommentTab, "")
        self.manageTaskTab = QtWidgets.QWidget()
        self.manageTaskTab.setObjectName("manageTaskTab")
        self.currentTaskHeaderLabel = QtWidgets.QLabel(self.manageTaskTab)
        self.currentTaskHeaderLabel.setGeometry(QtCore.QRect(110, 30, 281, 21))
        self.currentTaskHeaderLabel.setObjectName("currentTaskHeaderLabel")
        self.currentTaskNewDeadlineLabel = QtWidgets.QLabel(self.manageTaskTab)
        self.currentTaskNewDeadlineLabel.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.currentTaskNewDeadlineLabel.setObjectName("currentTaskNewDeadlineLabel")
        self.currentTaskNewDeadlineInput = QtWidgets.QDateEdit(self.manageTaskTab)
        self.currentTaskNewDeadlineInput.setGeometry(QtCore.QRect(210, 90, 110, 22))
        self.currentTaskNewDeadlineInput.setObjectName("currentTaskNewDeadlineInput")
        self.currentTaskNewEmployeeLabel = QtWidgets.QLabel(self.manageTaskTab)
        self.currentTaskNewEmployeeLabel.setGeometry(QtCore.QRect(30, 140, 121, 20))
        self.currentTaskNewEmployeeLabel.setObjectName("currentTaskNewEmployeeLabel")
        self.currentTaskNewEmployeeInput = QtWidgets.QComboBox(self.manageTaskTab)
        self.currentTaskNewEmployeeInput.setGeometry(QtCore.QRect(210, 140, 101, 22))
        self.currentTaskNewEmployeeInput.setObjectName("currentTaskNewEmployeeInput")
        self.currentTaskCloseButton = QtWidgets.QPushButton(self.manageTaskTab)
        self.currentTaskCloseButton.setGeometry(QtCore.QRect(100, 310, 75, 23))
        self.currentTaskCloseButton.setObjectName("currentTaskCloseButton")
        self.manageTaskNewUserButton = QtWidgets.QPushButton(self.manageTaskTab)
        self.manageTaskNewUserButton.setGeometry(QtCore.QRect(360, 140, 111, 23))
        self.manageTaskNewUserButton.setObjectName("manageTaskNewUserButton")
        self.currentTaskReopenButton = QtWidgets.QPushButton(self.manageTaskTab)
        self.currentTaskReopenButton.setGeometry(QtCore.QRect(300, 310, 101, 23))
        self.currentTaskReopenButton.setObjectName("currentTaskReopenButton")
        self.manageTaskDeadlineButton = QtWidgets.QPushButton(self.manageTaskTab)
        self.manageTaskDeadlineButton.setGeometry(QtCore.QRect(350, 90, 111, 23))
        self.manageTaskDeadlineButton.setObjectName("manageTaskDeadlineButton")
        self.tabWidget_2.addTab(self.manageTaskTab, "")
        self.openTaskList = QtWidgets.QListWidget(self.openTaskTab)
        self.openTaskList.setGeometry(QtCore.QRect(30, 270, 141, 181))
        self.openTaskList.setObjectName("openTaskList")
        self.openTaskHeaderLabel = QtWidgets.QLabel(self.openTaskTab)
        self.openTaskHeaderLabel.setGeometry(QtCore.QRect(30, 240, 47, 13))
        self.openTaskHeaderLabel.setObjectName("openTaskHeaderLabel")
        self.selectTaskProjectInput = QtWidgets.QComboBox(self.openTaskTab)
        self.selectTaskProjectInput.setGeometry(QtCore.QRect(20, 50, 141, 22))
        self.selectTaskProjectInput.setObjectName("selectTaskProjectInput")
        self.selectTaskEmployeeInput = QtWidgets.QComboBox(self.openTaskTab)
        self.selectTaskEmployeeInput.setGeometry(QtCore.QRect(20, 120, 131, 22))
        self.selectTaskEmployeeInput.setObjectName("selectTaskEmployeeInput")
        self.selectTaskEmployeeLabel = QtWidgets.QLabel(self.openTaskTab)
        self.selectTaskEmployeeLabel.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.selectTaskEmployeeLabel.setObjectName("selectTaskEmployeeLabel")
        self.selectTaskTypeLabel = QtWidgets.QLabel(self.openTaskTab)
        self.selectTaskTypeLabel.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.selectTaskTypeLabel.setObjectName("selectTaskTypeLabel")
        self.selectTaskTypeInput = QtWidgets.QComboBox(self.openTaskTab)
        self.selectTaskTypeInput.setGeometry(QtCore.QRect(20, 190, 121, 22))
        self.selectTaskTypeInput.setObjectName("selectTaskTypeInput")
        self.selectTaskTypeInput.addItem("")
        self.selectTaskTypeInput.addItem("")
        self.selectTaskTypeInput.addItem("")
        self.selectTaskTypeInput.addItem("")
        self.tabWidget.addTab(self.openTaskTab, "")
        self.manageTab = QtWidgets.QWidget()
        self.manageTab.setObjectName("manageTab")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.manageTab)
        self.tabWidget_3.setGeometry(QtCore.QRect(40, 40, 651, 461))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.createProjectTab = QtWidgets.QWidget()
        self.createProjectTab.setObjectName("createProjectTab")
        self.newProjectNameLabel = QtWidgets.QLabel(self.createProjectTab)
        self.newProjectNameLabel.setGeometry(QtCore.QRect(60, 50, 141, 31))
        self.newProjectNameLabel.setObjectName("newProjectNameLabel")
        self.newProjectDescLabel = QtWidgets.QLabel(self.createProjectTab)
        self.newProjectDescLabel.setGeometry(QtCore.QRect(60, 100, 151, 31))
        self.newProjectDescLabel.setObjectName("newProjectDescLabel")
        self.newProjectDeadlineLabel = QtWidgets.QLabel(self.createProjectTab)
        self.newProjectDeadlineLabel.setGeometry(QtCore.QRect(60, 200, 141, 31))
        self.newProjectDeadlineLabel.setObjectName("newProjectDeadlineLabel")
        self.newProjectNameInput = QtWidgets.QLineEdit(self.createProjectTab)
        self.newProjectNameInput.setGeometry(QtCore.QRect(240, 60, 391, 20))
        self.newProjectNameInput.setObjectName("newProjectNameInput")
        self.newProjectDescInput = QtWidgets.QTextEdit(self.createProjectTab)
        self.newProjectDescInput.setGeometry(QtCore.QRect(240, 110, 391, 71))
        self.newProjectDescInput.setObjectName("newProjectDescInput")
        self.newProjectDeadlineInput = QtWidgets.QDateEdit(self.createProjectTab)
        self.newProjectDeadlineInput.setGeometry(QtCore.QRect(280, 210, 110, 22))
        self.newProjectDeadlineInput.setObjectName("newProjectDeadlineInput")
        self.newProjectSubmitButton = QtWidgets.QPushButton(self.createProjectTab)
        self.newProjectSubmitButton.setGeometry(QtCore.QRect(290, 260, 101, 23))
        self.newProjectSubmitButton.setObjectName("newProjectSubmitButton")
        self.tabWidget_3.addTab(self.createProjectTab, "")
        self.createTaskTab = QtWidgets.QWidget()
        self.createTaskTab.setObjectName("createTaskTab")
        self.newTaskProjectLabel = QtWidgets.QLabel(self.createTaskTab)
        self.newTaskProjectLabel.setGeometry(QtCore.QRect(70, 40, 171, 41))
        self.newTaskProjectLabel.setObjectName("newTaskProjectLabel")
        self.newTaskProjectInput = QtWidgets.QComboBox(self.createTaskTab)
        self.newTaskProjectInput.setGeometry(QtCore.QRect(290, 50, 191, 22))
        self.newTaskProjectInput.setObjectName("newTaskProjectInput")
        self.newTaskEmployeeLabel = QtWidgets.QLabel(self.createTaskTab)
        self.newTaskEmployeeLabel.setGeometry(QtCore.QRect(70, 100, 161, 21))
        self.newTaskEmployeeLabel.setObjectName("newTaskEmployeeLabel")
        self.newTaskEmployeeInput = QtWidgets.QComboBox(self.createTaskTab)
        self.newTaskEmployeeInput.setGeometry(QtCore.QRect(290, 100, 191, 22))
        self.newTaskEmployeeInput.setObjectName("newTaskEmployeeInput")
        self.newTaskNameLabel = QtWidgets.QLabel(self.createTaskTab)
        self.newTaskNameLabel.setGeometry(QtCore.QRect(80, 150, 181, 31))
        self.newTaskNameLabel.setObjectName("newTaskNameLabel")
        self.newTaskNameInput = QtWidgets.QLineEdit(self.createTaskTab)
        self.newTaskNameInput.setGeometry(QtCore.QRect(290, 150, 191, 20))
        self.newTaskNameInput.setObjectName("newTaskNameInput")
        self.newTaskDescLabel = QtWidgets.QLabel(self.createTaskTab)
        self.newTaskDescLabel.setGeometry(QtCore.QRect(70, 200, 181, 31))
        self.newTaskDescLabel.setObjectName("newTaskDescLabel")
        self.newTaskDescInput = QtWidgets.QTextEdit(self.createTaskTab)
        self.newTaskDescInput.setGeometry(QtCore.QRect(290, 190, 291, 51))
        self.newTaskDescInput.setObjectName("newTaskDescInput")
        self.newTaskDeadlineLabel = QtWidgets.QLabel(self.createTaskTab)
        self.newTaskDeadlineLabel.setGeometry(QtCore.QRect(80, 270, 151, 21))
        self.newTaskDeadlineLabel.setObjectName("newTaskDeadlineLabel")
        self.newTaskDeadlineInput = QtWidgets.QDateEdit(self.createTaskTab)
        self.newTaskDeadlineInput.setGeometry(QtCore.QRect(290, 270, 101, 22))
        self.newTaskDeadlineInput.setObjectName("newTaskDeadlineInput")
        self.newTaskSubmitButton = QtWidgets.QPushButton(self.createTaskTab)
        self.newTaskSubmitButton.setGeometry(QtCore.QRect(270, 320, 75, 23))
        self.newTaskSubmitButton.setObjectName("newTaskSubmitButton")
        self.tabWidget_3.addTab(self.createTaskTab, "")
        self.createUserTab = QtWidgets.QWidget()
        self.createUserTab.setObjectName("createUserTab")
        self.newEmployeeIdLabel = QtWidgets.QLabel(self.createUserTab)
        self.newEmployeeIdLabel.setGeometry(QtCore.QRect(50, 90, 91, 21))
        self.newEmployeeIdLabel.setObjectName("newEmployeeIdLabel")
        self.newEmployeeIdInput = QtWidgets.QLineEdit(self.createUserTab)
        self.newEmployeeIdInput.setGeometry(QtCore.QRect(170, 90, 113, 20))
        self.newEmployeeIdInput.setObjectName("newEmployeeIdInput")
        self.newEmployeeNameLabel = QtWidgets.QLabel(self.createUserTab)
        self.newEmployeeNameLabel.setGeometry(QtCore.QRect(336, 90, 71, 20))
        self.newEmployeeNameLabel.setObjectName("newEmployeeNameLabel")
        self.newEmployeeNameInput = QtWidgets.QLineEdit(self.createUserTab)
        self.newEmployeeNameInput.setGeometry(QtCore.QRect(440, 90, 113, 20))
        self.newEmployeeNameInput.setObjectName("newEmployeeNameInput")
        self.newEmployeeEmailLabel = QtWidgets.QLabel(self.createUserTab)
        self.newEmployeeEmailLabel.setGeometry(QtCore.QRect(70, 160, 91, 16))
        self.newEmployeeEmailLabel.setObjectName("newEmployeeEmailLabel")
        self.newEmployeeEmailInput = QtWidgets.QLineEdit(self.createUserTab)
        self.newEmployeeEmailInput.setGeometry(QtCore.QRect(180, 160, 361, 20))
        self.newEmployeeEmailInput.setObjectName("newEmployeeEmailInput")
        self.newEmployeeSubmitButton = QtWidgets.QPushButton(self.createUserTab)
        self.newEmployeeSubmitButton.setGeometry(QtCore.QRect(270, 300, 75, 23))
        self.newEmployeeSubmitButton.setObjectName("newEmployeeSubmitButton")
        self.radioButton = QtWidgets.QRadioButton(self.createUserTab)
        self.radioButton.setGeometry(QtCore.QRect(270, 220, 121, 17))
        self.radioButton.setObjectName("radioButton")
        self.tabWidget_3.addTab(self.createUserTab, "")
        self.manageUsersTab = QtWidgets.QWidget()
        self.manageUsersTab.setObjectName("manageUsersTab")
        self.setPrivilegesLabel = QtWidgets.QLabel(self.manageUsersTab)
        self.setPrivilegesLabel.setGeometry(QtCore.QRect(80, 150, 101, 16))
        self.setPrivilegesLabel.setObjectName("setPrivilegesLabel")
        self.setPrivilegesInput = QtWidgets.QComboBox(self.manageUsersTab)
        self.setPrivilegesInput.setGeometry(QtCore.QRect(250, 150, 91, 22))
        self.setPrivilegesInput.setObjectName("setPrivilegesInput")
        self.setPrivilegesInput.addItem("")
        self.setPrivilegesInput.addItem("")
        self.setPrivilegesButton = QtWidgets.QPushButton(self.manageUsersTab)
        self.setPrivilegesButton.setGeometry(QtCore.QRect(410, 150, 91, 23))
        self.setPrivilegesButton.setObjectName("setPrivilegesButton")
        self.deleteUserButton = QtWidgets.QPushButton(self.manageUsersTab)
        self.deleteUserButton.setGeometry(QtCore.QRect(370, 320, 91, 23))
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.setPrivilegesUserInput = QtWidgets.QComboBox(self.manageUsersTab)
        self.setPrivilegesUserInput.setGeometry(QtCore.QRect(250, 80, 101, 22))
        self.setPrivilegesUserInput.setObjectName("setPrivilegesUserInput")
        self.resetPasswordButton = QtWidgets.QPushButton(self.manageUsersTab)
        self.resetPasswordButton.setGeometry(QtCore.QRect(120, 310, 91, 23))
        self.resetPasswordButton.setObjectName("resetPasswordButton")
        self.tabWidget_3.addTab(self.manageUsersTab, "")
        self.tabWidget.addTab(self.manageTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.changePasswordLabel = QtWidgets.QLabel(self.settingsTab)
        self.changePasswordLabel.setGeometry(QtCore.QRect(80, 100, 111, 16))
        self.changePasswordLabel.setObjectName("changePasswordLabel")
        self.changePasswordInput1 = QtWidgets.QLineEdit(self.settingsTab)
        self.changePasswordInput1.setGeometry(QtCore.QRect(230, 100, 113, 20))
        self.changePasswordInput1.setObjectName("changePasswordInput1")
        self.changePasswordInput2 = QtWidgets.QLineEdit(self.settingsTab)
        self.changePasswordInput2.setGeometry(QtCore.QRect(410, 100, 113, 20))
        self.changePasswordInput2.setObjectName("changePasswordInput2")
        self.changePasswordButton = QtWidgets.QPushButton(self.settingsTab)
        self.changePasswordButton.setGeometry(QtCore.QRect(580, 100, 75, 23))
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.logoutButton = QtWidgets.QPushButton(self.settingsTab)
        self.logoutButton.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.logoutButton.setObjectName("logoutButton")
        self.tabWidget.addTab(self.settingsTab, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.Header)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.projectDetailsTabs.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeWelcomeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.overdueProjectsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.overdueTasksLabel.setText(_translate("MainWindow", "TextLabel"))
        self.approvalProjectLabel.setText(_translate("MainWindow", "TextLabel"))
        self.approvalProjectsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("MainWindow", "Home"))
        self.projectNameLabel1.setText(_translate("MainWindow", "TextLabel"))
        self.projectDescriptionLabel.setText(_translate("MainWindow", "TextLabel"))
        self.projectCompletionLabel.setText(_translate("MainWindow", "TextLabel"))
        self.projectDeadlineLabel.setText(_translate("MainWindow", "TextLabel"))
        item = self.projectOverviewTaskTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Task Name"))
        item = self.projectOverviewTaskTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Task Owner"))
        item = self.projectOverviewTaskTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Task Deadline"))
        item = self.projectOverviewTaskTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Task Completion"))
        self.projectDetailsTabs.setTabText(self.projectDetailsTabs.indexOf(self.projectOverviewTab), _translate("MainWindow", "Project Overview"))
        self.manageProjectNameLabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentProjectDeadlineHeader.setText(_translate("MainWindow", "Current Deadline"))
        self.currentProjectDeadlinelabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentProjectNewDeadlineHeader.setText(_translate("MainWindow", "Set New Deadline"))
        self.currentProjectCloseButton.setText(_translate("MainWindow", "Close Project"))
        self.currentProjectNewDeadlineButton.setText(_translate("MainWindow", "Set Deadline"))
        self.currentProjectReopenButton.setText(_translate("MainWindow", "Reopen Project"))
        self.projectDetailsTabs.setTabText(self.projectDetailsTabs.indexOf(self.manageProjectTab), _translate("MainWindow", "Manage Project"))
        self.projectHeaderLabel.setText(_translate("MainWindow", "Project List"))
        self.projectTypeLabel.setText(_translate("MainWindow", "Select Project Type"))
        self.projectTypeInput.setItemText(0, _translate("MainWindow", "All"))
        self.projectTypeInput.setItemText(1, _translate("MainWindow", "Open"))
        self.projectTypeInput.setItemText(2, _translate("MainWindow", "Outstanding"))
        self.projectTypeInput.setItemText(3, _translate("MainWindow", "Closed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.projectTab), _translate("MainWindow", "Project"))
        self.openProjectHeaderLabel.setText(_translate("MainWindow", "Select Project"))
        self.openTaskTitleLabel1.setText(_translate("MainWindow", "TextLabel"))
        self.taskDescLabel.setText(_translate("MainWindow", "TextLabel"))
        self.openTaskDeadline.setText(_translate("MainWindow", "TextLabel"))
        self.openTaskCompletionLabel.setText(_translate("MainWindow", "TextLabel"))
        self.openTaskCompletionChangeButton.setText(_translate("MainWindow", "Set New Completion"))
        self.openTaskOwnerLabel.setText(_translate("MainWindow", "TextLabel"))
        self.chaseUpdateButton.setText(_translate("MainWindow", "Chase"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.openTaskDetailsTab), _translate("MainWindow", "Task Details"))
        self.openTaskTitleLabel2.setText(_translate("MainWindow", "TextLabel"))
        self.sendCommentBetton.setText(_translate("MainWindow", "Send Comment"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.openTaskCommentTab), _translate("MainWindow", "Comments"))
        self.currentTaskHeaderLabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentTaskNewDeadlineLabel.setText(_translate("MainWindow", "New Deadline"))
        self.currentTaskNewEmployeeLabel.setText(_translate("MainWindow", "New User"))
        self.currentTaskCloseButton.setText(_translate("MainWindow", "Close Task"))
        self.manageTaskNewUserButton.setText(_translate("MainWindow", "Submit Changes"))
        self.currentTaskReopenButton.setText(_translate("MainWindow", "Reopen Project"))
        self.manageTaskDeadlineButton.setText(_translate("MainWindow", "Submit Changes"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.manageTaskTab), _translate("MainWindow", "Manage Task"))
        self.openTaskHeaderLabel.setText(_translate("MainWindow", "Tasks"))
        self.selectTaskEmployeeLabel.setText(_translate("MainWindow", "Select Employee"))
        self.selectTaskTypeLabel.setText(_translate("MainWindow", "Select Task Type"))
        self.selectTaskTypeInput.setItemText(0, _translate("MainWindow", "All"))
        self.selectTaskTypeInput.setItemText(1, _translate("MainWindow", "Open"))
        self.selectTaskTypeInput.setItemText(2, _translate("MainWindow", "Outstanding"))
        self.selectTaskTypeInput.setItemText(3, _translate("MainWindow", "Closed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.openTaskTab), _translate("MainWindow", "Open Tasks"))
        self.newProjectNameLabel.setText(_translate("MainWindow", "Enter New Project Name"))
        self.newProjectDescLabel.setText(_translate("MainWindow", "Enter New Project Description"))
        self.newProjectDeadlineLabel.setText(_translate("MainWindow", "Enter New Project Deadline"))
        self.newProjectSubmitButton.setText(_translate("MainWindow", "Submit Project"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.createProjectTab), _translate("MainWindow", "Create Project"))
        self.newTaskProjectLabel.setText(_translate("MainWindow", "Select Associated Project"))
        self.newTaskEmployeeLabel.setText(_translate("MainWindow", "Assign Team Member"))
        self.newTaskNameLabel.setText(_translate("MainWindow", "Enter Task Name"))
        self.newTaskDescLabel.setText(_translate("MainWindow", "Enter Task Description"))
        self.newTaskDeadlineLabel.setText(_translate("MainWindow", "Enter Task Deadline"))
        self.newTaskSubmitButton.setText(_translate("MainWindow", "Submit Task"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.createTaskTab), _translate("MainWindow", "Create Task"))
        self.newEmployeeIdLabel.setText(_translate("MainWindow", "User ID"))
        self.newEmployeeNameLabel.setText(_translate("MainWindow", "User Name"))
        self.newEmployeeEmailLabel.setText(_translate("MainWindow", "User Email"))
        self.newEmployeeSubmitButton.setText(_translate("MainWindow", "Create"))
        self.radioButton.setText(_translate("MainWindow", "Create Admin"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.createUserTab), _translate("MainWindow", "Create Users"))
        self.setPrivilegesLabel.setText(_translate("MainWindow", "Set Privileges"))
        self.setPrivilegesInput.setItemText(0, _translate("MainWindow", "User"))
        self.setPrivilegesInput.setItemText(1, _translate("MainWindow", "Admin"))
        self.setPrivilegesButton.setText(_translate("MainWindow", "Submit Change"))
        self.deleteUserButton.setText(_translate("MainWindow", "Delete User"))
        self.resetPasswordButton.setText(_translate("MainWindow", "Reset Password"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.manageUsersTab), _translate("MainWindow", "Manage Users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manageTab), _translate("MainWindow", "Create"))
        self.changePasswordLabel.setText(_translate("MainWindow", "Change Password"))
        self.changePasswordButton.setText(_translate("MainWindow", "Set Password"))
        self.logoutButton.setText(_translate("MainWindow", "Log Out"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), _translate("MainWindow", "Settings"))


