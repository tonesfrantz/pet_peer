import database
import bcrypt


def insert_user(name, email, password):
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    results = database.sql_read_write(
        "INSERT INTO users(name, email, password) VALUES(%s, %s, %s) RETURNING *;", [
            name, email, password]
    )
    return results[0]


def get_user_by_email(email):
    results = database.sql_select(
        "SELECT * FROM users WHERE email = %s;", [email])
    if len(results) > 0:
        return results[0]
    else:
        return None


def get_user_by_id(user_id):
    results = database.sql_select(
        "SELECT * FROM users WHERE user_id = %s;", [user_id])
    result = results[0]
    return result


def get_all_users():
    results = database.sql_select("SELECT * FROM users;", [])
    return results


def update_user(user_id, name, email, password):
    password = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
    results = database.sql_read_write("UPDATE users SET name = %s, email = %s, password = %s WHERE user_id = %s RETURNING *;", [
        name, email, password, user_id])
    return results[0]


def delete_user(user_id):
    database.sql_write(
        "DELETE FROM users WHERE user_id = %s;", [user_id])
