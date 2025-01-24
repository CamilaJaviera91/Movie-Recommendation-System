# Movie Recommendation System

Development of a recommendation system using a movie dataset. Store the information in PostgreSQL and use Python to build a machine learning model that suggests movies based on user preferences, utilizing PostgreSQL, Pandas, and Scikit-learn tools.

## Database Schema

## <u>Connection</u>

1. In this case, we are going to use DBeaver, so the first thing we need to do is create a new connection.
- As shown in the picture, we need to configure the following settings:
    - **<u>Host</u>:** localhost
    - **<u>Database</u>:** postgres
    - **<u>Port</u>:** 5432
    - **<u>Username</u>:** postgres
    - **<u>Password</u>:** _YOUR PASSWORD_
<br>

![Clothing Store 1](./images/pic4.png)

2. After setting the parameters, we should test the connection to ensure it works before applying the configuration.

<br>

![Clothing Store 1](./images/pic5.jpg)

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

## <u>Documentation</u>

- [Postgres Documentation](https://www.postgresql.org/docs/)
- [Faker Documentation](https://faker.readthedocs.io/en/master/)
- [Random Documentation](https://docs.python.org/3/library/random.html)
- [Psycopg Documentation](https://www.psycopg.org/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [ReportLab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf)

## <u>Sources</u>

- [DBeaver Community](https://dbeaver.io/download/)
- [Install Docker Desktop on Linux](https://docs.docker.com/desktop/setup/install/linux/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Alacritty](https://github.com/alacritty/alacritty)

## <u>Contributions</u>

Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality.