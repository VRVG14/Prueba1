import mysql.connector
class Connector():
    """
    docstring
    """
    mydatabase = mysql.connector.connect(host="localhost", user="root", passwd="@123AnOtHeR890@",database="Tienda", auth_plugin="caching_sha2_password")
    apuntador = mydatabase.cursor()