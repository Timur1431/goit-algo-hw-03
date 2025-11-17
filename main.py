from datetime import datetime, date

def get_days_from_today(date: str):
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None

    today = date.today()
    diff = today - target_date
    return diff.days