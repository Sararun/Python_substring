d = {}
dicts = {}
s = "abcabcbb"
for i, c in enumerate(s):
    d[c] = i
print(str(d))
for key, value in d.items():
    dicts.setdefault(value, set()).add(key)
result = [key for key, values in dicts.items() if len(values)>1]
print(result)


ы