def convert_time(start_time, end_time):
    start_ls = list(start_time)
    if len(start_time) == 5:
        None
    elif len(start_time) == 4:
        start_ls.insert(0, 0)
    start = float(start_ls[0])*10 + float(start_ls[1]) + (float(start_ls[3])*10 + float(start_ls[4]))/60

    
    end_ls = list(end_time)
    if len(end_time) == 5:
        None
    elif len(end_time) == 4:
        end_ls.insert(0, 0)
    end = float(end_ls[0])*10 + float(end_ls[1]) + (float(end_ls[3])*10 + float(end_ls[4]))/60

    return [start, end]

def convert_day(day):
    day = day.lower()
    if day == 'monday':
        num = 0
    elif day == 'tuesday':
        num = 1
    elif day == 'wednesday':
        num = 2
    # useless func
    return None

        
