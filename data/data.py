from dataclasses import dataclass


@dataclass
class Customer:
    first_name: str = None
    last_name: str = None
    post_code: str = None