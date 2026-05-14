from datetime import datetime


def GetDay(date: datetime):
    dayInt = date.weekday()
    day = ""
    match dayInt:
        case 0:
            day = "Senin"
        case 1:
            day = "Selasa"
        case 2:
            day = "Rabu"
        case 3:
            day = "Kamis"
        case 4:
            day = "Jumat"
        case 5:
            day = "Sabtu"
        case 6:
            day = "Minggu"

    return day