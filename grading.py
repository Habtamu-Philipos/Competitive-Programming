def gradingStudents(grades):
    rslt =[]
    for i in range(len(grades)):
        nxt_mult = grades[i]//5 + 1
        sbtrct= nxt_mult * 5
        diff = sbtrct - grades[i]
        if grades[i] >= 38 and diff < 3:
            rslt.append(sbtrct)
        else: rslt.append(grades[i])
    return rslt  
