from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja

class Dojo:

    def __init__(self,data_dict):
        self.id=data_dict['id']
        self.name=data_dict['name']
        self.image=data_dict['image']
        self.created_at=data_dict['created_at']
        self.updated_at=data_dict['updated_at']
        self.ninjas_list=[] 
#============READ ALL =================
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = [] 
        if results:
            for row in results:
                all_dojos.append(cls(row))
            return all_dojos
        return []
        #================================READ ONE with his ninjas =================
    @classmethod
    def get_one(cls,data_dict):
        query = """SELECT * FROM dojos 
                    LEFT JOIN ninjas 
                    ON dojos.id = ninjas.dojo_id  
                    WHERE dojos.id=%(id)s ;"""
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        ninjas = []
        if result:
            this_dojo =  cls(result[0])
            for row in result:
                ninja_data = {
                    'id':row['ninjas.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'age': row['age'],
                    'dojo_id': row['dojo_id'],
                    'created_at' :row['ninjas.created_at'],
                    'updated_at' :row['ninjas.updated_at']
                }
                one_ninja = ninja.Ninja(ninja_data)
                ninjas.append(one_ninja)
                this_dojo.ninjas_list = ninjas
            return this_dojo
        return None
#============Create a dojo=================
    @classmethod
    def create_dojo(cls,data_dict):
        query = """INSERT INTO dojos (name, image) 
        VALUES (%(name)s,%(image)s);"""
        result= connectToMySQL(DATABASE).query_db(query,data_dict)
        print(f"This is the result after creating a new dojo {result}")
#============Update a dojo =================
    @classmethod
    def update_dojo(cls,data_dict):
        query = """UPDATE dojos SET name=%(name)s,image=%(image)s WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
        
    #============Delete a dojo =================
    @classmethod
    def delete_dojo(cls,data_dict):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data_dict)