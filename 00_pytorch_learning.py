# -*- coding: utf-8 -*-
"""00_pytorch_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14eqMUC3ECUlK-NfeV0_oWVDGBqnwHdDP
"""

import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

!nvidia-smi

scalar=torch.tensor(7)
scalar

scalar.ndim

scalar.item()

vector=torch.tensor([2,2])
vector

vector.shape
vector.ndim

#matrix
MATRIX=torch.tensor([[7,8],
                     [9,10]])

MATRIX.ndim

MATRIX.shape
MATRIX[1]

TENSOR = torch.tensor([[[1,2,3],
                        [3,6,9],
                        [2,4,5]]])

print(TENSOR.ndim)
print(TENSOR.shape)
print(TENSOR[0])

"""**Random Tensor**"""

random_tensor=torch.rand(3,4)
random_tensor

random_tensor=torch.rand(10,10,10)

random_image_tensor=torch.rand(size=(224,224,3))
random_image_tensor.shape,random_image_tensor.ndim

random_image_tensor=torch.rand(size=(3,224,224))
random_image_tensor.shape,random_image_tensor.ndim

random_tensor=torch.rand(size=(3,3))
zeros=torch.zeros(size=(3,3))
zeros * random_tensor
ones=torch.ones(size=(3,3))

ones.dtype

## Creating range of tensor USE arange as deprecated
torch.range(0,10)

one_to_ten= torch.arange(1,11)

A=torch.arange(start=0,end=10,step=1)
A

#create Tensor Like
ten_zeros=torch.zeros_like(input=one_to_ten)
ten_zeros

"""# Dealing with DataTypes"""

float_32_tensor=torch.tensor([3.0,4.0,9.0],
                              dtype=None)
float_32_tensor.dtype #Default

float_16_tensor=torch.tensor([3.0,4.0,9.0],
                              dtype=torch.float16)
float_16_tensor.dtype

A=torch.tensor([3.0,4.0,9.0],
               dtype=None,
               device="cpu",# or "cuda",#which devices on which tensor preseny
               requires_grad=False)#whether or not track gradients on this device
               
A

#Convert into another data type
B=A.type(torch.float16)
B

A * B

print(f"Datatype of tensor : {A.dtype}")
print(f"Size of tensor : {A.size}")
print(f"Shape of tensor : {A.shape}")
print(f"Device on which tensor exists : {A.device}")

"""# Manipulating Tensors"""

# addition,subtraction,multiplication,division
x = torch.tensor([1,2,3])
print(x+10)
print(x*10)
print(x/10)

#Tensor Inbuilt function
Y= torch.mul(x,10)
print(Y)
Z= torch.add(x,20)
print(Z)

#  Multiplication- elementwise or Matrix multiplication (dot prodcut)
print(A*A) # element wise
#or
print(A,"*",A) # element wise
print(f"Equals: {A*A}")
torch.matmul(A,A)# Matrix Multiplication
A@A# Matrix Multiplication

# Commented out IPython magic to ensure Python compatibility.
# %%time
# torch.matmul(A,A)# Matrix Multiplication

# Commented out IPython magic to ensure Python compatibility.
# %%time
# value=0
# for i in range(len(A)):
#   value+=A[i]*A[i]
# print(value)

"""**Shape Error**"""

torch.matmul(torch.rand(3,2),torch.rand(3,2)) #error

torch.matmul(torch.rand(3,2),torch.rand(2,2))

torch.rand(3,2)@torch.rand(2,2)

"""More to Shape error"""

# Shapes for Matrix multiplication'
tensor_A=torch.tensor([[1,2],
                      [3,4],
                      [5,6]])
tensor_B=torch.tensor([[7,10],
                      [3,4],
                      [5,6]])
torch.mm(tensor_A,tensor_B) #error

torch.mm(tensor_A,tensor_B.T) # No error as transpose is used

tensor_B.T.shape

"""## Find the mean max and sum of tensor (Tensor aggregation)"""

x=torch.arange(0,100,10)
print(torch.max(x))
print(torch.min(x))
print(torch.sum(x))

print(torch.mean(x)) #Error

print(torch.mean(x.type(torch.float32)))
#or
print(x.type(torch.float32).mean())

