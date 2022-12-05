
from datetime import datetime as dt


def result_log(data, result):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    with open('log.csr', 'a') as file:
        file.write('{} data: {}: result: {}\n'
                   .format(time, data, result))
