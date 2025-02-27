import random
import faker
import datetime

fake = faker.Faker() # fakes data

#define realistic medical conditions
medical_conditions = ["Hypertension", "Asthma", "Heart Disease", "Pneumonia", "Fractured Bone", "Depression", "Flu",
                    "Gastroenteritis", "Migraines"]

# define provider speciaties
specialties = ["Cardiology", "Pediatrics", "Neurology", "General Medicine", "Orthopedics",
               "Endocrinology", "Dematology", "Psychiatry", "Oncology", "Pulmonology"]

#Generating the empty list for SQL statements
sql_statements = []

#Generate Patients (500) more
for patient_id in range(11, 511):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_year = random.randint(1940, 2010)
    gender = random.choice(["Male", "Female"])
    zip_code = fake.zipcode()
    sql_statements.append(f"INSERT INTO Patients(patient_id, first_name, last_name, birth_year, gender, zip_code) "
                          f"VALUES ({patient_id}, '{first_name}','{last_name}', {birth_year}, '{gender}', '{zip_code}');")


