from enum import Enum

class GroupTypeEnum(str, Enum):
    
    Trip = "trip"
    Home = "home"
    Couple = "couple"
    Other = "other"

class SplitTypeEnum(str, Enum):

    Equal = "equal"
    Unequal = "unequal"
    Percentage = "percentage"
    Adjustment = "adjustment"
    