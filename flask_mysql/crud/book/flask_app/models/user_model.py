from flask_app.config.mysqlconnection import connectToMySQL
#=============Create a new table with==================
class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.my_list=[]

#!! all queries are class methods
# ===============Read all users ====================
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM users;"
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
        INSERT INTO users (first_name, last_name)
        values (%(first_name)s, %(last_name)s)"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
        query_2 = """
        SELECT * FROM users left JOIN books on users.id = books.user_id WHERE id=%(id)s;"""
# ===============Read One User ====================
    @classmethod
    def get_one(cls,data_dict):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results= connectToMySQL(DATABASE).query_db(query,data_dict)
        print(results)
        if results:
            return cls(results[0])
        return []
# ===============Insert One User ====================


