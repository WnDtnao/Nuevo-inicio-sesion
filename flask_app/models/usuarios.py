from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    db = "core"  

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL(cls.db).query_db(query, data)
        if not resultado:
            return None
        return cls(resultado[0])