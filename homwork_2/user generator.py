from faker import Faker

name = Faker('uk_UA')

fake_result = name.first_name(), name.email()
for _ in range(100):
    fake_result.count(100)

    print(fake_result)
