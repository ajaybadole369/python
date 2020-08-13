# def FindIntersection(strArr):
strArr=["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]     
  # code goes here
arr1=strArr[0].split(', ')
print(arr1)
arr2=strArr[1].split(', ')
print(arr2)
ls=[value for value in arr1 if value in arr2]
print(','.join(ls))




  # return ','.join(ls)
  # return ls

# keep this function call here 
# print(FindIntersection(input('enter string ')))
