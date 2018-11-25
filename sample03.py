import sqlite3


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM users WHERE age < 20"

    results = cursor.execute(sql)

    users = results.fetchall()
    print(users)
    for user in users:
        user_name = user[0]
        user_age = user[1]
        print(f"{user_name}さんは{user_age}歳です")

    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()
