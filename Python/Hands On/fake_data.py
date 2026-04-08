from faker import Faker

fake = Faker()

print(fake.name())          # Random full name
print(fake.address())       # Random address
print(fake.email())         # Random email
print(fake.date_of_birth()) # Random DOB
print(fake.company())       # Random company name
print(fake.text())          # Random text