from enum import Enum

class GroupTypeEnum(str, Enum):
    
    Trip = "trip"
    Home = "home"
    Couple = "couple"
    Other = "other"