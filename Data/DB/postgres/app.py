from database import Database
from users import User


Database.initialise(database="JedAIHouse", host="localhost", user="jedai", password="1234")
# my_user = User("cipriane@jedai.com", "Elies", "cipriane", None)
my_user = User.load_from_db('amie')
print(my_user)