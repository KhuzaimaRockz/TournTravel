from datetime import date
from datetime import datetime


def error_handle(error_code):
    error_desc = open('errors.txt', 'r')  # Opening existing list of errors

    EL = error_desc.readlines()
    for EC in EL:
        if str(error_code) == EC[:3]:  # Splicing Error code to Match Error code with existing errors
            ED = EC[4::]  # Splicing Error code to only get Error detail
            break
    else:
        ED = 'Unknown Error'

    error_desc.close()

    # Error logging part
    log_file = open('error_log.txt', 'a')  # Opening existing log file

    today = date.today() # getting the current days date
    timern = datetime.now() # getting the current time

    current_date = today.strftime("%d/%m/%Y")  # Formatting as dd/mm/YYYY
    current_time = timern.strftime("%H:%M:%S") # Formatting as H:M:S

    log_write = f"{current_date} {current_time} ERROR:{error_code} - {ED}" # Formatting Error Log
    
    log_line = ''

    for log_word in log_write:  # converting tuple to string without changing format
        log_line = log_line + str(log_word)

    log_file.write(log_line + '\n')  # Writing into Log File
    log_file.close()
# END: Utility Functions