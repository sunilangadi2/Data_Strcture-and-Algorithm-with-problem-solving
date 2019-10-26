''' An efficient solution is to use Greedy approach. 
	The basic idea of the greedy approach is to 
	calculate the ratio value/weight for each item 
	and sort the item on basis of this ratio. 
	Then take the item with the highest ratio 
	and add them until we can’t add the next item as a whole 
	and at the end add the next item as much as we can. 
	Which will always be the optimal solution to this problem.'''


# Python3 program to solve fractional 
# Knapsack Problem 
class ItemValue: 
	
	"""Item Value DataClass"""
	def __init__(self, wt, val, ind): 
		self.wt = wt 
		self.val = val 
		self.ind = ind 
		self.cost = val // wt 

	def __lt__(self, other): 
		return self.cost < other.cost 

# Greedy Approach 

class FractionalKnapSack: 
	
	"""Time Complexity O(n log n)"""
	@staticmethod
	def getMaxValue(wt, val, capacity): 
		
		"""function to get maximum value """
		iVal = [] 
		for i in range(len(wt)): 
			iVal.append(ItemValue(wt[i], val[i], i)) 
		
		# sorting items by value 
		iVal.sort(reverse = True) 

		totalValue = 0
		for i in iVal: 
			curWt = int(i.wt) 
			curVal = int(i.val) 
			if capacity - curWt >= 0: 
				capacity -= curWt 
				totalValue += curVal 
			else: 
				fraction = capacity / curWt 
				totalValue += curVal * fraction 
				capacity = int(capacity - (curWt * fraction)) 
				break
		return totalValue 

# Driver Code 
if __name__ == "__main__": 
	wt = [10, 40, 20, 30] 
	val = [60, 40, 100, 120] 
	capacity = 50

	maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity) 
	print("Maximum value in Knapsack =", maxValue) 

