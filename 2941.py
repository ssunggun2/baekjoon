import re
s=input()
s=re.sub(r"dz=",'0',s)
s=re.sub(r'c-','0',s)
s=re.sub(r'c=','0',s)
s=re.sub(r'd-','0',s)
s=re.sub(r'lj','0',s)
s=re.sub(r'nj','0',s)
s=re.sub(r's=','0',s)
s=re.sub(r'z=','0',s)
print(len(s))