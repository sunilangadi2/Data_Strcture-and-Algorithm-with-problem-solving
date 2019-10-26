#include<iostream>
#include<limits.h>
using namespace std;

void print_util(int A[], int B[], int m, int n, int i, int j, int k, int buffer[], int temp)
{
	
	if(k==m+n || i==m || j==n)
	return;
	if(A[i]<temp)
	print_util(A,B, m, n, i+1, j, k, buffer, temp);
    else if(B[j]<A[i])
	print_util(A,B,m, n, i, j+1, k, buffer, temp);
	else
	{
	buffer[k]= A[i];
	buffer[k+1]= B[j];
	for(int p=0; p<k+2; p++)
	cout<<buffer[p]<<" ";
	cout<<endl;
	temp = B[j];
	print_util(A,B,m,n,i+1,j+1, k+2,buffer, temp);
	}
}


void print(int A[], int B[], int m, int n)
{
	int buffer[m+n];
	for(int i=0; i<m; i++)
	for(int j=0; j<n; j++)
	if (A[i] < B[j] )
	print_util(A,B,m,n,i,j,0,buffer, -INT_MAX);

}

int main()
{
	printf("starts");
	int A[]= {10,15,25};
	int B[]={1,5,20,30};
	print(A,B,3,4);	
	return 0;
}