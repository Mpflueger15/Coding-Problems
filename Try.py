def lookandsay(num):
    look=[1]

    for n in range (0,num):
        new_look = []
        count = 1
        for m in range(0,len(look)):
            try:
                if look[m+1] == look[m]:
                    count += 1
                else:
                    new_look.append(count)
                    new_look.append(look[m])
                    count = 1
            except IndexError:
                if len(look)<2:
                    new_look=[1]
        look = new_look
    return look

print lookandsay(3)