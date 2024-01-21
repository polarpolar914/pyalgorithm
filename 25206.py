import sys
input = sys.stdin.readline
n = 20
gpa = 0
credits = 0
gpa_map = { "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0 }
for i in range(n):
    line = input().rstrip()
    line = list(line.split())
    if line[2] == "P": continue
    credits += float(line[1])
    gpa += float(line[1]) * gpa_map[line[2]]
print("%.6f" % (gpa / credits))

