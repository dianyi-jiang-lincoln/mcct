###############################
### MCCT                    ###
###############################

# def a function  which can return a SQL
def query_mentor_info():
    return (
        f"SELECT im.last_name, im.first_name, "
        f"im.phone_number, c.name AS company_name, u.email, "
        f"p.title AS project_title, "
        f"p.summary AS project_summary "
        f"FROM users AS u "
        f"LEFT JOIN industry_mentors AS im ON u.id = im.id "
        f"LEFT JOIN companies AS c ON im.company_id = c.id "
        f"LEFT JOIN projects AS p ON p.mentor_id = im.id "
        f"WHERE u.id = %s "
    )

def update_mentor_profile():
    return (
        f"UPDATE `industry_mentors` SET "
        f"`first_name` = %s, "
        f"`last_name` = %s, "
        f"`phone_number` = %s "
        f"WHERE `id` = %s;"
    )

def query_project_lists(project_id=""):
    where_clause = ""
    if project_id != None:
        if len(project_id) != 0:
            where_clause = f"AND p.id = {project_id} "
    return (
        f"SELECT p.id AS `ID`, "
        f"p.title AS `Title`, "
        f"p.summary AS `Summary`, "
        f"COALESCE(GROUP_CONCAT(s.`name`), '') AS Skills "
        f"FROM users AS u "
        f"LEFT JOIN industry_mentors AS im ON u.id = im.id  "
        f"LEFT JOIN companies AS c ON im.company_id = c.id "
        f"LEFT JOIN projects AS p ON p.mentor_id = im.id "
        f"LEFT JOIN project_skills AS ps ON p.id = ps.project_id "
        f"LEFT JOIN skills AS s ON ps.skill_id = s.id "
        f"WHERE im.id = %s "
        f"{where_clause}"
        f"GROUP BY p.id;"
    )

def mentor_query_project_list():
    return(
        f"SELECT  p.id AS project_id, "
        f"c.`name` AS company_name, "
        f"p.title AS project_title, "
        f"p.summary AS project_summary, "
        f"p.number_of_students AS position, "
        f"COUNT(pl.student_id) AS students_enrolled, "
        f"( "
        f" SELECT  "
        f"COALESCE(GROUP_CONCAT(s.`name`), '') AS Skills  "
        f"FROM projects AS p "
        f"LEFT JOIN industry_mentors AS im ON p.mentor_id = im.id  "
        f"LEFT JOIN project_skills AS ps ON p.id = ps.project_id  "
        f"LEFT JOIN skills AS s ON ps.skill_id = s.id  "
        f"WHERE im.id = %s "
        f") AS skills "
        f"FROM projects AS p  "
        f"LEFT JOIN industry_mentors AS im ON p.mentor_id = im.id "
        f"LEFT JOIN placements AS pl ON p.id =pl.project_id "
        f"LEFT JOIN companies AS c ON im.company_id =c.id "
        f"WHERE im.id = %s "
        f"GROUP BY p.id"
    )

def mentor_query_available_students():
    return(
        f"SELECT  "
        f"s.student_id AS `Student ID`, "
        f"concat(s.first_name, ' ', s.last_name) AS `Student name`, "
        f"GROUP_CONCAT(skills.name) AS Skills, "
        f"s.phone_number AS `Phone Number`, "
        f"s.cv_file_path AS CV  "
        f"FROM students AS s "
        f"LEFT JOIN student_skills AS ss ON s.id = ss.student_id "
        f"LEFT JOIN skills ON ss.skill_id = skills.id "
        f"LEFT JOIN placements AS pl ON pl.student_id = s.id "
        f"LEFT JOIN project_student_preferences AS psp ON psp.student_id =s.id "
        f"LEFT JOIN projects AS p ON p.id = psp.project_id "
        f"WHERE  "
        f"s.id NOT IN ( "
        f"SELECT s.id "
        f"FROM students AS s "
        f"LEFT JOIN student_skills AS ss ON s.id = ss.student_id  "
        f"LEFT JOIN skills ON ss.skill_id = skills.id "
        f"LEFT JOIN placements AS pl ON pl.student_id = s.id  "
        f"LEFT JOIN project_student_preferences AS psp ON psp.student_id =s.id "
        f"LEFT JOIN projects AS p ON p.id = psp.project_id "
        f"WHERE  psp.project_id =%s  " 
        f"GROUP BY s.id "
        f") " 
        f"AND s.networking=1 "
        f"GROUP BY s.id "
    )

def update_project_info():
    return f"UPDATE projects " f"SET title = %s, summary = %s " f"WHERE id = %s; "

def query_skills():
    return (
        f"SELECT s.name AS skills "
        f"FROM projects AS p "
        f"LEFT JOIN project_skills AS ps "
        f"ON p.id =ps.project_id "
        f"LEFT JOIN skills AS s "
        f"ON ps.skill_id = s.id "
        f"WHERE p.id = %s; "
    )

def delete_skill():
    return (
        f"DELETE * FROM project_skills "
        f"WHERE project_id = %s AND skill_id = %s "
    )

