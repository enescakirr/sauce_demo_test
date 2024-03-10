import pymysql
import os
import configparser


def read_config():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, '../requirements/config.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path)
    DB_DATABASE = config.get("DatabaseSettings", "DB_DATABASE")
    DB_HOST = config.get("DatabaseSettings", "DB_HOST")
    DB_USER = config.get("DatabaseSettings", "DB_USER")
    return DB_USER, DB_HOST, DB_DATABASE


def connection():
    """
    Database connection açar.
    """

    DB_USER, DB_HOST, DB_DATABASE = read_config()
    return pymysql.connect(
        database=DB_DATABASE,
        host=DB_HOST,
        user=DB_USER,
    )


class Database:

    def __init__(self):
        self.config = read_config()


class DatabaseController(Database):
    def __init__(self):
        Database.__init__(self)


    @staticmethod
    def insert_data(case_name, case_path, case_status):
        db = connection()
        cursor = db.cursor()
        query = "INSERT INTO saucedemo_db.case_reports (case_name, case_path, case_status) VALUES (%s, %s, %s)"
        values = (case_name, case_path, case_status)
        cursor.execute(query, values)
        db.commit()
        db.close()
