# Movie Recommendation System

## Database Schema

### Schema 

![imagen3](./images/pic3.png)


### `movies`
- **movie_id** (INT, PRIMARY KEY, AUTO_INCREMENT) - Unique identifier for each movie.
- **title** (VARCHAR(255)) - Title of the movie.
- **release_year** (INT) - Year the movie was released.
- **genre** (VARCHAR(100)) - Genre of the movie.
- **description** (TEXT) - Brief description of the movie.
- **director** (VARCHAR(100)) - Director of the movie.
- **duration** (INT) - Duration in minutes.
### `users`
- **user_id** (INT, PRIMARY KEY, AUTO_INCREMENT) - Unique identifier for each user.
- **username** (VARCHAR(50)) - Username.
- **email** (VARCHAR(100)) - User's email address.
- **password** (VARCHAR(255)) - Encrypted password.
- **join_date** (DATETIME) - Date the user registered.
### `ratings`
- **rating_id** (INT, PRIMARY KEY, AUTO_INCREMENT) - Unique identifier for each rating.
- **user_id** (INT, FOREIGN KEY) - Reference to the user who rated the movie.
- **movie_id** (INT, FOREIGN KEY) - Reference to the rated movie.
- **rating** (DECIMAL(3, 2)) - Rating given to the movie (e.g., from 1.0 to 5.0).
- **rating_date** (DATETIME) - Date the rating was made.

## Relationships Between Tables
1. `movies` and `ratings` are related through `movie_id`, allowing storage of ratings given to each movie.
2. `users` and `ratings` are related through `user_id`, tracking which user gave a rating.

## Use in a Recommendation System
- **Collaborative Filtering:** Use the `ratings` table to find similar behavior patterns among different users.