s = 'Hello world Мир'
sb = s.encode('utf-8')
print(sb)
print(type(sb))

b = 'Hello world'
bb = b.encode('ascii')
print(bb)
print(type(bb))

s = sb.decode('utf-8')
print(s)
print(type(s))


b = bb.decode('ascii')
print(b)
print(type(b))