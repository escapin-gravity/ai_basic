import torch

def f1(x):
    return x**2

def diff(f, x):
    """
    단일 변수 함수 f의 수치 미분 계산
    1. 전진 차분법: 빠르지만 상대적으로 부정확함
    2. 중간 차분법: 전진 차분법보다 정확도가 높음
    """
    h = 1e-7  
    # return (f(x + h) - f(x)) / h  # 전진 차분법
    return (f(x + h) - f(x - h)) / (2 * h)  # 중간 차분법


def f2(x):
    return torch.sum(x ** 2)

def gradient(f, x):
    """
    다변수 함수 f의 수치 그래디언트 계산
    - 각 차원별로 중간 차분법을 사용하여 미분 계산
    """
    h = 1e-6  
    grad = torch.zeros_like(x) 
    perturb = torch.eye(len(x)) * h  # 변화를 한 번에 적용하기 위한 행렬

    for i in range(len(x)):
        grad[i] = (f(x + perturb[i]) - f(x - perturb[i])) / (2 * h)

    return grad


if __name__ == "__main__":
    # 단일 변수 수치 미분
    x = 3.0
    result_diff = diff(f1, x)
    print(f"f1({x})의 수치 미분 결과: {result_diff}")

    # 다변수 함수의 그래디언트 계산 
    x_multi = torch.tensor([1.0, 2.0, 3.0], requires_grad=False)
    result_grad = gradient(f2, x_multi)
    print(f"f2({x_multi.tolist()})의 그래디언트: {result_grad}")