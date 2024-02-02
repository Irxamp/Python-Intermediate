VarList1=[]
VarList2=[]
VarTotal=[]
vari=1
varj=0
VarNum=int(input("Please enter the Total number of the List Elements you want"))
print("Please enter the items of Firs&Second List")
while(vari<=VarNum):
 Varl1=int(input("Value of %d Element of List1:"%vari))
 VarList1.append(Varl1)

 Varl2=int(input("Va;ue of %d Element of List2;"%vari))
 VarList2.append(Varl2)
 
 vari=vari+1
while(varj<VarNum):
 VarTotal.append(VarList1[varj]+VarList2[varj])
 varj=varj+1

print("The sum of two list is:", VarTotal)


 