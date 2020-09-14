# slicing
def append(strr1,strr2):
    n = int(len(strr1) / 2)
    res = strr1[: n] + strr2 + strr1[n:]
    return res


print(append("Darkseid","Thanos"))
