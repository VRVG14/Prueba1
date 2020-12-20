import Connector
class Consultas():
    """
    docstring
    """
    con = Connector.Connector()

    def querySimok(self, query):
        """
        Metodo para hacer una consulta general sobre algo
        """
        
        self.con.apuntador.execute(query)
        result = self.con.apuntador.fetchall()
        return result
