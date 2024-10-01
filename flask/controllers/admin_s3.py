import boto3
#importa las credenciales del archivo keys
from keys import ACCESS_KEY,SECRET_KEY

bucket_name = "bucket-aws-app-cloud"
def connectionS3():
#conectar sesion a AWS
    session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
#conectar al servicio S3
    session_s3 = session_aws.resource('s3')
    print("Conexion satisfactoria")
    return session_s3

#funcion para guardar archivos temporalmente
def save_file(photo):
    photo_name = "photo.jpg"
    photo_path = "/tmp/" + photo_name
    photo.save(photo_path)
    print("Photo saved")
    return photo_path, photo_name

#funcion para subir archivos a S3
def upload_file(photo_path, photo_name):
    session_s3 = connectionS3()
    session_s3.meta.client.upload_file(photo_path, bucket_name, photo_name)
    print("Photo uploaded")

#prueba de obtener datos de los objetos del bucket
def get_files():
    session_s3 = connectionS3()
#se guarda toda la informacion del bucket en la variable bucket_all 
    bucket_project = session_s3.Bucket(bucket_name)
    all_obj = bucket_project.objects.all()
    for obj in all_obj:
        print(obj.key)

