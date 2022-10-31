import utils.database as dab
from config import *


def convert_time(seconds: int) -> str:
    if seconds < 60:
        return f"{round(seconds)} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{round(minutes)} minutes"
    hours = minutes / 60
    return f"{round(hours)} hours"
