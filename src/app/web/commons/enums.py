from enum import Enum

class GroupTypeEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value.lower() == value.lower():
                return member
            
    Trip = "trip"
    Home = "home"
    Couple = "couple"
    Other = "other"

class SplitTypeEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):   
        for member in cls:
            if member.value.lower() == value.lower():
                return member
            
    Equal = "equal"
    Unequal = "unequal"
    Percentage = "percentage"
    Adjustment = "adjustment"
    