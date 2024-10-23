# Написать функцию, которая принимает объект datetime
# и возвращает номер недели.

from datetime import datetime 

def get_week_num(date) -> int:
  return date.isocalendar()[1]

print(get_week_num(datetime(2025,10,1,12)))

