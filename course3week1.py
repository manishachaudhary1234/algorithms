jobsFile = open('jobs.txt','r')
lines = jobsFile.readlines()[1:]

jobs = []
length,weight = 0,0

for line in lines:
    weight = int(line.split()[0])
    length = int(line.split()[1])
    jobs.append([weight,length,weight - length])

jobs = sorted(jobs,key = lambda x:(x[2],x[0]))
jobs = jobs[-1::-1]#inverse, decreasing order
sumTime = 0
sumLength = 0 
for job in jobs:
    sumLength += job[1]
    sumTime += job[0] * sumLength
print(sumTime)

