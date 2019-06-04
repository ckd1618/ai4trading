import re

def compute(str, regex):
  str_lower = str.lower()
  list1=re.findall(regex,str_lower)
  return list1

str = "how many 5 chucks did a wood chuck chuck if a wood chuck could chuck wood 5 times!"
# regex = r'(\w*) '
# regex = r'(\w*)\W*'
# regex = r'\b\w+\b'
regex = r'\w+\d*'

items = compute(str, regex)

counts =dict()
for i in items:
  counts[i] = counts.get(i,0)+1

print(regex)
print(counts)

