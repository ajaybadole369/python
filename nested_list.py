li = [['Harry', 37.21], ['Berry', 37.26], ['Tina', 38.2], ['Akriti', 41], ['Harsh', 39]]
x=sorted(li)
print(x)
ls=[37.21,37.21,37.2,41,39]
y=sorted(set(ls))[1]
print(y)
for i ,j in x:
    if y==j:
        print(i)




