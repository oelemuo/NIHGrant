"""
Generate & Insert Community-Level Data

- Generate realistic community data (weather, food insecurity, housing instability).
- Insert it into the database automatically.
- Ensure consistency with your Patients and Visits data.
"""


import faker
import random

from generateSQL import sql_statements, sql_file

fake = faker.Faker()

# Define Community Factors
weather_conditions = ["Snowstorm", "Cold", "Heatwave", "Sunny", "Blizzard", "Windy", "Flooding", "Thunderstorm",
                      "Hurricane Warning", "Heavy Rain"]
food_insecurity_levels = ["Low", "Medium", "High"]
housing_instability_levels = ["Low", "Medium", "High"]

#generate sql statements
sql_statements = []

#Generate Community Data
for community_data_id in range(1,101):
    zip_code = fake.zipcode()
    weather = random.choice(weather_conditions)
    food_insecurity = random.choice(food_insecurity_levels)
    housing_instability = random.choice(food_insecurity)

    sql_statements.append(f"INSERT INTO Community_Data (community_data_id, zip_code, weather_condition, food_insecurity_level,"
                          f"housing_instability_level, ) VALUES ({community_data_id}, '{zip_code}','{weather}', '{food_insecurity}', '{housing_instability}')")
# Saving SQL script as a file
sql_file_path = r"C:\Users\obinn\Documents\insert_community_data.sql"
with open(sql_file_path, "w", encoding="utf-8") as sql_file:
    sql_file.write("\n".join(sql_statements))

print(f"SQL file generated: {sql_file_path}")