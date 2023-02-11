from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:

    def __init__(self,data_dict):
        self.id=data_dict['id']
        self.dojo_id=data_dict['dojo_id']
        self.first_name=data_dict ['first_name']
        self.last_name=data_dict ['last_name']
        self.age=data_dict ['age']
        self.created_at=data_dict['created_at']
        self.updated_at=data_dict['updated_at']

#============READ ALL ninjas =================
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)# result la liste qui va retourner de la database
        all_ninjas = [] 
        if results:
            for row in results:
                all_ninjas.append(cls(row))
            return all_ninjas
        return []
#============READ ONE ninja =================
    @classmethod
    def get_one(cls,data_dict):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        if result:
            return cls(result[0])
        return None

#============Create a ninja =================
    @classmethod
    def create_ninja(cls,data_dict):
        query = """INSERT INTO ninjas (dojo_id,first_name,last_name,age) 
        VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        print(f"This is the result after creating a new ninja {result}")

    #============Update a ninja =================
    @classmethod
    def update_ninja(cls,data_dict):
        query = """UPDATE ninjas SET dojo_id=%(dojo_id)s, 
        first_name=%(first_name)s,last_name=%(last_name)s,
        age=%(age)s WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
        
    #============Delete a ninja =================
    @classmethod
    def delete_ninja(cls,data_dict):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data_dict)
        