def query_all_skill_names_in_db():
    return (
        f"SELECT name FROM skills "
    )

def delete_project_skill():
    return (
        f"DELETE ps "
        f"FROM project_skills AS ps "
        f"LEFT JOIN skills AS s "
        f"ON s.id = ps.skill_id "
        f"WHERE ps.project_id = %s AND s.name = %s; "
    )

def insert_skill_for_project():
    return (
        f"INSERT INTO project_skills  (project_skills.project_id,project_skills.skill_id) "
        f"VALUES ( "
        f"%s, "
        f"(SELECT id FROM skills WHERE skills.`name` = %s) "
        f"); "
    )

def query_student_lists():
    return (
        f"SELECT "
        f"concat(students.first_name, ' ', students.last_name) AS `Student name`, "
        f"GROUP_CONCAT(skills.name) AS skills, "
        f"students.phone_number, "
        f"students.cv_file_path "
        f"FROM "
        f"students "
        f"LEFT JOIN "
        f"student_skills ON students.id = student_skills.student_id "
        f"LEFT JOIN "
        f"skills ON student_skills.skill_id = skills.id "
        f"GROUP BY "
        f"students.id; "
    )

def search_students(student_skills="", student_name=""):
    search_by_skills = "skills.name LIKE %s "
    search_by_name = "(students.first_name LIKE %s OR students.last_name LIKE %s)"

    where_clause = ""
    if len(student_skills) == 0 and len(student_name) == 0:
        where_clause = ""
    elif len(student_name) == 0:
        where_clause = f"WHERE {search_by_skills}"
    elif len(student_skills) == 0:
        where_clause = f"WHERE {search_by_name}"
    else:
        where_clause = f"WHERE {search_by_skills} AND {search_by_name}"

    return (
        f"SELECT "
        f"students.student_id AS `Student ID`,"
        f"concat(students.first_name, ' ', students.last_name) AS `Student name`, "
        f"u.email AS `Student Email`, "
        f"GROUP_CONCAT(skills.name) AS Skills,"
        f"students.phone_number AS `Phone Number`,"
        f"students.cv_file_path AS CV "
        f"FROM "
        f"students "
        f"join users u on u.id = students.id "
        f"LEFT JOIN "
        f"student_skills ON students.id = student_skills.student_id "
        f"LEFT JOIN "
        f"skills ON student_skills.skill_id = skills.id "
        f"{where_clause} "
        f"GROUP BY students.id; "
    )

def view_student_profile():
    return (
        f"SELECT "
        f" * "
        f"FROM "
        f"students "
        f"WHERE "
        f"students.student_id = %s; "
    )

def check_mentor_prefered_projects_numbers():
    return (
        f"SELECT count(*) AS total_prefered_project  "
        f"FROM project_student_preferences AS psp "
        f"LEFT JOIN projects AS p ON p.id = psp.project_id "
        f"LEFT JOIN industry_mentors AS im ON im.id = p.mentor_id "
        f"WHERE im.id = %s "
    )

def query_student_id():
    return (
        f"SELECT id "
        f"FROM students "
        f"WHERE student_id = %s"
    )

def add_prefered_student():
    return (
        f"INSERT INTO project_student_preferences "
        f"(project_id, student_id) "
        f"VALUES (%s, %s); "
    )

def query_prefered_students():
    return (
        f"SELECT * "
        F"FROM project_student_preferences "
    )

def query_project_preferred_students():
    return (
        f"SELECT  s.student_id AS `Student ID`,  "
        f"concat(s.first_name, ' ', s.last_name) AS `Student name`, "
        f"CASE "
        f"WHEN sk.name is null THEN \"No skills \" " 
        f"ELSE CONCAT(\"\", GROUP_CONCAT(sk.name SEPARATOR ','), \"\") "
        f"END AS Skills, "
        f"s.phone_number AS `Phone Number`,  "
        f"psp.preference, "
        f"s.cv_file_path AS CV  "
        f"FROM students AS s "
        f"LEFT JOIN student_skills AS ss ON s.id =ss.student_id "
        f"LEFT JOIN skills AS sk ON sk.id = ss.skill_id "
        f"LEFT JOIN project_student_preferences AS psp ON psp.student_id =s.id "
        f"WHERE psp.project_id = %s "
        f"GROUP BY s.id "
        f"ORDER BY psp.preference_rank DESC"
    ) 

def delete_project_preferred_student():
    return (
        f"DELETE psp "
        f"FROM project_student_preferences  AS psp "
        f"LEFT JOIN students AS s ON s.id = psp.student_id "
        f"WHERE psp.project_id = %s AND s.student_id= %s "
    )

def set_prefered_student_rank():
    return (
        f"UPDATE project_student_preferences  AS psp  "
        f"LEFT JOIN students AS s ON psp.student_id=s.id  "
        f"SET preference_rank = %s "
        f"WHERE s.student_id = %s "
    )

def set_preference():
    return (
        f"UPDATE project_student_preferences  AS psp  "
        f"LEFT JOIN students AS s ON psp.student_id=s.id  "
        f"SET preference = %s "
        f"WHERE s.student_id = %s AND project_id = %s  "
    )