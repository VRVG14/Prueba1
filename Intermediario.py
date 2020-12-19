import Connector
class Consultas():
    """
    docstring
    """
    def querySimpl(query):
        """
        Metodo para hacer una consulta general sobre algo
        """
        con = Connector.Connector()
        result = con.apuntador.execute(query)         
        return result
    
    
