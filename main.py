import time
def sumdiffsq(number, leftnum, rightnum):
	return ((number - leftnum)**2 + (number - rightnum)**2)
def moveindex(index, nL, iL, rightLeft, optimalDiff):
	#rightLeft is 1 if we should move to right, 0 if we should move to left
	#print("HERE!")
	indexcpy = iL[index] #the index of numsList we are looking at
	if rightLeft == 1:
		while (indexcpy < iL[index + 1]):
			if (nL[iL[index + 1]] - nL[indexcpy] < nL[indexcpy] - nL[iL[index - 1]]): #if right distance becomes less than left distance
				#print("indexcpy " + str(indexcpy))
				break
			indexcpy += 1
		if indexcpy == iL[index + 1]:
			indexcpy -= 1
			if indexcpy == iL[index]:
				return(0)
			iL[index] = indexcpy
			#print("here 1")
			return (1)
		else: #if broke because right dist. became less than left dist.
			if (sumdiffsq(nL[indexcpy], nL[iL[index + 1]], nL[iL[index - 1]]) <= sumdiffsq(nL[indexcpy - 1], nL[iL[index + 1]], nL[iL[index - 1]])):
				iL[index] = indexcpy
				#print(indexcpy)
				#print("Here 2")
				return (1)
			else: #if right dist becoming less increased the error,  reduce by 1
				indexcpy -= 1
				if indexcpy == iL[index]:
					return (0)
				else:
					iL[index] = indexcpy
					#print("Here 3")
					return (1)

	elif rightLeft == 0:
		while (indexcpy > iL[index - 1]):
			if (nL[indexcpy] - nL[iL[index - 1]] < nL[iL[index + 1]] - nL[indexcpy]): #if left distance becomes less than right distance
				break
			indexcpy -= 1
		if (indexcpy == iL[index - 1]):
			indexcpy += 1
			if indexcpy == iL[index]:
				return(0)
			iL[index] = indexcpy
			return (1)
		else: #if broke because left dist. becamse more than right dist.
			if (sumdiffsq(nL[indexcpy], nL[iL[index + 1]], nL[iL[index - 1]]) > sumdiffsq(nL[indexcpy - 1], nL[iL[index + 1]], nL[iL[index - 1]])):
				iL[index] = indexcpy
				return (1)
			else: #if left dist becoming less increased the error,  increase by 1
				if indexcpy + 1 == iL[index]:
					return (0)
				else:
					iL[index] = indexcpy + 1
					return (1)
	return (1)

def optimalSubsample(numslist, N):
	assert(N >= 1 and len(numslist) >= 1) #should we allow for 0 len lists? How can we take N out of 0 a length list?
	if N == 1:
		return(numslist[0])
	finallist = [numslist[0], numslist[len(numslist) - 1]]
	if N == 2:
		return (finallist)
	if N == len(numslist):
		return (numslist)
	diff = []
	for i in numslist:
		listtoadd = []
		for j in numslist:
			listtoadd.append(abs(j - i))
		diff.append(listtoadd)

	optimalDiff = (numslist[len(numslist) - 1] - numslist[0]) / (N - 1)
	ilist = [0, len(numslist) - 1] #this list includes indexes we are considering - we always have ends
	for i in range(1, N - 1):
		ilist.append(i)
	ilist.sort()
	#print(ilist)
	change = -1
	while(change != 0):
		change = 0
		for i in range(1,len(ilist) - 1):
			#print(ilist)
			left = True
			right = True
			if ilist[i] - ilist[i - 1] == 1:
				left = False
			if ilist[i + 1] - ilist[i] == 1:
				right = False
			rightleftdifference = diff[ilist[i]][ilist[i + 1]] - diff[ilist[i]][ilist[i - 1]]
			#print(rightleftdifference, right, left, diff[ilist[i]][ilist[i+1]])
			if rightleftdifference > 0 and right:
				change += moveindex(i, numslist, ilist, 1, optimalDiff)
			elif rightleftdifference < 0 and left:
				change += moveindex(i, numslist, ilist, 0, optimalDiff)
			print(ilist)
		print()
		time.sleep(1)
		#print(change)
			#print(ilist, change)
	finallist = []
	for i in ilist:
		finallist.append(numslist[i])
	return (finallist)

def meansquareerror(currlist, listofoptdistance):
	#finds mean square error 
	listofdiff = []
	for i,j in zip(currlist, currlist[1:]):
		listofdiff.append(j - i)
	meansquareerror = 0
	for i,j in zip(listofdiff, listofoptdistance):
		meansquareerror += ((j - i) ** 2)
	meansquareerror /= len(listofdiff)
	return (meansquareerror)



def recursiveMethod(currlist, candidates, N, include, vectorofoptdistance):
	#currlist is the subset of initial list we are creating
	#candidates is numbers we can add to currlist
	#N is number of numbers we need to have in final list
	#include is 1 if we should add the next candidate and 0 if we should not
	if (len(currlist) == N):
		currlist.sort()
		return([meansquareerror(currlist, vectorofoptdistance), currlist])
	elif (len(candidates) + len(currlist) < N):
		return ([-1,[]]) #if you cannot get N members 
	else:
		newvalue = candidates.pop(0)
		a = currlist[:]
		if include == 1:
			a.append(newvalue)
		first = recursiveMethod(a[:], candidates[:], N, 1, vectorofoptdistance)
		second = recursiveMethod(a[:], candidates[:], N, 0, vectorofoptdistance)
		if first[0] == -1:  #if -1, not enough members, so pick other result
			return (second)
		elif second[0] == -1:
			return (first)
		elif first[0] <= second[0]: 
			return (first)
		else:
			return (second)

def optimalSubsampleTrees(nums, N):
	#finds most evenly spaced N numbers by minimizing mean square error between successive differences and optimal distance: (distance between ends) / (N - 1)
	assert(N >= 1 and N <= len(nums))
	if N == 1:
		return ([nums[0]])
	elif N == 2:
		return ([nums[0], nums[len(nums) - 1]])
	elif N == len(nums):
		return (nums)
	else:
		startinglist = [nums[0], nums[len(nums) - 1]]
		candidates = nums[1:len(nums) - 1]
		optimalDistance = (nums[len(nums) - 1] - nums[0])/(N - 1) #creating a repeating list of the optimal distance, which is (distance between ends) / (N - 1)
		listofoptdistance = []
		for i in range(N - 1):
			listofoptdistance.append(optimalDistance)
		a = recursiveMethod(startinglist,candidates[:], N, 1, listofoptdistance)
		b = recursiveMethod(startinglist,candidates[:], N, 0, listofoptdistance)
		if a[0] == -1:
			return (b[1])
		elif b[0] == -1:
			return (a[1])
		elif a[0] <= b[0]:
			return (a[1])
		else:
			return (b[1])
listtocheck = list(range(100))
num = 5
begin = time.time()
print(optimalSubsample(listtocheck, num))
end = time.time()
print(end - begin)
#begin = time.time()
#print(optimalSubsampleTrees(listtocheck, num))
#end = time.time()
#print(end - begin)



