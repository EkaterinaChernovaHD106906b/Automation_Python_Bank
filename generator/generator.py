import random

from faker import Faker

from data.data import Customer, User, Date

faker_en = Faker('en')
Faker.seed()


def generated_customer():
    yield Customer(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        post_code=faker_en.postcode()
    )


def generated_user():
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        address=faker_en.address(),
        city=faker_en.city(),
        state=faker_en.state(),
        zipcode=faker_en.country_code(),
        phone=faker_en.phone_number(),
        ssn=faker_en.ssn(),
        user_name=faker_en.user_name(),
        password=faker_en.password()

    )


def generated_date():
    yield Date(
        day=faker_en.day_of_month(),
        month=faker_en.month(),
        year=faker_en.year()

    )


def generated_file():
    path = rf'C:\Users\user\PycharmProjects\pythonProject3\test_file{random.randint(0, 100)}.txt'
    with open(path, 'w') as file:
        file.write('Hello, world')
    return file.name, path
