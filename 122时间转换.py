#!/usr/bin/env python
# coding=utf-8

t = int(input())

# 如果 t 等于 0，直接输出 "00:00:00 am"
if t == 0:
    formatted_time = "00:00:00 am"
else:
    # 计算小时、分钟、秒数
    hours = t // 3600
    minutes = (t % 3600) // 60
    seconds = t % 60

    # 根据规则输出时间格式
    if hours < 12:
        if hours == 0:
            hours = 12
        time_period = "am"
    elif hours == 12:
        time_period = "midnoon"
    else:
        hours -= 12
        time_period = "pm"

    # 格式化输出
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d} {time_period}"

print(formatted_time)
