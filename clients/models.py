import uuid

class Client:

    def __init__(self, name, company, email, position, uid =None):
        self.name =name
        self.company =company
        self.email =email
        self.position =position
        self.uid = uid or uuid.uuid4()


    def to_dict(self):
        #funcion global vars; chekea q es lo q recresa el metodo to_dic y nos permite acceder a un dic (representacion de un dic)
        return vars(self)
        

    @staticmethod     #es un metodo q se puede ejecutar sin ninguna istancia de clase
    def schema():     #no necesita self, porqe no nesesita una instancia 
        return ['name', 'company', 'email', 'position', 'uid']
        



