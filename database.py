import sqlite3

conn = sqlite3.connect('projectManagement.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
                employee_id INTEGER PRIMARY KEY,
                employee_name TEXT NOT NULL,
                email TEXT NOT NULL,
                admin_flag INTEGER NOT NULL,
                password TEXT NOT NULL
                )''')


cur.execute('''CREATE TABLE IF NOT EXISTS projects (
               project_id INTEGER PRIMARY KEY,
               project_name TEXT NOT NULL,
               project_desc TEXT,
               project_completion INTEGER,
               project_deadline TEXT,
               project_status INTEGER
               )''')

cur.execute('''CREATE TABLE IF NOT EXISTS task (
               project_id INTEGER NOT NULL,
               task_id INTEGER PRIMARY KEY,
               employee_id INTEGER NOT NULL,
               task_name TEXT NOT NULL,
               task_desc TEXT,
               task_completion INTEGER,
               task_deadline TEXT,
               task_status INTEGER
               )''')

cur.execute('''CREATE TABLE IF NOT EXISTS comment (
                comment_id INTEGER PRIMARY KEY,
                task_id INTEGER NOT NULL,
                employee_id INTEGER NOT NULL,
                comment_text TEXT,
                date_time TEXT NOT NULL,
                comment_order INTEGER NOT NULL
                )''')

conn.commit()

conn.close()

def insert_into_project(project_id, project_name, project_desc, project_completion, project_deadline, project_status):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO projects (project_id, project_name, project_desc, project_completion, project_deadline, project_status)
                    VALUES(?,?,?,?,?,?)''', (project_id, project_name, project_desc, project_completion, project_deadline, project_status))
    conn.commit()
    conn.close()

def insert_into_task(project_id, task_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO task (project_id, task_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status)
                VALUES(?,?,?,?,?,?,?,?)''', (project_id, task_id, employee_id, task_name, task_desc, task_completion, task_deadline, task_status))
    conn.commit()
    conn.close()

def insert_into_comment(comment_id, task_id, employee_id, comment_text, date_time, comment_order):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO comment (comment_id, task_id, employee_id, comment_text, date_time, comment_order)
                    VALUES(?,?,?,?,?)''', (comment_id, task_id, employee_id, comment_text, date_time, comment_order))
    conn.commit()
    conn.close()

def insert_into_user(employee_id, employee_name, email, admin_flag, password):
    conn = sqlite3.connect('projectManagement.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO users (employee_id, employee_name, email, admin_flag, password)
                    VALUES(?,?,?,?,?)''', (employee_id, employee_name, email, admin_flag, password))
    conn.commit()
    conn.close()

insert_into_user('01290103','Elliot York','elliotyork@outlook.com',1,'password1')
insert_into_user('1162070','John Smith','john@outlook.com',0,'password2')

insert_into_user('1162071', 'Alice Johnson', 'alice@gmail.com', 0, 'abc123')
insert_into_user('1162072', 'Bob Anderson', 'bob@yahoo.com', 0, 'securepass')
insert_into_user('1162073', 'Emily Brown', 'emily@hotmail.com', 0, 'p@ssw0rd!')
insert_into_user('1162074', 'Michael Davis', 'michael@example.com', 0, 'mysecret')

insert_into_project(1, 'test_project1', 'test_project_1_desc', '10', '20240801', 1)
insert_into_project(2, 'sample_project', 'description_of_sample_project', '5', '20240415', 1)
insert_into_project(3, 'new_website', 'developing_a_new_website', '15', '20241030', 1)
insert_into_project(4, 'data_analysis', 'analyzing_sales_data', '8', '20240720', 1)
insert_into_project(5, 'mobile_app', 'building_a_mobile_application', '12', '20241205', 1)


insert_into_task('1', '1', '1162070', 'test_task_1', 'test_task_1_desc', '80', '20240801', 1)
insert_into_task('1', '2', '1162071', 'sample_task_1', 'sample_task_1_desc', '50', '20240420', 1)
insert_into_task('1', '3', '1162072', 'new_task', 'description_of_new_task', '60', '20241005', 1)
insert_into_task('1', '4', '1162073', 'analyze_data', 'analyze_sales_data', '70', '20240725', 1)
insert_into_task('1', '5', '1162074', 'design_UI', 'design_user_interface', '90', '20241210', 1)
insert_into_task('2', '6', '1162070', 'test_task_2', 'test_task_2_desc', '70', '20240805', 1)
insert_into_task('2', '7', '1162071', 'sample_task_2', 'sample_task_2_desc', '40', '20240425', 1)
insert_into_task('2', '8', '1162072', 'create_backend', 'develop_backend_logic', '80', '20241010', 1)
insert_into_task('2', '9', '1162073', 'generate_reports', 'generate_sales_reports', '65', '20240730', 1)
insert_into_task('2', '10', '1162074', 'implement_features', 'implement_new_features', '85', '20241215', 1)
insert_into_task('3', '11', '1162070', 'test_task_3', 'test_task_3_desc', '75', '20240810', 1)
insert_into_task('3', '12', '1162071', 'sample_task_3', 'sample_task_3_desc', '45', '20240501', 1)
insert_into_task('3', '13', '1162072', 'debug_code', 'debugging_application', '70', '20241015', 1)
insert_into_task('3', '14', '1162073', 'optimize_performance', 'optimize_application_performance', '80', '20240801', 1)
insert_into_task('3', '15', '1162074', 'conduct_tests', 'conduct_system_tests', '90', '20241220', 1)
insert_into_task('4', '16', '1162070', 'test_task_4', 'test_task_4_desc', '65', '20240815', 1)
insert_into_task('4', '17', '1162071', 'sample_task_4', 'sample_task_4_desc', '55', '20240505', 1)
insert_into_task('4', '18', '1162072', 'write_documentation', 'documenting_code', '75', '20241020', 1)
insert_into_task('4', '19', '1162073', 'deploy_application', 'deploying_application', '85', '20240805', 1)
insert_into_task('4', '20', '1162074', 'review_code', 'code_review_process', '95', '20241225', 1)

