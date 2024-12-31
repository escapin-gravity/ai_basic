import torch

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
print(f"x = {x}, y = {y}")

y.retain_grad()
y.backward()  # dy/dx
print(f"x.grad = {x.grad}")  # dy/dx, x.grad = 4
print(f"y.grad = {y.grad}")  # dy/dy

x.grad.zero_() # x.grad = 0


'''
x는 사용자가 직접 생성한 리프 텐서라 기울기가 기본적으로 저장되지만, 
y와 z는 연산 결과로 생성된 비리프 텐서라 retain_grad()를 호출해야 기울기가 저장되고 유지됩니다.
'''
z = x ** 3
z.retain_grad()
z.backward()
print(f"x.grad = {x.grad}")  # dz/dx, x.grad = 12
print(f"z.grad = {z.grad}")  # dz/dz

