from datetime import datetime
from random import choice

IMAGES = [
    "https://media.licdn.com/dms/image/D5610AQGfki8DlgCSxA/image-shrink_800/0/1706659203997?e=1707562800&v=beta&t=XBbwf3NudCzDVjb2ElXicvPBsKk_fZOhI-pXbbN8d9s",
    "https://media.licdn.com/dms/image/D5610AQE5QAP54sqBew/image-shrink_800/0/1706608908468?e=1707562800&v=beta&t=krO25r5vYt1hhKv011KyS2li-zGOjCP0ST5vgIp28vk",
    "https://media.licdn.com/dms/image/D5610AQEHbUGSMIxS_g/image-shrink_800/0/1706522427063?e=1707562800&v=beta&t=_ZBNtuuncM2wjpW_smMC752KyGDC5QUg4ykk4wId00Y",
    "https://media.licdn.com/dms/image/D4E10AQHbyLXZzlRalA/image-shrink_800/0/1706572873262?e=1707562800&v=beta&t=LuQ0YASFTFveJSiM25OmdpN3mIgoMhbMW9ASV4V2-40",
    "https://media.licdn.com/dms/image/D4E10AQHuGhPPR4_Thw/image-shrink_800/0/1705988140353?e=1707562800&v=beta&t=6JplB5_O2jXpnEVlWLXd8Lq6thFO2shetqkXrFcMJ2E",
]


def get_random_image_link():
    return choice(IMAGES)


def hours_diff(start_time: datetime, end_time: datetime) -> int | float:
    time_diff = end_time - start_time
    return time_diff.total_seconds() / 3600
