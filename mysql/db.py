import pymysql.cursors
import sys
import json

"""
i used this lib from an older project to save time
"""


# import config
with open('config.json') as json_config:
    config = json.load(json_config)

class Dbcon():

    def __init__(self):
        self.connection = pymysql.connect(
            host = config["mysql"]["host"],
            user = config["mysql"]["user"],
            password = config["mysql"]["pass"],
            db = config["mysql"]["db"],
            charset = config["mysql"]["charset"],
            cursorclass=pymysql.cursors.DictCursor
            )

        #return self.connection

    def __exit__(self):
        self.connection.close()

    def get(self, sql):
        try:
            with self.connection.cursor() as c:
                c.execute(sql)
                result=c.fetchall()
                return(result)
        finally:
            pass

    def set(self, sql):
        try:
            with self.connection.cursor() as c:
                c.execute(sql)
        except pymysql.err.IntegrityError:
            #place for rollback or else
            print('could not execute sql:', sql)
            raise Exception('error with mysql', sql)

        self.connection.commit()

def main():
    x = Dbcon()
    sql = "SELECT 1"
    print(x.get(sql))
    del x


if __name__ == '__main__':
    main()