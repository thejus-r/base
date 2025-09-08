from typing import List
def readBinaryWatch(turnedOn: int) -> List[str]:
    output = []
    for h in range(12):
        for m in range(60):
            temp = bin(h) + bin(m)
            if turnedOn == temp.count("1"):
                time = "%d:%02d"% (h,m)
                output.append(time)

    return output

print("Example 1: ", readBinaryWatch(1))