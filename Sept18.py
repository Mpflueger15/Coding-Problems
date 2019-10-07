def merge(intervals):
  result = []
  for start, end in sorted(intervals, key=lambda i: i[0]):
    # If current interval overlaps with the previous one, combine them
    print start, end
    result.append(start)


print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]