from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Dojo:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
#===========================Creation de survey====================
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos (name, location, language,comment) 
                    VALUES (%(name)s, %(location)s, %(language)s,%(comment)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
#===========================Read survey by id ====================
    @classmethod
    def get_by_id(cls,data):
        query ="""
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        results= connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1 :
            return False
        return cls(results[0])
#=======================Validation====================
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])<3:
            is_valid = False
            flash('Name must be at least 3 characters long',"name")
        if data['location']=="":
            is_valid  = False
            flash('You must choose a dojo location',"location")
        if data['language']=="":
            is_valid  = False
            flash('You must choose a language',"language")
        if len(data['comment'])<3:
            is_valid = False
            flash('Comment must be at least 3 characters long',"comment")
        return is_valid