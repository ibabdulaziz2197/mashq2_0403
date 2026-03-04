# 5
def ruxsat(yosh):
    if yosh >= 18:
        return "Ruxsat berildi"
    else:
        return "Ruxsat berilmadi"

res = (ruxsat(19))
print(res)


res1 = (ruxsat(15))
print(res1)


# 6
def raqam(son):
    if son > 0:
        return "Nol"
    else:
        return "Nol emas"


res = (raqam(0))
print(res)

res1 = (raqam(1))
print(res1)

# 8
def a(parol):
    if parol < 8:
        return "Juda qisqa"
    else:
        return "Qabul qilndi"

res = a(5)
print(res)

res1 = a(10)
print(res1)

# 10
def son(a):
    if a > 20:
        return "Oraliq"
    else:
        return "Oraliq emas"

res = son(11)
print(res)

res1 = son(21)
print(res1)
