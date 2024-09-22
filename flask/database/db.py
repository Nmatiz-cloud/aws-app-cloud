import pymysql

punto_enlace = 'db-rds-cloud.cjuc4cc60l7d.us-east-2.rds.amazonaws.com'
user  = 'admin'
password = 'admin_cloud'
#intenta conectarse a la base de datos


def connectionsql():
    try:
        obj_connect = pymysql.connect(
            host=punto_enlace,
            user=user,
            password=password
        )
        print("Conexion satisfactoria a la base de datos")
        return obj_connect
    #para generar el error en caso de que no se conecte a la base de datos
    except Exception as err:
        print("Error", err)

connectionsql()

def add_user(ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL):
    try:
        instruction_sql = "INSERT INTO db_user.users (ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL) values ("+ID+", '"+NAME_USER+"', '"+LAST_NAME+"', '"+BIRTHDAY+"', '"+ACT_LABORAL+"')"
        obj_connect = connectionsql()
        obj_connect.cursor().execute(instruction_sql)
        obj_connect.commit()
        print("El usuario fue añadido")
    except Exception as err:
        print("Error", err)