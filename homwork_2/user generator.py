from faker import Faker
name = Faker('uk_UA')
for _ in range(100):
    print(name.first_name(), '-',  name.email())
