###############################
### Dianyi Jiang            ###
###############################

# search companies
def search_companies(company_name="", mentor_name="", project_title=""):
    search_by_cname = "c.name LIKE %s "
    search_by_mname = "CONCAT(i.first_name, ' ', i.last_name) LIKE %s "
    search_by_ptitle = "p.title LIKE %s "

    where_clause = ""
    if len(company_name) == 0 and len(mentor_name) == 0 and len(project_title) == 0:
        where_clause = ""
    elif len(mentor_name) == 0  and len(project_title) == 0:
        where_clause = f"WHERE {search_by_cname}"
    elif len(company_name) == 0 and len(project_title) == 0:
        where_clause = f"WHERE {search_by_mname}"
    elif len(mentor_name) == 0 and len(company_name) == 0:
        where_clause = f"WHERE {search_by_ptitle}"
    elif len(mentor_name) == 0:
        where_clause = f"WHERE {search_by_cname} AND {search_by_ptitle}"
    elif len(project_title) == 0:
        where_clause = f"WHERE {search_by_cname} AND {search_by_mname}" 
    elif len(company_name) == 0:
        where_clause = f"WHERE {search_by_mname} AND {search_by_ptitle}"
    else:
        where_clause = f"WHERE {search_by_cname} AND {search_by_mname} AND {search_by_ptitle}"

    return (
        f"SELECT c.name AS CompanyName, "
        f"CONCAT(i.first_name, ' ', i.last_name) AS MentorName, "
        f"u.email AS MentorEmail, "
        f"i.phone_number AS MentorPhone, "
        f"p.title AS ProjectTitle, "
        f"p.number_of_students AS NoOfStudents, "
        f"p.id AS ProjectID, "
        f"p.summary AS ProjectSummary, "
        f"p.project_type AS ProjectType, "
        f"CASE "
        f"WHEN s.name is null THEN \"No skills required\" "  
        f"ELSE CONCAT(\"\", GROUP_CONCAT(s.name SEPARATOR ','), \"\") "
        f"END AS Skills "
        f"FROM "
        f"companies c "
        f"join industry_mentors i on c.id = i.company_id "
        f"join users u on u.id = i.id "
        f"join projects p on i.id = p.mentor_id "
        f"left join project_skills ps on p.id = ps.project_id "
        f"left join skills s on ps.skill_id = s.id "
        f"{where_clause} "
        f"GROUP by p.id "
        f"ORDER BY c.name "
    )

# company list
def company_list(company_name=""):
    search_by_cname = "c.name LIKE %s "

    where_clause = ""
    if len(company_name) == 0:
        where_clause = ""

    else:
        where_clause = f"WHERE {search_by_cname} "

    return (
        f"SELECT c.id AS ID, "
        f"c.name AS Name, "
        f"if(char_length(c.description) > 50, CONCAT(SUBSTRING(c.description, 1, 50), '...'), c.description) AS Description "
        f"FROM companies c "
        f"{where_clause} "
    )

# company list
def get_company():
    return (
        f"SELECT c.id AS ID, "
        f"c.name AS Name, "
        f"c.description AS Description "
        f"FROM companies c "
        f"WHERE id = %s;"
    )

# company list
def add_company():
    return (
        f"INSERT INTO `companies` "
        f"(`name`, `description`) "
        f"VALUES (%s, %s);"
    )

# update company
def update_company():
    return (
        f"UPDATE `companies` SET "
        f"`name` = %s, "
        f"`description` = %s "
        f"WHERE `id` = %s; "
    )

# mentor list
def mentor_list(name=""):
    search_by_mname = "CONCAT(im.first_name, ' ', im.last_name) LIKE %s "

    where_clause = ""
    if len(name) == 0:
        where_clause = ""
    else:
        where_clause = f"WHERE {search_by_mname} "

    return (
        f"SELECT im.id AS ID, "
        f"CONCAT(im.first_name, ' ', im.last_name) AS Name, "
        f"p.title AS `Project Title` "
        f"FROM industry_mentors im "
        f"LEFT JOIN projects p ON im.id = p.mentor_id "
        f"{where_clause};"
    )

