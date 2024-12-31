---
### Gradient의 개념
다변수 함수 \( f(x) \)의 gradient는 함수의 편미분으로 구성된 **gradient vector**입니다. 이를 \(\nabla f(x)\)로 표현하며, 다음과 같은 의미를 가집니다:

- \( \nabla f(x) \): 함수 \( f(x) \)가 \( x \) 위치에서 변화가 가장 큰 방향과 크기를 나타냅니다.

### 자동 미분 (Autograd)
PyTorch의 신경망에서는 계산 그래프(Computation Graph)를 구성하고, **Chain Rule**을 사용하여 자동으로 미분을 계산합니다. 자동 미분은 다음 메서드로 수행할 수 있습니다:

1. **`Tensor.backward()`**  
   - Back-propagation에서 필요한 계산 그래프의 역방향 미분을 수행합니다.
2. **`torch.autograd.grad()`**  
   - 특정 Tensor에 대한 gradient를 직접 계산합니다.

### 자동 미분 사용 조건
1. **`requires_grad` 설정**  
   - Tensor를 생성할 때 `requires_grad=True`로 설정해야 gradient가 계산됩니다.
   
   ```python
   x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
   ```

2. **계산 그래프와 관련된 메서드**:
   - `detach()`: 계산 그래프에서 Tensor를 분리합니다.
   - `numpy()`: Tensor를 NumPy 배열로 변환합니다.
   - `retain_grad()`: 중간 노드의 gradient를 유지하려면 호출해야 합니다.

---

### 예제 코드

```python
import torch

# Tensor 생성과 requires_grad 설정
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x**2 + 3*x + 4

# Backward 호출
y.sum().backward()

# Gradient 확인
print("Gradient:", x.grad)
```

---

### 주요 개념
#### 1. Gradient
\[
\nabla f(x) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)
\]

#### 2. Chain Rule
\[
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial y} \cdot \frac{\partial y}{\partial x}
\]

#### 3. Backward
\[
\text{Tensor.backward()} \implies \text{자동으로 } \nabla f(x) \text{ 계산}
\]