import re

rrn = '\\b(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1])).[1-4][0-9]{6}\\b'
pn = '([a-zA-Z]{1}|[a-zA-Z]{2})\d{8}'



regexp_list = [rrn,pn]

result_li =[]

for regexp in regexp_list:
    p = re.compile(regexp)
    result = p.findall("980323-1224518 \n PP22415643")
    result_li.append(result)

print(result_li)