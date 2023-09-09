###############################
### MCCT                    ###
###############################

def update_student_user():
    return (
        f"UPDATE `users` SET "
        f"`email` = %s "
        f"WHERE `id` = %s; "
    )

def update_student_profile():
    return (
        f"UPDATE `students` SET "
        f"`first_name` = %s, "
        f"`last_name` = %s, "
        f"`alternative_name` = %s, "
        f"`preferred_name` = %s, "
        f"`phone_number` = %s, "
        f"`address` = %s, "
        f"cv_file_path = %s "
        f"WHERE `id` = %s ;"
    )

def get_student_profile():
    return (
        f"select "
        f"u.username, "
        f"u.email, "
        f"first_name, "
        f"last_name, "
        f"alternative_name, "
        f"preferred_name, "
        f"phone_number, "
        f"address, "
        f"cv_file_path, "
        f"s.created_at, "
        f"s.updated_at "
        f"from students as s "
        f"INNER JOIN users u ON s.id = u.id "
        f"where u.id = %s ;"
    )

def query_first_time_login():
    return (
        f"SELECT first_time_login "
        f"FROM users "
        f"WHERE id = %s; "
    )

def query_access_to_projects():
    return (
        f"SELECT finish_questionnaire, ownproject "
        f"FROM students "
        f"WHERE id = %s; "
    )

def query_placement_status():
    return (
        f"SELECT pr.id AS ProjectID, "
        f"pr.title AS ProjectTitle, "
        f"pr.project_type AS ProjectType, "
        f"pl.status, "
        f"pr.summary  AS ProjectSummary, "        
        f"pr.number_of_students AS NoOfStudents, "
        f"CONCAT(im.first_name, ' ', im.last_name) AS MentorName, "
        f"CASE "
        f"WHEN s.name is null THEN \"No skills required\" "  
        f"ELSE CONCAT(\"\", GROUP_CONCAT(s.name SEPARATOR ','), \"\") "
        f"END AS Skills "
        f"FROM placements pl "
        f"JOIN projects pr on pl.project_id = pr.id "
        f"JOIN industry_mentors im on pr.mentor_id = im.id "
        f"left join project_skills ps on pr.id = ps.project_id "
        f"left join skills s on ps.skill_id = s.id "
        f"WHERE student_id = %s "
        f"GROUP by pr.id; "
    )

def query_prefered_projects():
    return (
        f"SELECT p.id AS project_id,  "
        f"c.name AS company_name, "
        f"p.title, "
        f"p.summary, "
        f"spp.preference "
        f"FROM students AS s "
        f"LEFT JOIN student_project_preferences AS spp "
        f"ON s.id = spp.student_id "
        f"LEFT JOIN projects AS p "
        f"ON spp.project_id = p.id "
        f"LEFT JOIN industry_mentors AS im ON p.mentor_id = im.id "
        f"LEFT JOIN companies AS c ON im.company_id =c.id "
        f"WHERE s.id = %s "
        f"ORDER BY spp.preference_rank DESC ;"
    )

def query_available_projects(project_name=""):
    search_by_project = "p.title LIKE %s "
    where_clause = ""
    
    if len(project_name) > 0:
        where_clause = f"WHERE {search_by_project} "

    return (
        f"SELECT p.id AS `Project ID`, "
        f"p.title AS `Project Name`, "
        f"CONCAT(im.first_name, ' ', im.last_name) AS Mentor, "
        f"c.`name` AS `Company Name`, "
        f"p.summary AS `Summary`, "
        f"COUNT(pl.student_id) AS students_enrolled, "
        f"p.number_of_students "
        f"FROM projects AS p "
        f"LEFT JOIN industry_mentors AS im ON p.mentor_id = im.id "
        f"LEFT JOIN placements AS pl ON p.id = pl.project_id "
        f"LEFT JOIN companies AS c ON im.company_id = c.id "
        f"{where_clause}"
        f"GROUP BY p.id "
        f"HAVING students_enrolled < p.number_of_students; "
    )

def check_student_prefered_projects_numbers():
    return (
        f"SELECT count(*) AS total_prefered_project "
        f"FROM student_project_preferences "
        f"WHERE student_id = %s; "
    )

def add_student_prefered_project():
    return (
        f"INSERT INTO student_project_preferences(student_id, project_id) "
        f"VALUES(%s, %s); "
    )

def check_duplication_of_perfered_project():
    return (
        f"SELECT COUNT(*) AS prefered_project_number "
        f"FROM student_project_preferences "
        f"WHERE student_id = %s AND project_id = %s; "
    )

def delete_prefered_project():
    return (
        f"DELETE FROM student_project_preferences "
        f"WHERE student_id = %s AND project_id = %s; "
    )

def set_prefered_project_rank():
    return (
        f"UPDATE student_project_preferences  "
        f"SET preference_rank = %s  "
        f"WHERE project_id = %s and student_id = %s ; "
    )

def initial_student_profile():
    return (
        f"UPDATE `students` SET "
        f"`first_name` = %s, "
        f"`last_name` = %s, "
        f"`alternative_name` = %s, "
        f"`preferred_name` = %s, "
        f"`phone_number` = %s, "
        f"`address` = %s "
        f"WHERE `id` = %s ;"
    )

def get_skills():
    return (
        f"SELECT name "
        f"From skills"
    )

def delete_student_skills():
    return (
        f"DELETE  "
        f"FROM student_skills"
        f"WHERE student_id = %s"
    )

def add_student_skills():
    return (
        f"INSERT INTO student_skills (student_id, skill_id) "
        f"VALUES ( %s , (SELECT id FROM skills WHERE skills.`name` = %s) )"
    )
def set_preference():
    return (
        f"UPDATE student_project_preferences "
        f"SET preference  = %s "
        f"WHERE student_id = %s AND project_id = %s "
    )

def set_first_login_value():
    return (
        f"UPDATE users "
        f"SET first_time_login = 0 " 
        f"WHERE id = %s "
    )

def set_questionnaire_info():
    return (
        f"UPDATE students "
        f"SET networking = %s, ownproject = %s, finish_questionnaire = 1 "
        f"WHERE id = %s "
    )

def get_finish_questionnaire():
    return (
        f"SELECT finish_questionnaire "
        f"FROM students "
        f"WHERE id = %s"
    )