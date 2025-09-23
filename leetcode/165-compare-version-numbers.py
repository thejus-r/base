def compareVersion(version1: str, version2: str) -> int:

    vs1, vs2 = version1.split("."), version2.split(".")
    l1, l2 = len(vs1), len(vs2)

    for i in range(max(l1, l2)):
        v1 = int(vs1[i]) if i < l1 else 0
        v2 = int(vs2[i]) if i < l2 else 0

        if v1 < v2: return -1
        if v1 > v2: return 1

    return 0


print("Example 1:",compareVersion("1.0", "0.1"))
print("Example 1:",compareVersion("7.5.2.4", "7.5.3"))
print("Example 1:",compareVersion("0.1", "0.001"))