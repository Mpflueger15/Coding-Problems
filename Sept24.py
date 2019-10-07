def capacity(arr):
    peak=True
    puddles=0
    max_value=0
    for i in arr:
        new_max = max(i, max_value)
        print new_max, i, max_value
        if new_max >= max_value:
            if not peak:
                puddles+=1
                peak = True
            max_value = new_max
        else:
            peak = false
    return puddles

print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# 6