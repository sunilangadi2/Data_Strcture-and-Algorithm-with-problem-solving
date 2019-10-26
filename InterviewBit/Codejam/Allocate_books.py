'''N number of books are given. 
The ith book has Pi number of pages. 
You have to allocate books to M number of students 
so that maximum number of pages alloted to a student is minimum. 
A book will be allocated to exactly one student. 
Each student has to be allocated at least one book. 
Allotment should be in contiguous order, for example: 
A student cannot be allocated book 1 and book 3, skipping book 2.

NOTE: Return -1 if a valid assignment is not possible

Input:

List of Books
M number of students
Your function should return an integer corresponding to the minimum number.

Example:

P : [12, 34, 67, 90]
M : 2

Output : 113

There are 2 number of students. Books can be distributed in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. 

'''

class Solution:
    def numberOfStudents(self, A, pages):
        count = 0
        students = 1
        for i in range(len(A)):
            count += A[i]
            if count > pages:
                count = A[i]
                students += 1
        return students

    def books(self, A, M):
        if M > len(A):
            return -1
        min_pages = max(A)
        max_pages = sum(A)
        while(min_pages < max_pages):
            mid = int((min_pages + max_pages) / 2)
            if self.numberOfStudents(A, mid) > M:
                min_pages = mid + 1
            else:
                max_pages = mid
        return min_pages

s=Solution()
print(s.books([12, 34, 67, 100],4))