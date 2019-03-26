def time_converter(time):
    import re
    hours = int(re.search(r'^..', time).group())
    if 10 <= hours < 12:
        time = time + ' a.m.'
    elif 0 < hours < 10:
        time = re.search(r'....$', time).group() + ' a.m.'
    elif hours == 0:
        time = re.sub(r'^00', '12', time) + ' a.m.'
    elif hours == 12:
        time = time + ' p.m.'
    else:
        time = re.sub(r'^..', str(hours - 12), time) + ' p.m.'
        
    return time