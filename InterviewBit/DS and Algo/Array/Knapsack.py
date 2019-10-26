# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:35:36 2018

@author: Sunil Angadi
"""
def knapsack(profit_array,capaity):
    max_profit=0
    p_array=sorted(profit_array)
    for i in range(0,len(p_array)):
        if(p_array[i]<capacity):
            max_profit=max_profit+p_array[i]
    return max_profit
            

if __name__=='__main__':
    print("Enter the profit values in a list")
    # to read elements like this way 23 44 30 12 16
    profit_array=list(map(int,input().split()))
    print("Enter the capacity of the Knapsack")
    capacity=int(input())
    max_profit=knapsack(profit_array,capacity)
    max_tasks=0
    print("Maximum Number of tasks : %s ,Maximun amount of profit :%s" %(max_tasks,max_profit))
    