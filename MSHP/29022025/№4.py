
alph = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alph[:17]:
    if (int(f"9759{x}", 17) + int(f"3{x}108", 17)) % 11 == 0:
        print((int(f"9759{x}", 17) + int(f"3{x}108", 17)) // 11)
        break
