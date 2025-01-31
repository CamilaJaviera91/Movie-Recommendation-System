from faker import Faker
import random

# Initialize the Faker library to generate random user data
fake = Faker()

# Set the number of user entries to generate
num_entries = 200

# Generate unique user IDs in advance to ensure uniqueness
userid = random.sample(range(1000, 9999), num_entries)  # Generate unique user IDs within a range

# Generate random user attributes
name = [fake.name_nonbinary().capitalize() for _ in range(num_entries)]  # Generate non-binary names
email = [fake.email().lower() for _ in range(num_entries)]  # Generate lowercase email addresses
password = [fake.password() for _ in range(num_entries)]  # Generate random passwords
joindate = [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_entries)]  # Generate random join dates within the last 10 years

# Combine the generated data into a structured list of tuples
users = [
    (userid[i], name[i], email[i], password[i], joindate[i])
    for i in range(num_entries)
]

# Print the generated user data in SQL INSERT format
print("INSERT INTO movie_recommendation.users (user_id, username, email, password, join_date) VALUES")
values = ",\n".join(
    [f"    ({u[0]}, '{u[1]}', '{u[2]}', '{u[3]}', '{u[4]}')" for u in users]
)
print(values + ";")