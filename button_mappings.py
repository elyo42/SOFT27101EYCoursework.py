import sqlite3
from PyQt5.QtWidgets import QMessageBox
from classes import Project_Overview_Project, Project_Overview_Tasks, Task_Details, Comment
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
        cur.execute('SELECT project_name, project_id from projects')
    elif project_type == 'Open':
        cur.execute('SELECT project_name, project_id from projects WHERE project_status = 1')
    elif project_type == 'Outstanding':
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        cur.execute('SELECT project_name, p.project_id from projects p INNER JOIN task t on p.project_id = t.project_id '
                    'WHERE project_status = 1 GROUP BY 1 HAVING (AVG(task_completion) = 100 or CAST(project_deadline as DATE) < CAST(? as DATE) )', (current_date,))
    else:
        cur.execute('SELECT project_name, project_id from projects WHERE project_status = 2')
    projects = cur.fetchall()
    conn.close()
    return projects

def projectOverviewProjectDetailsSQL(project_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT project_name, project_desc, project_deadline, AVG(task_completion) FROM projects p '
                'INNER JOIN task t on p.project_id = t.project_id WHERE p.project_id = ? GROUP BY 1,2,3', (project_id,))
    project_details = cur.fetchone()
    if project_details is not None:
        project = Project_Overview_Project(*project_details)
    else:
        cur.execute('SELECT project_name, project_desc, project_deadline,0 FROM projects where project_id = ?', (project_id,))
        project = Project_Overview_Project(*cur.fetchone())

    return project

def projectOverviewTasksSQL(project_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT t.task_name, employee_name, t.task_deadline, t.task_completion FROM task as t '
                'Inner JOIN users AS u on t.employee_id = u.employee_id WHERE t.project_id = ?', (project_id,))
    rows = cur.fetchall()
    tasks = []
    for row in rows:
        task = Project_Overview_Tasks(*row)
        tasks.append(task)
    conn.close()
    return tasks

def manageProjectsSQL(project_id, new_deadline):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE projects SET project_deadline = ? WHERE project_id = ?', (new_deadline, project_id))
    conn.commit()
    conn.close()


def closeProjectsSQL(project_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE projects SET project_status = 2 WHERE project_id = ?', (project_id,))
    conn.commit()
    conn.close()


def reopenProjectsSQL(project_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE projects SET project_status = 1 WHERE project_id = ?', (project_id,))
    conn.commit()
    conn.close()


def projectBoxSQL():
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT project_name, project_id FROM projects')
    projects = cur.fetchall()
    conn.close()
    return projects

def employeeBoxSQL():
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT employee_name, employee_id FROM users')
    employees = cur.fetchall()
    conn.close()
    return employees

def taskListSQL(project_id, employee_id, task_status):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    if project_id == '0':
        if employee_id == '0':
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
                            'WHERE u.employee_id = ?', (employee_id,))
            elif task_status == 'Open':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE t.task_status = 1 AND u.employee_id = ?', (employee_id,))
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE task_status = 1 and (task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))'
                            ' AND u.employee_id = ?', (current_date, employee_id))
            else:
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'WHERE task_status = 2 AND u.employee_id = ?', (employee_id,))
    else:
        if employee_id == '0':
            if task_status == 'All':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE p.project_id = ?', (project_id,))
            elif task_status == 'Open':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE t.task_status = 1 AND p.project_id = ?', (project_id,))
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE task_status = 1 and (task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))'
                            ' AND p.project_id = ?', (current_date, project_id))
            else:
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN projects p ON t.project_id = p.project_id '
                            'WHERE task_status = 2 AND p.project_id = ?', (project_id,))
        else:
            if task_status == 'All':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE u.employee_id = ? and p.project_id = ?', (employee_id, project_id))
            elif task_status == 'Open':
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE t.task_status = 1 AND u.employee_id = ? '
                            'and p.project_id = ?', (employee_id,project_id))
            elif task_status == 'Outstanding':
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE task_status = 1 and (task_completion = "100" OR CAST(task_deadline as DATE) < CAST(? as date))'
                            ' AND u.employee_id = ? and p.project_id = ?', (current_date, employee_id, project_id))
            else:
                cur.execute('SELECT t.task_name, t.task_id FROM task t INNER JOIN users u ON t.employee_id = u.employee_id '
                            'INNER JOIN projects p ON t.project_id = p.project_id WHERE task_status = 2 AND u.employee_id = ? '
                            'and p.project_id = ?', (employee_id,project_id))
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



def updateTaskUserSQL(task_id, new_user):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('SELECT employee_id FROM users WHERE employee_name = ?', (new_user, ))
    employee = int(cur.fetchone()[0])
    cur.execute('UPDATE task SET employee_id = ? WHERE task_id = ?', (employee, task_id))
    conn.commit()
    conn.close()



def closeTaskSQL(task_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET task_status = 2 WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()


def reopenTaskSQL(task_id):
    conn = sqlite3.connect('projectmanagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET task_status = 1 WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()


def writeCommentSQL(task_id, employee_id, comment_text, current_date_time):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO comment (task_id, employee_id, comment_text, date_time)
                    VALUES(?,?,?,?)''', (task_id, employee_id, comment_text, current_date_time))
    conn.commit()
    conn.close()

def commentsSQL(task_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT u.employee_name, c.comment_text, c.date_time FROM comment c INNER JOIN '
                ' users u ON c.employee_id = u.employee_id WHERE c.task_id = ? order by cast(c.date_time as DATE) DESC', (task_id,))
    rows = cur.fetchall()
    conn.close()
    comments = []
    for row in rows:
        comments.append(Comment(*row))
    return comments

def newProjectSQL(project_name, project_desc, project_deadline):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO projects (project_name, project_desc, project_deadline, project_status)
                    VALUES(?,?,?,?)''', (project_name, project_desc, project_deadline, 1))
    conn.commit()
    conn.close()

def newTaskSQL(project_id, employee_id, task_name, task_desc, task_deadline):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO task (project_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status)
                VALUES(?,?,?,?,?,?,?)''', (project_id, employee_id, task_name, task_desc, 0, task_deadline, 1))
    conn.commit()
    conn.close()

def newUserSQL(employee_id, employee_name, email, admin_flag):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO users (employee_id, employee_name, email, admin_flag, password)
                    VALUES(?,?,?,?,?)''', (employee_id, employee_name, email, admin_flag, employee_id))
    conn.commit()
    conn.close()

def changeUserPrivilegeSQL(employee_id, admin_flag):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE users SET admin_flag = ? WHERE employee_id = ?', (admin_flag, employee_id))
    conn.commit()
    conn.close()
def resetPasswordSQL(employee_id, password):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE users SET password = ? WHERE employee_id = ?', (password, employee_id))
    conn.commit()
    conn.close()
def deleteUserSQL(employee_id, admin_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET employee_id = ? WHERE employee_id = ?', (admin_id, employee_id))
    cur.execute('delete from users where employee_id = ?', (employee_id,))
    conn.commit()
    conn.close()