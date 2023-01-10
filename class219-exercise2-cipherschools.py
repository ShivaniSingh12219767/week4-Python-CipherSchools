with open("week4-Python-CipherSchools/salary.txt","r") as rf:
    with open("week4-Python-CipherSchools/output.txt","a") as wf:
        for line in rf.readlines():
            name,salary=line.split(",")
            wf.write(f'{name}\'s salary is {salary}')