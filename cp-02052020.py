def to_hex(n):
    hx = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hxdict = dict(enumerate(hx))
    stack = []
    num = ''
    while n>0:
    	stack.append(n%16)
    	n = n//16
    while len(stack) > 0:
    	num += hxdict[stack.pop()]
    return num
print(to_hex(123))
# 7B