"""**Finding the position of min and max**"""

x=torch.arange(1,100,10)
x

x.argmin()

x.argmax()

"""# **Reshaping, Stacking, Squeezing,view,Unsqueezing and Permute**
1.  **View** - Return a view of an input tensor of certain shape but keep the same memory as the manin tensor
2.    **Stacking** - Combine Multiple tenosr on top of each other  (vstack) or  side by side (hstack)
3.  **Squeeze** - Removes all 1 dimensions from a tensor
4.  **Unsqueeze** - Add a one dimensions to tensor
5.  **Permute** - Return a view of the input with dimensions permuted or swapped in a certain way








"""

x=torch.arange(1.,10.)
x,x.shape

# Add an extra dimensions
x_reshape=x.reshape(9,1)
x_reshape,x_reshape.size

# Add an extra dimensions
x_reshape=x.reshape(3,3)
x_reshape,x_reshape.size

# change the view
z=x.view(1,9)
z,z.shape

# Changing z changes x as both share same memory
z[:,0]=5
x,z

x_stacked=torch.stack([x,x,x,x],dim=1)
x_stacked

x_stacked=torch.stack([x,x,x,x],dim=0)
x_stacked

# Torch.squeeze Remove 1 dimensions
x_reshape=x_reshape.reshape(1,9)
x_reshape,x_reshape.shape,x_reshape.squeeze()

x_squeezed=x_reshape.squeeze()

x_reshape.squeeze().shape

# unsequeeze Add Extra  dimension
x_unsqueezed=x_squeezed.unsqueeze(dim=0)
x_unsqueezed,x_unsqueezed.shape

# unsequeeze Add Extra  dimension
x_unsqueezed1=x_squeezed.unsqueeze(dim=1)
x_unsqueezed1,x_unsqueezed1.shape

#Permute
x_original=torch.rand(2,3,5)
x.size()

x_original=torch.rand(size=(224,224,3)) #[height,width,channels]
x_original.size()
# permute to rearrange the axis
x_permuted=x_original.permute(2,0,1)#shifts 0 ->1 ,1->2,2->0
x_permuted.size(),x_original.size()

x_original[0,0,0]=879
x_original[0,0,0],x_permuted[0,0,0]# same memory as view

"""# **Indexing Selecting data from tensors**
Same as Numpy
"""

x=torch.arange(1,10).reshape(1,3,3)
x,x.shape

x[0] #inside first bracket

x[0][0] #dim=1

x[0][0][0] #last dimension

x[1][1][1] # Error

x[0][1][1]

x[:,0]

x[:,:,1]

# Get all value of zero dimension but only the 1 index value of 1st and 2nd dimension
x[:,1,1],x[0,1,1]

x[0,0,:]

#index to return 9
print(x[0,2,2])
print(x[0][2][2])



# index to retrn 3,6 and 9
print(x[0,:,2])
print(x[:,:,2])
print(x[0,:,2].shape)
print(x[:,:,2].shape)

"""# **Pytorch and Numpy**


*  Data in numpy want in pytorch torch.from_numpy(ndarray)
*   Data in torch want in Numpy torch.Tensor.numpy()



"""

# Pytorch and numpy
import numpy as np
array=np.arange(1.0,8.0) # Dfault Datatype Float64
tensor=torch.from_numpy(array)
array,array.dtype,tensor,tensor.dtype

import numpy as np
array=np.arange(1.0,8.0) # Dfault Datatype Float64
tensor=torch.from_numpy(array,dtype=torch.float32)# Error
array,array.dtype,tensor,tensor.dtype

import numpy as np
array=np.arange(1.0,8.0) # Dfault Datatype Float64
tensor=torch.from_numpy(array).type(torch.float32) # No error
array,array.dtype,tensor,tensor.dtype

# change the value of array
import numpy as np
array=np.arange(1.0,8.0) # Dfault Datatype Float64
array=array+1
array,array.dtype,tensor,tensor.dtype

# Tensor to Numpy Array
tensor=torch.ones(7)
numpy_tensor=tensor.numpy()
tensor,numpy_tensor

tensor=torch.ones(7)
tensor=tensor+1
tensor,numpy_tensor