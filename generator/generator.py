from faker import Faker

from data.data import Customer, User

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
