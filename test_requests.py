import datetime
import requests

# Set the base URL of your API
base_url = "http://localhost:8000"

# Make a GET request to retrieve the role of a user by ID
def get_user_role(user_id):
    url = f"{base_url}/users/{user_id}/role"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["role"]
    else:
        return None

# Make a POST request to create a new user
async def create_user(name, email, role_id, password=None):
    url = f"{base_url}/users"
    data = {
        "name": name,
        "email": email,
        "role_id": role_id,
        "password": password,
        "created_at": str(datetime.datetime.today().date())  # Convert date to string
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        data = response.json()
        return data["message"]
    else:
        return None

# Test the API calls
user_role = get_user_role(1)
print(f"User Role: {user_role}")

create_result = create_user("John Doe", "john.doe@example.com", 1, "password123")
print(f"Create User Result: {create_result}")
