import pymysql
import os

def handle_sql_query(query):
    try:
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB"),
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            cursor.execute(query)
            if query.strip().lower().startswith(("select","show")):
                result = cursor.fetchall()
            else:
                conn.commit()
                result = {"message": "Query Generated and executed successfully"}
        conn.close()
        
        return result
    except Exception as e:
        return {"error": str(e)}
