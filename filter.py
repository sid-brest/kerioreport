import os
from datetime import datetime

def select_rows_with_sid(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'SID' in line:
                line = line.replace('SID', 'Струневский')
                date_str = line.split('[')[1].split(']')[0]
                date = datetime.strptime(date_str, '%d/%b/%Y %H:%M:%S')
                month_name = date.strftime('%m')
                year = date.strftime('%Y')
                report_file = f'{month_name}_{year}.txt'
                with open(report_file, 'a') as output_file:
                    output_file.write(line)

file_path = 'debug.log.txt'  
select_rows_with_sid(file_path)