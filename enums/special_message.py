from enum import Enum


class SpecialMessage(str, Enum):
    ORDER = 'success'
    CHECK = 'error'
