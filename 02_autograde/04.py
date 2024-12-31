import torch

x = torch.tensor([2.0, 3.0, 4.0], requires_grad=True)

y = x.sum()
print(f"y = {y}")

y.backward()
print("x.grad = ", x.grad)


z = x.mean()
print("z = ", z)

x.grad.zero_()
z.backward()
print("x.grad = ", x.grad)


x.grad.zero_()
w = (x ** 2).mean()
print("w = ", w)

w.backward()
print("x.grad = ", x.grad)