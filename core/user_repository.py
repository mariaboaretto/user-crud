import sqlite3
from core.user import User


# Ways to format the query:
# "...VALUES (?, ?, ?)", (first_name, last_name, email)
# "...VALUES (:first_name, :last_name, :email)", {'first_name': first_name, 'last_name': last_name, 'email': email}

class UserRepository:
    def __init__(self):
        # Creates the user_list.db file if it doesn't exist or connect to an existing file
        self.conn = sqlite3.connect("../user_list.db")
        # Creates cursor for executing queries
        self.c = self.conn.cursor()
        self.__create_user_table()

    # Creates Users table if it does not exist in the db
    def __create_user_table(self):
        with self.conn:
            self.c.execute("CREATE TABLE IF NOT EXISTS users ("
                           "user_id INTEGER PRIMARY KEY,"
                           "f_name TEXT NOT NULL,"
                           "l_name TEXT NOT NULL,"
                           "email TEXT UNIQUE NOT NULL,"
                           "username TEXT UNIQUE NOT NULL,"
                           "psswrd TEXT NOT NULL)")

    def insert_user(self, first_name, last_name, email, username, password):
        with self.conn:
            self.c.execute("INSERT INTO users (f_name, l_name, email, username, psswrd)"
                           "VALUES (?, ?, ?, ?, ?)", (first_name, last_name, email, username, password))

    def select_all_users(self) -> list[User]:
        user_list = []

        for user in self.c.execute("SELECT user_id, f_name, l_name, email, username, psswrd FROM users").fetchall():
            new_user = User(user[0], user[1], user[2], user[3], user[4], user[5])
            user_list.append(new_user)

        return user_list

    # Removes a user based on the user_id
    def remove_user_by_user_id(self, user_id: int):
        with self.conn:
            self.c.execute("DELETE FROM users WHERE user_id = (:user_id)", {"user_id": user_id})

    # Updates user's first name and last name information
    def update_user_info(self, user_id: int, first_name: str = None, last_name: str = None):
        query = "UPDATE users SET "

        dirty = False

        if first_name is not None:
            if dirty:
                query += ", "

            query += "f_name = '{}'".format(first_name)
            dirty = True

        if last_name is not None:
            if dirty:
                query += ", "

            query += "l_name = '{}'".format(last_name)
            dirty = True

        query += " WHERE user_id = '{}'".format(user_id)

        with self.conn:
            self.c.execute(query)

    # Update user's password
    def update_user_password(self, user_id: int, password: str):
        with self.conn:
            self.c.execute("UPDATE users SET psswrd = ? WHERE user_id = ?", (password, user_id))

    def filter_users_by_search_text(self, search_text: str) -> list[User]:
        search_text = "%" + search_text + "%"
        filtered_users = []

        for user in self.c.execute("""SELECT user_id, f_name, l_name, email, username, psswrd FROM users
                                        WHERE f_name LIKE ? COLLATE NOCASE
                                        OR l_name LIKE ? COLLATE NOCASE
                                        OR username LIKE ? COLLATE NOCASE
                                        OR email LIKE ? COLLATE NOCASE""",
                                   (search_text, search_text, search_text, search_text)).fetchall():
            new_user = User(user[0], user[1], user[2], user[3], user[4], user[5])
            filtered_users.append(new_user)

        return filtered_users

    def find_user_by_user_id(self, user_id: int):
        self.c.execute("""SELECT user_id, f_name, l_name, email, username, psswrd FROM users
                          WHERE user_id = :user_id""", {"user_id": user_id})

        user = self.c.fetchone()

        if user:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        else:
            raise Exception("User not found")
