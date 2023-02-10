from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
#=============Create a new table with==================
class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

#!! all queries are class methods
# ===============Read all users ====================
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM users;"
        results=connectToMySQL("user").query_db(query)
        print (f"Result from database = {results}")
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users
# ===============Create user ====================
    @classmethod
    def create_user(cls,data_dict):
        query = """
        INSERT INTO users (first_name, last_name, email)
        values (%(first_name)s, %(last_name)s, %(email)s)"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
# ===============Read One User ====================
    @classmethod
    def get_one(cls,data_dict):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results= connectToMySQL(DATABASE).query_db(query,data_dict)
        print(results)
        if results:
            return cls(results[0])
        return []
# ===============Delete One User ====================
@classmethod
def delete_one(cls,data_dict):
    query = "DELETE FROM users WHERE id = %(id)s;"
    return connectToMySQL(DATABASE).query_db(query,data_dict)
# ===============Update One User ====================
@classmethod
def update_one(cls,data_dict):
    query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
    return connectToMySQL(DATABASE).query_db(query,data_dict)

