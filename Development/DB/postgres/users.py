from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, last_name, first_name, id):
        self.email = email
        self.last_name = last_name
        self.first_name = first_name
        self.id = id 

    def __repr__(self):
        return "<User: {}>".format(self.email)
    
    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO users(email,last_name, first_name) VALUES(%s, %s, %s)',(self.email, self.last_name, self.first_name))


    @classmethod
    def load_from_db(cls, first_name):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE first_name=%s', (first_name,))
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])

       

