# A simple recommendation system
data = {
    'User1': {'Matrix': 5, 'Titanic': 1, 'Avatar': 4},
    'User2': {'Matrix': 4, 'Titanic': 2, 'Avatar': 5},
    'User3': {'Matrix': 1, 'Titanic': 5, 'Avatar': 1}
}

def recommend(target_user, data):
    all_movies = {'Matrix', 'Titanic', 'Avatar'}
    seen = set(data[target_user].keys())
    not_seen = all_movies - seen
    
    if target_user == 'User1':
        best_match = 'User2'
    else:
        best_match = 'User1'
        
    for movie in not_seen:
        if data[best_match].get(movie, 0) > 3:
            print(f"Recommended for {target_user}: {movie}")

recommend('User1', data)
