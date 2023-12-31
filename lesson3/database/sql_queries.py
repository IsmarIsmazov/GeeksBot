CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
         TELEGRAM_ID INTEGER,
         USERNAME CHAR(50),
         FIRST_NAME CHAR(50),
         LAST_NAME CHAR(50),
         UNIQUE(TELEGRAM_ID)
         )
"""
CREATE_USER_FORM_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS user_form
        (ID INTEGER PRIMARY KEY,
         USER_ID INTEGER NOT NULL,
         TELEGRAM_ID INTEGER,
         NICKNAME CHAR(50),
         AGE INTEGER,
         BIO TEXT,
         GENDER TEXT,
         PHOTO TEXT,
         FOREIGN KEY (USER_ID) REFERENCES telegram_users (ID)
         )
"""

CREATE_BAN_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS ban_users
        (ID INTEGER PRIMARY KEY,
         TELEGRAM_ID INTEGER,
         COUNT INTEGER,
         UNIQUE(TELEGRAM_ID)
         )
"""

INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""

INSERT_USER_FORM_QUERY = """INSERT OR IGNORE INTO user_form VALUES (?,?,?,?,?,?,?,?)"""

SELECT_USER_BY_ID_QUERY = """SELECT ID FROM telegram_users WHERE TELEGRAM_ID = ?"""


INSERT_BAN_USER_QUERY = """INSERT OR IGNORE INTO ban_users VALUES (?,?,?)"""

SELECT_BAN_USER_QUERY = """SELECT * FROM ban_users WHERE TELEGRAM_ID = ?"""

UPDATE_BAN_USER_COUNT_QUERY = """UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?"""
