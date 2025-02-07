import numpy as np
import random

##task-1 
# vector=np.arange(10,50)
# print(vector)

##task-2 
# matrix=np.arange(0,9).reshape(3,3)
# print(matrix)

# #task-3
# Identity_matrix=np.eye(3)
# print(Identity_matrix)

# #task-4
# Random_matrix=np.random.randn(3,3,3)
# print(Random_matrix)

# #task-5
# Rand_matrix=np.random.randn(10,10)
# find_max=Rand_matrix.max()
# find_min=Rand_matrix.min()
# print(Rand_matrix)
# print(find_max)
# print(find_min)

# #task-6
# Rand_vec=np.random.randn(30)
# print(Rand_vec)
# mean=Rand_vec.mean()
# print(mean)

# #task-7
# Norm_matrix=np.random.randint(0,100,(5,5))
# min_val=Norm_matrix.min()
# max_val=Norm_matrix.max()
# normalized_matrix=(Norm_matrix-min_val)/(max_val-min_val)
# print(Norm_matrix)
# print(normalized_matrix)

# #task-8
# first_matrix=np.random.randn(5,3)
# second_matrix=np.random.randn(3,2)
# multiply=first_matrix@second_matrix
# print(first_matrix,second_matrix,multiply)

# #task-9
# first_matrix=np.random.randn(3,3)
# second_matrix=np.random.randn(3,3)
# dot_product=np.dot(first_matrix,second_matrix)
# print(first_matrix,second_matrix,dot_product)

# #task-10
# matrix=np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ])
# matrix_transpose=matrix.T
# print(matrix_transpose)

# #task-11
# matrix=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]    
# ])
# matrix_det=np.linalg.det(matrix)
# print(matrix_det)

##task-12
# matrix_1=np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]   
# ])
# matrix_2=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12]
# ])
# matrix_product=np.dot(matrix_1,matrix_2)
# print(matrix_product)

# #task-13
# matrix=np.random.randn(3,3)
# vector=np.array([[1],[2],[3]])
# matrix_vector=np.dot(matrix,vector)
# print(matrix_vector)

##task-14
# A=np.array([
#     [2,1,-1],
#     [-3,-1,2],
#     [1,2,3]
# ])
# b=np.array([8,-11,3])
# x=np.linalg.solve(A,b)
# print(x)

##task-15
# matrix=np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ])
# row_wise=np.sum(matrix,axis=1)
# col_wise=np.sum(matrix,axis=0)
# print(f"Row_wise: {row_wise}")
# print(f"Column_wise: {col_wise}")