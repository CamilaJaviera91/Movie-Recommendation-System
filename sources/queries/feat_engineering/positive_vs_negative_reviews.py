# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')  # Add the directory to the system path

from connection import connection  # Import the function to establish a database connection

# Import necessary libraries for database interaction and data processing
import psycopg2  # PostgreSQL database adapter
import locale    # For setting regional settings
import pandas as pd  # For handling data in tabular format

def positive_vs_negative_reviews():
    """
    Queries the movie recommendation database to retrieve statistics about movies,
    including title, release year, genre, number of positive/negative reviews, 
    and the total number of reviews.
    
    Returns:
        pd.DataFrame: A DataFrame containing the retrieved movie data.
    """
    # Attempt to set the locale to Spanish (Spain) for proper number formatting
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # Setting locale for number formatting
    except locale.Error:
        print("Error: Could not establish the regional settings.")  # Handle locale setting failure
    
    # Establish a connection to the database using the imported connection function
    con = connection()
    if con is None:
        print("Error: Could not establish a connection to the database.")  # Handle connection failure
        return None

    try:
        cursor = con.cursor()  # Create a cursor object to interact with the database

        # SQL query to fetch movie details along with aggregated review statistics
        cursor.execute('''
            SELECT
                m.title AS movies,  -- Movie title
                m.release_year AS release,  -- Release year of the movie
                m.genre AS genre,  -- Movie genre
                SUM(CASE WHEN r.rating > 3 THEN 1 ELSE 0 END) AS positive_reviews,  -- Count of positive reviews
                SUM(CASE WHEN r.rating <= 3 THEN 1 ELSE 0 END) AS negative_reviews,  -- Count of negative reviews
                COUNT(r.rating_id) AS total_reviews  -- Total number of reviews
            FROM postgres.movie_recommendation.movies m
            LEFT JOIN postgres.movie_recommendation.ratings r 
                ON r.movie_id = m.movie_id  -- Join movies with ratings based on movie_id
            GROUP BY 
                m.title, 
                m.release_year, 
                m.genre  -- Group by movie attributes
            ORDER BY 
                COUNT(r.rating_id) DESC;  -- Order by number of reviews in descending order
        ''')

        records = cursor.fetchall()  # Retrieve all query results

        # Extract column names from the query result
        columns = [desc[0] for desc in cursor.description]
        
        # Convert results into a Pandas DataFrame for easy analysis and visualization
        df = pd.DataFrame(records, columns=columns)

        return df  # Return the DataFrame for further use in the program

    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")  # Handle SQL execution errors
        return None

    finally:
        # Close cursor and connection safely to free up resources
        cursor.close()
        con.close()
        print("Connection closed successfully.")  # Confirm successful closure