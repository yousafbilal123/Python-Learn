from db import create_connection
from models import User

def create_user(user: User):
    """
    Inserts a new user into the users table.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, age)
        VALUES (?, ?)
    ''', (user.name, user.age))
    conn.commit()
    conn.close()

def read_users():
    """
    Retrieves all users from the database.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()
    conn.close()
    users = [User(id=row[0], name=row[1], age=row[2]) for row in users_data]
    return users

def update_user(user: User):
    """
    Updates an existing user's details.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users
        SET name = ?, age = ?
        WHERE id = ?
    ''', (user.name, user.age, user.id))
    conn.commit()
    conn.close()

def delete_user(user_id: int):
    """
    Deletes a user by id.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM users WHERE id = ?
    ''', (user_id,))
    conn.commit()
    conn.close()
