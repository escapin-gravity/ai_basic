import torch

x = torch.tensor([2.0, 3.0, 4.0], requires_grad=True)
print("x = ", x)
print("x.detach().numpy() = ", x.detach().numpy())

y = x ** 2
y.sum().backward(retain_graph=True)
print("y = ", y)
print("y.sum() = ", y.sum())
print("x.grad = ", x.grad)

x.grad.zero_()
y.backward(gradient=torch.ones_like(y))
print('x.grad = ', x.grad)

x.grad.zero_()
y = torch.tensor([-1.0, -2.0, -3.0], requires_grad=True)
z = x ** 2 + y ** 2
z.sum().backward() # z.sum()으로 스칼라 값으로 만들고 backward() 호출
print("z = ", z)
print("x.grad = ", x.grad)
print("y.grad = ", y.grad)