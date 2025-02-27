"""
Python Script to generate synthetic data
- Creates 500 new patients, 100 new providers, and 500 new visits
- Ensures realistic zip codes, medical conditions, and timestamps
- Outputs a SQL file to be run in SQL Server
"""

import random
import faker

fake = faker.Faker()  # Fakes data

# Define realistic medical conditions
medical_conditions = ["Hypertension", "Asthma", "Heart Disease", "Pneumonia", "Fractured Bone", "Depression", "Flu",
                      "Gastroenteritis", "Migraines"]

# Define provider specialties
specialties = ["Cardiology", "Pediatrics", "Neurology", "General Medicine", "Orthopedics",
               "Endocrinology", "Dermatology", "Psychiatry", "Oncology", "Pulmonology"]

# Generating the empty list for SQL statements
sql_statements = []

# Generate Patients (500)
for patient_id in range(11, 511):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_year = random.randint(1940, 2010)
    gender = random.choice(["Male", "Female"])
    zip_code = fake.zipcode()
    sql_statements.append(f"INSERT INTO Patients (patient_id, first_name, last_name, birth_year, gender, zip_code) "
                          f"VALUES ({patient_id}, '{first_name}', '{last_name}', {birth_year}, '{gender}', '{zip_code}');")

# Generate Providers (100)
for provider_id in range(11, 111):
    provider_name = f"Dr. {fake.first_name()} {fake.last_name()}"
    specialty = random.choice(specialties)
    hospital_affiliation = fake.company()
    sql_statements.append(f"INSERT INTO Providers (provider_id, provider_name, specialty, hospital_affiliation) "
                          f"VALUES ({provider_id}, '{provider_name}', '{specialty}', '{hospital_affiliation}');")

# Generate Visits (500)
for visit_id in range(11, 511):
    patient_id = random.randint(11, 510)  # Ensure it matches generated patient IDs
    provider_id = random.randint(11, 110)  # Ensure it matches generated provider IDs
    community_data_id = random.randint(1, 10)  # Keep within existing community data
    visit_date = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
    condition = random.choice(medical_conditions)
    sql_statements.append(f"INSERT INTO Visits (visit_id, patient_id, provider_id, community_data_id, visit_date, condition) "
                          f"VALUES ({visit_id}, {patient_id}, {provider_id}, {community_data_id}, '{visit_date}', '{condition}');")

# Save SQL script to a file (Moved outside the loop)
sql_file_path = r"C:\Users\obinn\Documents\insert_testpatient.sql"
with open(sql_file_path, "w") as sql_file:
    sql_file.write("\n".join(sql_statements))

print(f"SQL file generated: {sql_file_path}")
