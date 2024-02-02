VarList1=[]
VarList2=[]
VarTotal=[]


VarNum=int(input("Please enter the Total Number of  elements you want in list:"))
print("Please enter the values of the First & Second Lisr:")
for j1 in range(1, VarNum+1):
 VarL1=int(input("Please enter the %d Element value of List1:" %j1))
 VarList1.append(VarL1)

 VarL2=int(input("Please enter the %d Element Value of List2:" %j1))
 VarList2.append(VarL2)

for j1 in range(VarNum):
 VarTotal.append(VarList1[j1]+VarList2[j1])

print("The sum of two list is:", VarTotal)


 