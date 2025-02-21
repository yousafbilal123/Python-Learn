import sqlite3

# Function to create a connection to the SQLite database
def create_connection():
    try:
        connection = sqlite3.connect("example.db")
        return connection
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

# Function to create a new user
def create_user(name, age):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, age)
            VALUES (?, ?)
        ''', (name, age))
        conn.commit()
        conn.close()

# Function to read all users
def read_users():
    conn = create_connection()
    users = []
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users_data = cursor.fetchall()
        for row in users_data:
            users.append({"id": row[0], "name": row[1], "age": row[2]})
        conn.close()
    return users

# Function to update a user's details
def update_user(user_id, name, age):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users
            SET name = ?, age = ?
            WHERE id = ?
        ''', (name, age, user_id))
        conn.commit()
        conn.close()

# Function to delete a user
def delete_user(user_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM users WHERE id = ?
        ''', (user_id,))
        conn.commit()
        conn.close()

# Main function to demonstrate the CRUD operations
def main():
    create_table()  # Create table if it doesn't exist

    # Create some users
    create_user("Alice", 30)
    create_user("Bob", 25)

    # Read and display all users
    print("Users before update:")
    users = read_users()
    for user in users:
        print(user)

    # Update a user's details
    update_user(1, "Alice", 35)  # Updating Alice's age to 35

    # Read and display users again
    print("\nUsers after update:")
    users = read_users()
    for user in users:
        print(user)

    # Delete a user
    delete_user(2)  # Deleting Bob

    # Read and display users after deletion
    print("\nUsers after deletion:")
    users = read_users()
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
