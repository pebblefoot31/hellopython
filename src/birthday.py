sent = 'Happy birthday to you! Happy birthday to you!'
s = sent.split()
print(s)

d = {}

for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)
