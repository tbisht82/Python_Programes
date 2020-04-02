def MaxReducedString(s):
    data = []
    i = 0
    length = len(s)
    while i < length:
        if len(data) != 0 and data[-1] == s[i]:
            i = i + 1
            data.pop(-1)
        else:
            data.append(s[i])
            i = i + 1
    n = "".join(data)
    if n == "":
        return "Empty String"
    else:
        return n


rm = MaxReducedString("abaabaccddd")
print(rm)
