VarList1=[]
VarList2=[]
Varadd=[]
Varsub=[]
Varmul=[]
Vardiv=[]
Varmod=[]
Varexpo=[]

vari=0
varj=0

VarNum=int(input("please enter the total number of element in list:"))
print("Please enter the values for First and Second List")

while(vari<VarNum):
 Varl1=int(input("Please enter %d Element value of List1:"% varj))
 VarList1.append(Varl1)

 Varl2=int(input("Please enter %d Element value of List2:" %varj))
 VarList2.append(Varl2)

 vari=vari+1
while(varj<VarNum):
 Varadd.append(VarList1[varj]+VarList2[varj])
 Varsub.append(VarList1[varj]-VarList2[varj])
 Varmul.append(VarList1[varj]*VarList2[varj])
 Vardiv.append(VarList1[varj]/VarList2[varj])
 Varmod.append(VarList1[varj]%VarList2[varj])
 Varexpo.append(VarList1[varj]**VarList2[varj])
 varj=varj+1

print("The Values of List after Addition=",Varadd)
print("The Values of List after Substraction=",Varsub)
print("The Values of List after Multiplication=",Varmul)
print("The Values of List after Division=",Vardiv)
print("The Values of List after Modulus=",Varmod)
print("The Values of List after Exponent=",Varexpo)


 