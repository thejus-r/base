from sortedcontainers import SortedList
def main():
    l = [3,2,1,0,8,5,3,1,4,7,2,1,0]
    sl = SortedList(l)
    print(sl)

    idx = sl.bisect_right(1)
    print("Bisect Right", idx)
    idx = sl.bisect_left(1)
    print("Bisect Left", idx)
    idx = sl.bisect_right(10)
    print("Bisect Right", idx, "length", len(sl))
    return

main()