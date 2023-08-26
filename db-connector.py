from getpass import getpass
from mysql.connector import connect, Error

query_select = """
select* from roles
"""
#query="""
#insert into new_table (title)
#VALUES ('Project Manager'), ('Business Analyst'), ('System Analyst');
#"""

query_insert = """
insert into roles (r_title)
values ('Designer_Sirenski'), ('Programmer_Sirenski'), ('Project Manager_Sirenski'), ('Business Analyst_Sirenski'), ('System Analyst_Sirenski');
"""


#select * from new_table;
#"""
query_ater = """
ALTER IGNORE TABLE roles ADD UNIQUE INDEX (r_title)
"""
#Какой запрос на удаение дубликатов строк по названию? AAlter Ignore  не работает
try:
    with connect (host="91.149.187.115", port = "43251", user="shopuser", password="1346792c212C_C", database="test_shop") as connection:
        print (connection)
        with connection.cursor() as cursor:
            cursor.execute(query_select)
        #connection.commit() - если нужно сохранить изменения в БД. Используется с insert| create table.
        # Если данные только заьираются, то применяется  fetchall
            result=cursor.fetchall()
            print(result)
            
            cursor.execute(query_insert)
            connection.commit()
            print(result)
            
            cursor.execute(query_ater)
            result=cursor.fetchall()
            print(result)
except Error as e:
    raise


#как сделать так, чтобы при запуске срабатывал только нужный запрос, а не все?
#каким запросом удаляются дубликаты строк?



