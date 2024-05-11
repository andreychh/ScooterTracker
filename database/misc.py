from enum import Enum

from sqlalchemy.orm import DeclarativeBase


class ScooterState(Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'


class Base(DeclarativeBase):
    pass


# utils
def camel_to_snake(name: str) -> str:
    result = [name[0].lower()]
    for char in name[1:]:
        if char.isupper():
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
