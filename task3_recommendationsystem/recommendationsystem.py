# A simple recommendation system
# Change this part of your code in the file:
data = {
    'User1': {'Matrix': 5, 'Titanic': 1}, # Avatar is not seen
    'User2': {'Matrix': 4, 'Titanic': 2, 'Avatar': 5}, # User2 rated Avatar 5
    'User3': {'Matrix': 1, 'Titanic': 5, 'Avatar': 1}
}

def recommend(target_user, data):
    all_movies = {'Matrix', 'Titanic', 'Avatar'}
    seen = set(data[target_user].keys())
    not_seen = all_movies - seen
    
    # We will just look at User2 to recommend to User1
    best_match = 'User2'
        
    for movie in not_seen:
        if data[best_match].get(movie, 0) > 3:
            # Print directly inside the function
            print(f"Recommended for {target_user}: {movie}")
            return # Exit after finding one
    print("No recommendations found.")

# Call the function without printing its return value, since it prints inside
recommend('User1', data)
