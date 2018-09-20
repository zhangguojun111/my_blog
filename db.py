import pymysql
"""
对数据库的操作

"""




def get_db():
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='')
    return db



def select():

    try:
        db = get_db()
        cs = db.cursor()
        cs.execute("select 1")
    finally:
        db.close()




def query_db(sql, args=None,one = False):
    """

    :param sql:
    :param args:
    :param one:  等于False 为查询多条记录， 等于True时返回一条记录
    :return:
    """
    try:
        db = get_db()
        cs = db.cursor()
        cs.execute("select 1")
        result = cs.fetchall()
        cs.close()
        if one :
            if len(result)>0:
                return result[0]
            else:
                return None
        else:
            return result
    finally:
        db.close()




def update_db(sql, args=None):
    try:
        db = get_db()
        cs = db.cursor()
        cs.execute("select 1")
        db.commit()
        lastrowid = cs.lastrowid
        update_count = cs.rowcount
        cs.close()
        return update_count, lastrowid
    finally:
        db.close()



def get_one_post(post_path):
    pass


def get_post_list():
    pass