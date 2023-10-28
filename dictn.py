# d={'name':'shivu'
#    'age' : 22
#    'name':shivu}
# print(d)


# def getLetterCount(s):
#     counts={}
#     for letter in s:
#         if letter in counts:
#             counts[letter]+=1
#         else:
#             counts[letter]=1
#         #print(counts)
#     return counts
# print(getLetterCount("abbbccdddeea"))



def getInfo():
    name=input("Enter name\n")
    age=int(input("Enter age\n"))
    salary=int(input("Enter salary\n"))
    return {'name':name,
            'age':age,
            'salary':salary}
#res=getInfo()
#print(res)


def loadData(num):
    people=[]
    for i in range(num):
        print(f"Enter person {i+1} data")
        d=getInfo()
        people.append(d)
    return people
# data=loadData(3)
# print(data)

def minAgePerson(people):
    minPerson=people[0]
    for p in people[1:]:
        if p['age']<minPerson['age']:
            minPerson=p
    return minPerson

def minSalaryPerson(people):
    minPerson=people[0]
    for p in people[1:]:
        if p['salary']<minPerson['salary']:
            minPerson=p
    return minPerson

def main():
    num_people=int(input("Enter num of people\n"))
    people=loadData(num_people)
    option=input("Enter choice A: min age person, S: min salary\n ")
    if option=='A':
        #p=minAgePerson(people)
        p=min(people,key=lambda d:d['age'])
        print(p)

    if option=='S':
        p=minSalaryPerson(people)
        print(p)

main()

def getAge(d):
    return d['age']

 