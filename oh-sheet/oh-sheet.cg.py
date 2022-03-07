b26,sp,sh,c=lambda a:sum([("ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i)+1)*(26**j)for j,i in enumerate(a[::-1])])-1,lambda c:[False if i.isalpha() else True for i in c].index(True),__import__("json").load(open("oh-sheet.json","r")),input().split("!")
for i in sh:
    if c[0]==i["name"]:print(f"{i['cells'][int(c[1][sp(c[1]):])-1][b26(c[1][:sp(c[1])])]}")
