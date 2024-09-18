import pymysql

punto_enlace = 'db-rds-cloud.cjuc4cc60l7d.us-east-2.rds.amazonaws.com'
user  = 'admin'
password = 'admin_cloud'
#intenta conectarse a la base de datos


def connectionsql():
    try:
    pymysql.connect(
        host=punto_enlace,
        user=user,
        password=password
    )print("Conexion satisfactoria a la base de datos")
    #para generar el error en caso de que no se conecte a la base de datos
    except Exception as err:
        print("Error", err)

connectionSQL()