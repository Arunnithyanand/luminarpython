from functools import reduce
employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
     {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
     {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
]
# print employees name only
#
# for employee in employees:
#     print(employee["name"])
e_names=list(map(lambda emp:emp["name"],employees))
up_names=list(map(lambda name:name.upper(),e_names))
print(e_names)
print(up_names)
a_name=list(filter(lambda emp:emp["name"][0]=='a',employees))
print(a_name)
sal_emp=list(filter(lambda emp:emp["salary"]>23000,employees))
print(sal_emp)
developers=list(filter(lambda emp:emp["designation"]=="developer,",employees))
print(developers)
high_salary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                   list(map(lambda emp:emp["salary"],employees)))
print(high_salary)