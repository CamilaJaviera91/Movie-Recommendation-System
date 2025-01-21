-- Create Table: movies
CREATE TABLE movie_recommendation.movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INT NOT NULL,
    genre VARCHAR(100),
    description TEXT,
    director VARCHAR(100),
    duration INT
);

-- Create Table: users
CREATE TABLE movie_recommendation.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Table: ratings
CREATE TABLE movie_recommendation.ratings (
    rating_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES movie_recommendation.users(user_id),
    movie_id INT REFERENCES movie_recommendation.movies(movie_id),
    rating DECIMAL(3, 2) CHECK (rating >= 1.0 AND rating <= 5.0),
    rating_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Table: watchlist
CREATE TABLE movie_recommendation.watchlist (
    watchlist_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES movie_recommendation.users(user_id),
    movie_id INT REFERENCES movie_recommendation.movies(movie_id),
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Table: genres
CREATE TABLE movie_recommendation.genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Table: movie_genres
CREATE TABLE movie_recommendation.movie_genres (
    movie_id INT REFERENCES movie_recommendation.movies(movie_id),
    genre_id INT REFERENCES movie_recommendation.genres(genre_id),
    PRIMARY KEY (movie_id, genre_id)
);