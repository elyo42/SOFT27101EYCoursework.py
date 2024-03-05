import sqlite3
from PyQt5.QtWidgets import QMessageBox
from classes import Project_Overview_Project, Project_Overview_Tasks, Task_Details
import datetime

def login(employee_id, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('projectmanagement.db')
    cursor = conn.cursor()

    # Query the database for the provided username and password
    cursor.execute("SELECT employee_id, password, admin_flag FROM users WHERE employee_id=? AND password=?", (employee_id, password))
    user = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Check if a user with the provided credentials exists
    if user:
        if user[2] == 1:  # Check if the user is an admin
            QMessageBox.information(None, "Login", "Login Successful! Welcome Admin!")


            # Redirect to admin page
        else:
            QMessageBox.information(None, "Login", "Login Successful!")

            # Redirect to standard user page
    else:
        QMessageBox.warning(None, "Login", "Invalid Employee ID or Password!")

    return user


def projectListSQL(project_type):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()

    if project_type == 'All':
        cur.execute('SELECT project_name from projects')
    elif project_type == 'Open':
        cur.execute('SELECT project_name from projects WHERE project_status = 1')
    elif project_type == 'Outstanding':
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        cur.execute('SELECT project_name from projects WHERE project_status = 1 and (project_completion = "100" or CAST(project_deadline as DATE) < CAST(? as DATE) )', (current_date,))
    else:
        cur.execute('SELECT project_name from projects WHERE project_status = 2')
    projects = cur.fetchall()
    conn.close()
    return projects

def projectOverviewProjectDetailsSQL(project_name):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT project_name, project_desc, project_deadline, project_completion FROM projects WHERE project_name = ?', (project_name,))
    project_details = cur.fetchone()
    project = Project_Overview_Project(*project_details)
    return project

def projectOverviewTasksSQL(project_name):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT t.task_name, employee_name, t.task_deadline, t.task_completion FROM projects AS p INNER JOIN task as t ON p.project_id = t.project_id '
                'Inner JOIN users AS u on t.employee_id = u.employee_id WHERE p.project_name = ?', (project_name,))
    rows = cur.fetchall()
    tasks = []
    for row in rows:
        task = Project_Overview_Tasks(*row)
        tasks.append(task)
    conn.close()
    return tasks

def manageProjectsSQL(project_name, new_deadline):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE projects SET project_deadline = ? WHERE project_name = ?', (new_deadline, project_name))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Project Deadline Updated.")

def closeProjectsSQL(project_name):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE projects SET project_status = 2 WHERE project_name = ?', (project_name,))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Project Closed.")

def reopenProjectsSQL(project_name):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE projects SET project_status = 1 WHERE project_name = ?', (project_name,))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Project Reopened.")

def projectBoxSQL():
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT project_name FROM projects')
    projects = cur.fetchall()
    conn.close()
    return projects

def employeeBoxSQL():
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT employee_name FROM users')
    employees = cur.fetchall()
    conn.close()
    return employees

def taskListSQL(project_name, employee_name, task_status):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    if project_name == 'All':
        if employee_name == 'All':
            if task_status == 'All':
                cur.execute('SELECT task_name, task_id FROM task')
            elif task_status == 'Open':
                cur.execute('SELECT task_name, task_id FROM task WHERE task_status = 1')
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT task_name, task_id FROM task WHERE task_status = 1 and '
                            '(task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))', (current_date,))
            else:
                cur.execute('SELECT task_name, task_id FROM task WHERE task_status = 2')
        else:
            if task_status == 'All':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE u.employee_name = ?', (employee_name,))
            elif task_status == 'Open':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE t.task_status = 1 AND u.employee_name = ?', (employee_name,))
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE task_status = 1 and (task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))'
                            ' AND u.employee_name = ?', (current_date, employee_name))
            else:
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE task_status = 2 AND u.employee_name = ?', (employee_name,))
    else:
        if employee_name == 'All':
            if task_status == 'All':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE p.project_name = ?', (project_name,))
            elif task_status == 'Open':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE t.task_status = 1 AND p.project_name = ?', (project_name,))
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE task_status = 1 and (task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))'
                            ' AND p.project_name = ?', (current_date, project_name))
            else:
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE task_status = 2 AND p.project_name = ?', (project_name,))
        else:
            if task_status == 'All':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE u.employee_name = ? and p.project_name = ?', (employee_name, project_name))
            elif task_status == 'Open':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE t.task_status = 1 AND u.employee_name = ? '
                            'and p.project_name = ?', (employee_name,project_name))
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE task_status = 1 and (task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))'
                            ' AND u.employee_name = ? and p.project_name = ?', (current_date, employee_name, project_name))
            else:
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE task_status = 2 AND u.employee_name = ? '
                            'and p.project_name = ?', (employee_name,project_name))
    tasks = cur.fetchall()
    conn.close()
    return tasks

def taskDetailsSQL(task_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT task_name, task_desc, task_deadline, task_completion FROM task WHERE task_id = ?', (task_id,))
    task = Task_Details(*cur.fetchone())

    conn.close()
    return task

def updateTaskCompletionSQL(task_id, task_completion):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET task_completion = ? WHERE task_id = ?', (task_completion, task_id))
    conn.commit()
    conn.close()

def updateTaskDeadlineSQL(task_id, new_deadline):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET task_deadline = ? WHERE task_id = ?', (new_deadline, task_id))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Task Deadline Updated.")


def updateTaskUserSQL(task_id, new_user):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT employee_id FROM users WHERE employee_name = ?', (new_user, ))
    employee = int(cur.fetchone()[0])
    cur.execute('UPDATE task SET employee_id = ? WHERE task_id = ?', (employee, task_id))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Task Owner Updated.")


def closeTaskSQL(task_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET task_status = 2 WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Task Closed.")

def reopenTaskSQL(task_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET task_status = 1 WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()
    QMessageBox.information(None, None, "Task Reopened.")