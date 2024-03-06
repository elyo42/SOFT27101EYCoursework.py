import sqlite3
from PyQt5.QtWidgets import QMessageBox
from classes import Project_Overview_Project, Project_Overview_Tasks, Task_Details, Comment, HomePageManager, HomePageUser
import datetime
import hashlib




def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(employee_id, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('projectmanagement.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    # Query the database for the provided username and password
    cursor.execute("SELECT employee_id, password, admin_flag FROM users WHERE employee_id=? AND password=?", (employee_id, hashed_password))
    user = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Check if a user with the provided credentials exists
    if user is not None and user[0] != 0:

        if user[2] == 1:  # Check if the user is an admin
            QMessageBox.information(None, "Login", "Login Successful! Welcome Admin!")


            # Redirect to admin page
        else:
            QMessageBox.information(None, "Login", "Login Successful!")

            # Redirect to standard user page
    else:
        QMessageBox.warning(None, "Login", "Invalid Employee ID or Password!")
        user = None

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
    cur.execute('SELECT employee_name, employee_id FROM users WHERE not employee_id = 0')
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
    return employee



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
    cur.execute('SELECT task_id from task WHERE project_id = ? and employee_id = ? and task_name = ? and task_desc = ?'
                ' and task_deadline = ?', (project_id, employee_id, task_name, task_desc, task_deadline))
    new_task_id = cur.fetchone()[0]
    conn.close()
    return new_task_id

def newUserSQL(employee_id, employee_name, email, admin_flag):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    hashed_password = hash_password(employee_id)
    cur.execute('''INSERT INTO users (employee_id, employee_name, email, admin_flag, password)
                    VALUES(?,?,?,?,?)''', (employee_id, employee_name, email, admin_flag, hashed_password))
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
    hashed_password = hash_password(password)
    cur.execute('UPDATE users SET password = ? WHERE employee_id = ?', (hashed_password, employee_id))
    conn.commit()
    conn.close()
def deleteUserSQL(employee_id, admin_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('UPDATE task SET employee_id = ? WHERE employee_id = ?', (admin_id, employee_id))
    cur.execute('delete from users where employee_id = ?', (employee_id,))
    conn.commit()
    conn.close()

def homePageManagerSQL(employee_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT employee_name FROM users WHERE employee_id = ?', (employee_id,))
    employee_name = cur.fetchone()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cur.execute('SELECT count(distinct task_id), count(distinct project_id) FROM task WHERE task_status = 1 and '
                'cast(task_deadline as DATE) < cast(? as DATE)', (current_date,))
    overdue = cur.fetchone()
    cur.execute('SELECT count(distinct task_id), count(distinct project_id) FROM task WHERE task_status = 1 and '
                'task_completion = "100"')
    approval_task = cur.fetchone()
    cur.execute('SELECT count(distinct project_id) FROM task WHERE task_status = 1 having avg(task_completion) = "100" ')
    approval_project = cur.fetchone()
    if approval_project is None:
        approval_project = (0,)

    homePageDetails = HomePageManager(employee_name[0], overdue[0], overdue[1], approval_task[0], approval_project[0])
    conn.close()
    return homePageDetails

def taskOwnerSQL(task_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT employee_name, u.employee_id FROM users u INNER JOIN task t on u.employee_id = t.employee_id '
                'WHERE task_id = ?', (task_id,))
    task_user = cur.fetchone()
    conn.close()
    task_owner = f'{task_user[1]} | {task_user[0]}'
    return task_owner

def homePageUserSQL(employee_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT u.employee_name, count(distinct t.task_id), count(distinct project_id) FROM task t INNER JOIN '
                'users u ON u.employee_id = t.employee_id WHERE task_status = 1 and t.employee_id = ?', (employee_id,))
    details1 = cur.fetchone()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    cur.execute('SELECT count(distinct task_id) from task WHERE task_status = 1 and cast(task_deadline as date) < cast(? as date) '
                'and employee_id = ?', (current_date,employee_id))
    overdue = cur.fetchone()
    conn.close()
    home_details = HomePageUser(details1[0],details1[1],details1[2],overdue[0])
    return home_details
def getUserEmailTaskSQL(employee_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT email, employee_name FROM users WHERE employee_id = ?', (employee_id,))
    email = cur.fetchone()
    conn.close()
    return email

def getUserEmailProjectSQL(project_id):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('SELECT email, employee_name FROM users WHERE employee_id IN (SELECT distinct employee_id FROM task '
                'Where project_id = ?)', (project_id,))
    email = cur.fetchall()
    conn.close()
    return email