# mentor list
def get_mentor():
    return (
        f"SELECT u.id AS ID, "
        f"u.username AS Username, "
        f"im.first_name AS `First Name`, "
        f"im.last_name AS `Last Name`, "
        f"u.email AS Email, "
        f"im.phone_number AS Number, "
        f"c.name AS `Company Name`, "
        f"c.id AS `Company ID` "
        f"FROM `users` u "
        f"LEFT JOIN `industry_mentors` as im ON u.id = im.id "
        f"LEFT JOIN `companies` as c ON im.company_id = c.id "
        f"WHERE u.id = %s;"
    )

# mentor list
def validate_mentor_username():
    return (
        f"SELECT * FROM `users` "
        f"WHERE `username` = %s;"
    )

# mentor list
def validate_mentor_email():
    return (
        f"SELECT * FROM `users` "
        f"WHERE `email` = %s;"
    )

# mentor list
def add_mentor_user():
    return (
        f"INSERT INTO `users` "
        f"(`username`, `email`, `user_type`, `password`, `first_time_login`, `password_reset_token`) "
        f"VALUES (%s, %s, 2, '2d391cf135b02a8a1427014dab3761c9', NULL, NULL); "
    )

# mentor list
def add_mentor():
    return (
        f"INSERT INTO `industry_mentors` "
        f"(`id`, `company_id`, `first_name`, `last_name`, `phone_number`) "
        f"VALUES (%s, %s, %s, %s, %s);"
    )

# update mentor
def update_mentor_user():
    return (
        f"UPDATE `users` SET "
        f"`username` = %s, "
        f"`email` = %s "
        f"WHERE `id` = %s; "
    )

# update mentor
def update_mentor():
    return (
        f"UPDATE `industry_mentors` SET "
        f"`company_id` = %s, "
        f"`first_name` = %s, "
        f"`last_name` = %s, "
        f"`phone_number` = %s "
        f"WHERE `id` = %s; "
    )

# search students
def search_students(student_id="", student_name="", student_status=""):
    search_by_sid = "st.student_id LIKE %s "
    search_by_sname = "CONCAT(st.first_name, ' ', st.last_name) LIKE %s "
    search_by_sstatus = "p.status LIKE %s "

    where_clause = ""
    if len(student_id) == 0 and len(student_name) == 0 and len(student_status) == 0:
        where_clause = ""
    elif len(student_name) == 0  and len(student_status) == 0:
        where_clause = f"WHERE {search_by_sid}"
    elif len(student_id) == 0 and len(student_status) == 0:
        where_clause = f"WHERE {search_by_sname}"
    elif len(student_name) == 0 and len(student_id) == 0:
        where_clause = f"WHERE {search_by_sstatus}"
    elif len(student_name) == 0:
        where_clause = f"WHERE {search_by_sid} AND {search_by_sstatus}"
    elif len(student_status) == 0:
        where_clause = f"WHERE {search_by_sid} AND {search_by_sname}" 
    elif len(student_id) == 0:
        where_clause = f"WHERE {search_by_sname} AND {search_by_sstatus}"
    else:
        where_clause = f"WHERE {search_by_sid} AND {search_by_sname} AND {search_by_sstatus}"

    return (
        f"SELECT st.student_id AS StudentID, "
        f"CONCAT(st.first_name, ' ', st.last_name) AS StudentName, "
        f"u.email AS StudentEmail, "
        f"st.phone_number AS StudentPhone, "
        f"p.status AS PlacementStatus, "
        f"st.cv_file_path AS StudentCV, "
        f"CASE "
        f"WHEN s.name is null THEN \"Not specified\" "  
        f"ELSE CONCAT(\"\", GROUP_CONCAT(s.name SEPARATOR ','), \"\") "
        f"END AS Skills "
        f"FROM "
        f"students st "
        f"join users u on u.id = st.id "
        f"join placements p on st.id = p.student_id "
        f"left join student_skills ss on st.id = ss.student_id "
        f"left join skills s on ss.skill_id = s.id "
        f"{where_clause} "
        f"GROUP by p.id "
        f"ORDER BY st.last_name "
    )

def get_current_student_preferred_mentors():
    return (
        f"SELECT im.id AS 'mentor id' ,"
        f"spp.preference AS 'rank' "
        f"FROM students AS s "
        f"LEFT JOIN student_project_preferences AS spp "
        f"ON s.id = spp.student_id  "
        f"LEFT JOIN projects AS p "
        f"ON p.id = spp.project_id "
        f"LEFT JOIN industry_mentors AS im  ON im.id = p.mentor_id "
        f"WHERE s.student_id = %s; "
    )

