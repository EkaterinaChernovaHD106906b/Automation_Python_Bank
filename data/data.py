from dataclasses import dataclass


@dataclass
class Customer:
    first_name: str = None
    last_name: str = None
    post_code: str = None


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    address: str = None
    city: str = None
    state: str = None
    zipcode: str = None
    phone: str = None
    ssn: str = None
    user_name: str = None
    password: str = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
