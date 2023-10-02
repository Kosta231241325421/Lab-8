#lab 8.1
def pidrahuemo(sym):
    pidrahuemo = {}
    for hell in sym:
        if hell in pidrahuemo:
            pidrahuemo[hell] +=1
        else:
            pidrahuemo[hell] =1
    return pidrahuemo
sym=input("Введіть символи  ")
res=pidrahuemo(sym)
for hell, peace in res.items():
    print(f"'{hell}'= {peace}")