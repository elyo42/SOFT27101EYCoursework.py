# uncomment and run if error with database




#
# import sqlite3
# from button_mappings import hash_password
#
# def drop_table(table_name):
#     conn = sqlite3.connect('projectManagement.db')
#     cur = conn.cursor()
#     cur.execute(f'DROP TABLE IF EXISTS {table_name}')
#     conn.commit()
#     conn.close()
#
# drop_table('users')
# drop_table('projects')
# drop_table('task')
# drop_table('comment')
#
# conn = sqlite3.connect('projectManagement.db')
#
# cur = conn.cursor()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS users (
#                 employee_id INTEGER PRIMARY KEY,
#                 employee_name TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 admin_flag INTEGER NOT NULL,
#                 password TEXT NOT NULL
#                 )''')
#
#
# cur.execute('''CREATE TABLE IF NOT EXISTS projects (
#                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                project_name TEXT NOT NULL,
#                project_desc TEXT,
#                project_deadline TEXT,
#                project_status INTEGER
#                )''')
#
# cur.execute('''CREATE TABLE IF NOT EXISTS task (
#                project_id INTEGER NOT NULL,
#                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                employee_id INTEGER NOT NULL,
#                task_name TEXT NOT NULL,
#                task_desc TEXT,
#                task_completion INTEGER,
#                task_deadline TEXT,
#                task_status INTEGER
#                )''')
#
# cur.execute('''CREATE TABLE IF NOT EXISTS comment (
#                 comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 task_id INTEGER NOT NULL,
#                 employee_id INTEGER NOT NULL,
#                 comment_text TEXT,
#                 date_time TEXT NOT NULL
#                 )''')
#
# conn.commit()
#
# conn.close()
#
# def insert_into_project(project_name, project_desc, project_deadline, project_status):
#     conn = sqlite3.connect('projectManagement.db')
#     cur = conn.cursor()
#     cur.execute('''INSERT INTO projects (project_name, project_desc, project_deadline, project_status)
#                     VALUES(?,?,?,?)''', (project_name, project_desc, project_deadline, project_status))
#     conn.commit()
#     conn.close()
#
# def insert_into_task(project_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status):
#     conn = sqlite3.connect('projectManagement.db')
#     cur = conn.cursor()
#     cur.execute('''INSERT INTO task (project_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status)
#                 VALUES(?,?,?,?,?,?,?)''', (project_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status))
#     conn.commit()
#     conn.close()
#
# def insert_into_comment(task_id, employee_id, comment_text, date_time):
#     conn = sqlite3.connect('projectManagement.db')
#     cur = conn.cursor()
#     cur.execute('''INSERT INTO comment (task_id, employee_id, comment_text, date_time)
#                     VALUES(?,?,?,?)''', (task_id, employee_id, comment_text, date_time))
#     conn.commit()
#     conn.close()
#
# def insert_into_user(employee_id, employee_name, email, admin_flag, password):
#     conn = sqlite3.connect('projectManagement.db')
#     cur = conn.cursor()
#     hashed_password = hash_password(password)
#     cur.execute('''INSERT INTO users (employee_id, employee_name, email, admin_flag, password)
#                     VALUES(?,?,?,?,?)''', (employee_id, employee_name, email, admin_flag, hashed_password))
#     conn.commit()
#     conn.close()

# insert_into_user('01290103','Elliot York','elliotyork@outlook.com',1,'password1')
# insert_into_user('0','System','',1,'')
#
# for i in range(1, 6):
#     insert_into_user(i, f'User_{i}', f'user{i}@example.com', 0, f'password{i}')
#
#
# for i in range(1, 6):
#     insert_into_project(f'Project_{i}', f'Description of Project {i}', ('2024-05-0' + str(i)), i%2)
#
#
# for i in range(1, 26):
#     insert_into_task((i%5)+1, (i%5)+1, f'Task {i} for Project {(i%5)+1}', f'Description of Task {i}', (i*4), '2024-04-1' + str(i%5), i%2)
