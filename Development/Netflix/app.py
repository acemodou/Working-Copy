from user import User
import json

user = User("jose")
user.add_movie("The Matrix", "Sci-FI")
user.add_movie("The interview", "Comedy")

with open('myfile.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())