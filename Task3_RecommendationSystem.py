# A simple example of a recommendation system
# We have a dictionary of users and their movie ratings
data = {
    'User1': {'Matrix': 5, 'Titanic': 1},
    'User2': {'Matrix': 4, 'Titanic': 2},
    'User3': {'Matrix': 1, 'Titanic': 5}
}

def recommend(user, user_data):
    # This is a placeholder for your logic
    print(f"Recommendations for {user} based on similar users...")

# Run the function
recommend('User1', data)
