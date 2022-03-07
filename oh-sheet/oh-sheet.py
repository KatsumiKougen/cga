#!/usr/bin/env python3
import json

b26 = lambda alp: sum([("ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i) + 1) * (26 ** j) for j, i in enumerate(alp[::-1])]) - 1

separator = lambda coord: [False if i.isalpha() else True for i in coord].index(True)

with open("oh-sheet.json", "r") as f:
    sheet = json.load(f)

# DEBUGGING SECTION
for s in sheet:
    print(f"Current sheet: {s['name']}\n")
    for i, col in enumerate(s["cells"]):
        for j, row in enumerate(col):
            print(f"Column {i}, row {j}: {row}")
    print()
# END OF DEBUGGING SECTION

cmd = input("Command: ").split("!")
for col in sheet:
    if cmd[0] == col["name"]:
        print(b26(cmd[1][:separator(cmd[1])]), int(cmd[1][separator(cmd[1]):])-1)
        print(f"{col['cells'][int(cmd[1][separator(cmd[1]):])-1][b26(cmd[1][:separator(cmd[1])])]}")
        
