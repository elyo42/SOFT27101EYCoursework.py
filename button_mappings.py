import sqlite3
from PyQt5.QtWidgets import QMessageBox
from classes import Project_Overview_Project, Project_Overview_Tasks
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
            user = 1

            # Redirect to admin page
        else:
            QMessageBox.information(None, "Login", "Login Successful!")
            user = 2
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

def projectBoxSQL(employee_name):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT project_name FROM projects WHERE project_id IN '
                '(SELECT DISTINCT t.project_id FROM task as t INNER JOIN users u on t.employee_id = u.employee_id'
                'where t.employee_name = ?)', (employee_name, ))
    projects = cur.fetchall()
    conn.close()
    return projects



