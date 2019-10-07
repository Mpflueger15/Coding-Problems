def witnesses(heights):
    saw = []
    for x in heights[::-1]:
        if len(saw)==0 or x > saw[len(saw)-1]:
            saw.append(x)
    return len(saw)

print witnesses([3, 6, 3, 4, 1, 2, 1])