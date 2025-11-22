from datetime import datetime, date

def get_days_from_today(date: str):
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None

    target_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    diff = today - target_date
    return diff.days

print (get_days_from_today("2025-11-11"))
