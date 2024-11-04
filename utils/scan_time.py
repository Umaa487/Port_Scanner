import datetime

def time_status():
    curr_time = datetime.datetime.now()

    formatted_curr_time = curr_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_curr_time