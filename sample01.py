import sqlite3

def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = """CREATE TABLE users(
                name TEXT,
                age INTEGER
                )"""

    cursor.execute(sql)

    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()