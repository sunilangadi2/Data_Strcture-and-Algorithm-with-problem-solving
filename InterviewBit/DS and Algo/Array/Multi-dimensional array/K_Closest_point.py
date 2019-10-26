'''We have a list of points on the plane.  
Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the
 Euclidean distance.)

You may return the answer in any order.  
The answer is guaranteed to be unique 
(except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, 
so the answer is just [[-2,2]].'''

"""Solution 1:
	Sort the points by distance, then take the closest K points.
	In Python, we sort by a custom key function - namely, 
	the distance to the origin. Afterwards, we return the first
	K elements of the list.
"""
def kClosest(src,points, K):
    points.sort(key = lambda P: (src[0]-P[0])**2 + (src[1]-P[1])**2)
    return points[:K]
#input(src_point,other_points,k)
print(kClosest([-5,-5],[[-16, -5], [-1, 2], [-4, -3], [10, -2], [0, 3]],3))