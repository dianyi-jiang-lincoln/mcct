###############################
### Dianyi Jiang            ###
###############################

from flask import session
import os

class User:
    def __init__(self, name, role, id="", email="", role_id=""):
        self.name = name
        self.role = role
        self.id = id
        self.role_id = role_id
        self.email = email

        if (
            session.get("name") != name
            or session.get("role") != role
            or session.get("id") != id
            or session.get("email") != email
            or session.get("role_id") != role_id
        ):
            session["name"] = name
            session["role"] = role
            session["id"] = id
            session["role_id"] = role_id
            session["email"] = email
            session["is_authenticated"] = True

    def __str__(self):
        return f"🟢 <User(id = {self.id},  name = {self.name}, role = {self.role}, role_id = {self.role_id}, email = {self.email})>"

def current_user():
    name = session.get("name")
    role = session.get("role")
    id = session.get("id")
    email = session.get("email")
    role_id = session.get("role_id")

    if name == None or role == None or id == None or email == None or role_id == None:
        return None

    return User(name=name, role=role, id=id, email=email, role_id=role_id)

def clear_session():
    session.clear()

def encrypt_password(password=""):
    import hashlib

    md5 = hashlib.md5()
    salt = os.getenv("SALT")
    password_salt = (password + salt).encode("utf-8")
    md5.update(password_salt)
    return md5.hexdigest()

def is_password_matched(password=""):
    from db import db
    from db import query

    encrypted_password = encrypt_password(password)
    db_result = db.sql_exec(
        query.validate_password(),
        params=[current_user().email],
        callback=db.get_first_mapped_title_row,
    )
    query_password = db_result.get("password")
    return encrypted_password == query_password

def user_update_password(password=""):
    from db import db
    from db import query

    encrypted_password = encrypt_password(password)
    db_result = db.sql_exec(
        query.update_user_password(),
        params=[encrypted_password, current_user().email],
        callback=db.get_first_mapped_title_row,
    )
    return True
