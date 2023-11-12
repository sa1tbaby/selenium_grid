import pandas
from pandas import DataFrame
"""



test1 = [1,2,3]
teset2 = [6,7,8,9,0]
teset3 = [[6,7,1,9,0], [6,7,8,9,0], [6,7,8,3,0]]

for ii, kk in enumerate(test1):

    status = True
    val = teset3[ii]
    for i, j in enumerate(teset2):

        if j != val[i]:
            status = False
            break

    if not status:
        continue

    print(kk)



sss = pandas.read_excel('test.xlsx', index_col=0)
for i in sss.iterrows():
    j = i[1]
    print(j.iloc['locator_type'])
    print()

"""
class Base:
    def tt1(self):
        print(1)

class Derived(Base):

    def tt1(self):
        print(2)




d = Derived()
b: Base = d
b.s
print(1)

