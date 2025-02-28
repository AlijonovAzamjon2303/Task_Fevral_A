def son(s):
    s = s.strip()
    if "01" in s.strip("0") and "10" in s.strip("0"):
        print("No")
    else:
        print("YES")


s = input().strip()
son(s)
