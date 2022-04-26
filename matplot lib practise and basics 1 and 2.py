# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:29:20 2022

@author: sriharsha
"""
#1. Basic Plotting techniques using mAtplot lib

# =============================================================================

# import numpy as np
# import matplotlib.pyplot as plt
# N = 16
# x = np.linspace(0, 15, N)
# x = np.arange(6)
# a = [[1,2,3,4,6,8,9],[9,10,4,5,4,8,9],[7,8,9,6,5,4,2]]
# d = np.random.randn(6)
# # =============================================================================
# # 
# # y = np.geomspace(0.1, 2000, N)
# # print(y)
# # =============================================================================
# # =============================================================================
# # plt.plot(x, y, 'o--')
# # =============================================================================
# plt.plot(x,4**x)
# plt.plot(x,5**x)
# plt.plot(x,5.5**x)
# #plt.plot(x,d)
# plt.show()
# #help(np.linspace)
# #help(plt.plot)
# #print(np.logspace(0.1,2, 16))
# =============================================================================






#2. Grids and labeling axes


# =============================================================================
# 
# #Enabling the grid in visualization
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(6)
# plt.plot(x,x**2)   #1
# plt.plot(x,x**4)    #2
# plt.plot(x,x**3)    #3
# #
# 
# #plt.plot(x,x**2,x,x**4,x,x**3) --> short cut for 1 2 and 3 
# 
# plt.grid(True)  # to use grid in our graph
# #plt.savefig('test.png')  # to savre the figure we created in current directory
# 
# #print(plt.axis())
# # =============================================================================
# # #gives the axis in console #method 1
# # 
# # #plt.axis([0,6,-8,10])
# # #The statement plt.axis([0, 2, -8, 0]) sets the values of the axes. The first pair,
# # # (0, 2), refers to the limits for the x-axis, and the second pair, (-8, 0),
# # # refers to the limits for the y-axis.
# # 
# # =============================================================================
# # =============================================================================
# # # method 2 for setting axis
# # #Using  xlim() and ylim() 
# # plt.xlim([0,2])
# # plt.ylim([0,8])
# # plt.show()
# # 
# # 
# # =============================================================================

# # adding title and respective labels to the graph
# plt.xlabel('sriharsha')
# plt.xlim([0,4])
# plt.ylabel('job rate')
# plt.ylim([0,8])
# plt.title('success rate')
# 
# # we can also give legends for different colours
# #plt.legend(['1','2','3'])
# 
# #we can also set up the location of legend
# 
# plt.legend(['1','2','3'],loc = "lower right")
# plt.show()
# 
# 
# 
# 
# 
# =============================================================================




