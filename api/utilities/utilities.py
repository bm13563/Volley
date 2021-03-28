from datetime import datetime

def str_to_date(date_time_str):
    return datetime.strptime(date_time_str, '%Y%m%d%H%M')