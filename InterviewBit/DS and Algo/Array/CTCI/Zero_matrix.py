''' Zero Matrix: In any M X N Matrix if any element is set to zero,
	then set it's corresponding row and coumn also zero

	Time: O(M X N) 

	Solution:
	1. Check if first row and first column have any zero
	   then set the variable RowHasZero and ColumnHasZero
	2. Iterate through the rest of the matrix by setting
	   matrix[i][0] and matrix[0][i] to zero if there's a Zero
	   in the matrix[i][j]
	3. iterate through rest of the matrix by nullifying row i
	   if there's a zero in the matrix[i][0] 
	4. iterate through rest of the matrix by nullifying column j
	   if there's a zero in the matrix[0][j]
	5. Nullify the first row and first column based on the variable
	   RowHasZero and ColumnHasZero.
'''

def zero_matrix(matrix):
	RowHasZero=False
	ColumnHasZero=False
	n=len(matrix)
	print(n)
	# check if first row has zero
	for j in range(0,n):
		if matrix[0][j]==0:
			RowHasZero=True
			break

	# check if first column has zero
	for i in range(0,n):
		if matrix[i][0]==0:
			ColumnHasZero=True
			break

	# check for zero in the rest of the array
	for i in range(1,n):
		for j in range(1,n):
			if matrix[i][j]==0:
				matrix[i][0]=0
				matrix[0][j]=0

	# nullify row based on the value in first column
	for i in range(1,n):
		if matrix[i][0]==0:
			for j in range(0,n):
				matrix[i][j]=0

	# nullify column based on value in first row
	for j in range(1,n):
		if matrix[0][j]==0:
			for i in range(0,n):
				matrix[i][j]=0
	
	# nullify first row
	if RowHasZero:
		for j in range(0,n):
			matrix[0][j]=0

	# nullify first column
	if ColumnHasZero:
		for i in range(0,n):
			matrix[i][0]=0

	return matrix

data=  [ [1, 2, 3, 4, 0],
	    [6, 0, 8, 9, 10],
		[11, 12, 13, 14, 15],
		[16, 0, 18, 19, 20],
		[21, 22, 23, 24, 25]]

print(zero_matrix(data))


