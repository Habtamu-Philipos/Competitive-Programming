def countingValleys(steps, path):
    paths = list(path)
    count = 0
    res=0
    for i in range(steps):
        if paths[i] == "D" and  count== 0 : res +=1 
        if paths[i] == "U": count += 1
        if paths[i] =="D": count -=1
    return res
