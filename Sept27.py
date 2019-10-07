def lookandsay(num):
    look = [1]
    for n in range(0,num):
        new_look = []
        count = 1
        prev = 0
        for m in range(len(look)-1,-1,-1):
            if prev == look[m]:
                count += 1
            else:
                new_look.append(count)
                new_look.append(look[m])
                count = 1
            prev = look[m]
        look = new_look
    return look

print lookandsay(2)

