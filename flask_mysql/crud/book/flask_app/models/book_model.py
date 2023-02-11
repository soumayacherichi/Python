from flask_app.config.mysqlconnection import connectToMySQL
#=============Create a new table with==================
class Book:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.users_id = data_dict['users_id']
        self.title = data_dict['title']
        self.page = data_dict['page']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

#!! all queries are class methods
# ===============Read all users ====================
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM books;"
        results=connectToMySQL(DATABASE).query_db(query)
        print (f"Result from database = {results}")
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users
# ===============Create user ====================
    @classmethod
    def create_user(cls,data_dict):
        query = """
        INSERT INTO users (username, email, age)
        values (%(username)s, %(email)s, %(age)s)"""
        return connectToMySQL("w2day3").query_db(query,data_dict)
# ===============Read One User ====================
    @classmethod
    def get_one(cls,data_dict):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results= connectToMySQL("w2day3").query_db(query,data_dict)
        print(results)
        if results:
            return cls(results[0])
        return []
# ===============Insert One User ====================