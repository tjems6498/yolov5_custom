import torch

x = torch.arange(8).view(2, 2, 2)
print(x)

print(x.flip(0))
print(torch.flip(x,[0,1]))
