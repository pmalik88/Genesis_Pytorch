# -*- coding: utf-8 -*-
"""01_pytorch_learning

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_yqlFh7aW2n8DzAhP3B075qwWPlDwVna

# Reproducibility (trying to take random out of random)
"""

import torch
random_tensor_A=torch.rand(3,4)
random_tensor_B=torch.rand(3,4)
print(random_tensor_A)
print(random_tensor_B)
print(random_tensor_A==random_tensor_B)

import torch
# Set the random seed
Random_seed = 42
torch.manual_seed(Random_seed)
random_tensor_A=torch.rand(3,4)
random_tensor_B=torch.rand(3,4)
print(random_tensor_A)
print(random_tensor_B)
print(random_tensor_A==random_tensor_B)

import torch
# Set the random seed
Random_seed = 42
torch.manual_seed(Random_seed)
random_tensor_A=torch.rand(3,4)
torch.manual_seed(Random_seed)
random_tensor_B=torch.rand(3,4)
print(random_tensor_A)
print(random_tensor_B)
print(random_tensor_A==random_tensor_B)

import torch
# Set the random seed
torch.manual_seed(42)
random_tensor_A=torch.rand(3,4)
torch.manual_seed(42)
random_tensor_B=torch.rand(3,4)
print(random_tensor_A)
print(random_tensor_B)
print(random_tensor_A==random_tensor_B)

"""# Running tensors and Pytorch Objects on GPU for faster computations"""

### Getting a GPU use tim Dettmers
# Use google colab, AWS,AZURE
!nvidia-smi

### Check for GPU access for Pytorch
import torch
torch.cuda.is_available()

# Set up device agnostic code
device="cuda" if torch.cuda.is_available() else "cpu"
device

torch.cuda.device_count()

## Putting Tenosrs and models on GPU for faster computations
tensor=torch.tensor([1,2,3])
print(tensor,tensor.device)

# Move tensor on GPU
tensor_on_gpu=tensor.to(device)
print(tensor_on_gpu,tensor.device)

"""### Move tensor back to CPU
#If tensor on GPU , we can not transform it to Numpy
# put Sensor back to CPU and then transorm to Numpy
"""

tensor_on_gpu.numpy() # error

tensor_back_on_cpu=tensor_on_gpu.cpu().numpy()
print(tensor_back_on_cpu)

"""Excercises and **Extracurriculam**
https://www.learnpytorch.io/00_pytorch_fundamentals/#exercises
"""

import torch
torch.__version__