import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)
z = x ** 2 + y ** 2
z.backward()

print("x = ", x)
print("y = ", y)

print("x.grad = ", x.grad)
print("y.grad = ", y.grad)
