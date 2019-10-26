'''In this Kata, you will be given a number in form of a string 
   and an integer k and your task is to insert k commas into the string 
   and determine which of the partitions is the largest.
	For example:
	solve('123',1) = 23 because we insert one comma and get the substrings ('1','23') or ('12',3). The max of these is '23'.
	solve('1234',1) = 234 because ('1','234') or ('12','34') or ('123','4').
	solve('1234',2) = 34 because ('1','2','34') or ('1','23','4') or ('12','3','4'). 
	solve('1234',3) = 4.'''

def solve(st,k):
    c=len(st)-k
    return int(max(st[i:i+c] for i in range(k+1)))

print(solve("98761234578987",5))