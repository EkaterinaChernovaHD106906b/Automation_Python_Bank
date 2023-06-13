from faker import Faker

from data.data import Customer

faker_en = Faker('en')
Faker.seed()


def generated_customer():
    yield Customer(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        post_code=faker_en.postcode()
    )
