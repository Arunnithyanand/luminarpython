# import re
# x="a{2}" # a include group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
# x="a?" # a include group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#
# import re
# x="a{2,3}" # a include group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
# x="a{1,3}" # a include group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x="^a" # a include group
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re
x="a$" # a include group
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
