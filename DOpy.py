import numpy as np

seq1 = input("Please input sequence A:")
seq2 = input("Please input sequence B:")
seq1, seq2 = list(seq1), list(seq2)
seqall = seq1+seq2
seqall = list(set(seqall))
seqall.sort()
m,n=len(seq1),len(seq2)
space = len(seqall)
weight = np.ones((space,space))*666
gap = int(input("Please input gap cost:"))
for i in range(space):
	for j in range(space):
		if weight[i,j]==666:
			prompt = "Please input weight for"+' '+str(seqall[i]).upper()+' '+"to"+' '+str(seqall[j]).upper()+" :"
			weight[i,j]= input(prompt)
			weight[j,i] = weight[i,j]
		else:
			continue
result = np.zeros((m+1,n+1))
for i in range(m+1):
	result[i,0]=i*gap 
for j in range(n+1):
	result[0,j]=j*gap 

for i in range(m):
	for j in range(n):
		mindex = seqall.index(seq1[i])
		nindex = seqall.index(seq2[j])
		compare = weight[mindex,nindex]
		situation = [result[i,j]+compare,result[i,j+1]+gap,result[i+1,j]+gap]
		result[i+1,j+1]=max(situation)
print("\n\nAnswer is below:")
print("0      gap",end='    ')
for i in range(n):
	print(seq2[i],end="    ")
print("\ngap",end="   ")
print(result[0,:])
for i in range(m):
	print(seq1[i],end="     ")
	print(result[i+1,:])
