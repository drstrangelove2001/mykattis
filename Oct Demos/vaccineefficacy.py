N = int(input())
A = [input() for i in range(N)]
arrVacc = [item for item in A if item[0] == 'Y']
arrVA,arrVB,arrVC = [[x[i] for x in arrVacc] for i in range(1,4)]
infVA = len(list(filter(lambda x:x=='Y',arrVA)))/len(arrVacc)
infVB = len(list(filter(lambda x:x=='Y',arrVB)))/len(arrVacc)
infVC = len(list(filter(lambda x:x=='Y',arrVC)))/len(arrVacc)

arrNVacc = [item for item in A if item[0] == 'N']
arrNA,arrNB,arrNC = [[x[i] for x in arrNVacc] for i in range(1,4)]
infNA = len(list(filter(lambda x:x=='Y',arrNA)))/len(arrNVacc)
infNB = len(list(filter(lambda x:x=='Y',arrNB)))/len(arrNVacc)
infNC = len(list(filter(lambda x:x=='Y',arrNC)))/len(arrNVacc)

ansA = (infNA - infVA)/infNA if infNA !=0 else 0
ansB = (infNB - infVB)/infNB if infNB !=0 else 0
ansC = (infNC - infVC)/infNC if infNC !=0 else 0

print(round(ansA*100,6) if ansA>0 else 'Not Effective')
print(round(ansB*100,6) if ansB>0 else 'Not Effective')
print(round(ansC*100,6) if ansC>0 else 'Not Effective')