def get_mentors_who_preferred_current_student():
    return (
        f"SELECT im .id AS 'mentor id', "
        f"psp.preference AS 'rank' "
        f"FROM project_student_preferences AS psp "
        f"LEFT JOIN students AS s ON s.id = psp.student_id "
        f"LEFT JOIN projects AS p ON p.id = psp .project_id "
        f"LEFT JOIN industry_mentors AS im ON im.id = p.mentor_id "
        f"WHERE s.student_id = %s; "
    )

def get_recommend_mentos_info():
    return (
        f"SELECT im.id, "
        f"CONCAT(im.first_name, ' ', im.last_name) AS 'mentor name', "
        f"c.`name` AS 'company name' "
        f"FROM industry_mentors AS im  "
        f"LEFT JOIN projects AS p ON im.id = p.mentor_id "
        f"LEFT JOIN companies AS c ON c.id = im.company_id "
        f"WHERE im.id = %s "
    )

def get_current_mentor_preferred_students():
    return (
        f"SELECT s.id AS 'student id' , "
        f"psp.preference AS 'rank' "
        f"FROM students AS s "
        f"LEFT JOIN project_student_preferences AS psp ON s.id = psp.student_id "
        f"LEFT JOIN projects AS p ON p.id =psp.project_id "
        f"LEFT JOIN industry_mentors AS im ON p.mentor_id = im.id "
        f"WHERE im.id = %s "
    )

def get_students_who_preferred_current_mentor():
    return (
        f"SELECT  s.id AS 'student id', "
        f"spp.preference AS 'rank' "
        f"FROM students AS s "
        f"LEFT JOIN student_project_preferences AS spp  "
        f"ON spp.student_id = s.id "
        f"LEFT JOIN projects AS p  "
        f"ON spp.project_id = p.id "
        f"LEFT JOIN industry_mentors AS im  "
        f"ON im.id = p.mentor_id "
        f"WHERE im.id = %s "
    )

def get_recommend_students_info():
    return (
        f"SELECT "
        f"students.student_id AS `Student ID`,"
        f"concat(students.first_name, ' ', students.last_name) AS `Student name`, "
        f"GROUP_CONCAT(skills.name) AS Skills,"
        f"students.phone_number AS `Phone Number`,"
        f"students.cv_file_path AS CV "
        f"FROM "
        f"students "
        f"LEFT JOIN "
        f"student_skills ON students.id = student_skills.student_id "
        f"LEFT JOIN "
        f"skills ON student_skills.skill_id = skills.id "
        f"WHERE students.id =%s "
        f"GROUP BY students.id; "
    )

def get_placement_details():
    return (
        f"SELECT CAST((SELECT SUM(number_of_students)  FROM projects) AS CHAR) AS `Total Available Placements`, "
        f"(SELECT count(*)  FROM students WHERE ownproject = 1) AS `Students Have Placements`, "
        f"CAST((SELECT COUNT(student_id) AS Students FROM placements) AS CHAR) AS `Students Need Placement`; "
    )

def get_potential_placements():
    return (
        f"SELECT cm.name AS `Company Name`, COUNT(pl.student_id) AS `Potential Placements` "
        f"FROM placements AS pl "
        f"join projects AS pr on pl.project_id = pr.id "
        f"join industry_mentors AS im on pr.mentor_id = im.id "
        f"join companies AS cm on im.company_id = cm.id "
        f"WHERE pl.status in ('confirmed', 'potential') "
        f"GROUP BY cm.name; "
    )

  
def get_placement_status():
    return (
        f"select students.student_id AS `Student ID`, "
        f"CONCAT(students.first_name,' ', students.last_name) AS Name, "
        f"projects.title as `Project Title`, "
        # f"projects.number_of_students, "
        f"companies.name AS Company, "
        f"projects.title as `Project Title`, "
        f"projects.summary , "
        f"projects.number_of_students ,"
        f"projects.project_type "
        f"from placements "
        f"join students on placements.student_id = students.id "
        f"JOIN projects ON placements.project_id = projects.id "
        f"JOIN industry_mentors ON projects.mentor_id = industry_mentors.id "
        f"JOIN companies ON industry_mentors.company_id = companies.id"
    )