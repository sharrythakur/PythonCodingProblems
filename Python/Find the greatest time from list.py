li= [1,2,9,9]
li1=[]
for i in range(0,len(li)):
  for j in range(0,len(li)):
      for k in range(len(li)):
         for l in range(len(li)):
           if i != j and i != k and i != l and j != k and j != l and k != l:
               if (li[i]*10 + li[j]) < 24 and (li[k]*10 + li[l]) < 60:
                  li1.append(str(li[i]) + str(li[j]) + ":" + str(li[k]) + str(li[l]))

print(li1[-1])
