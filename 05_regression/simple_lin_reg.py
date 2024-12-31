import torch
import torch.optim as optim
import torch.nn.functional as F
import matplotlib.pyplot as plt


train_size = 12
torch.manual_seed(42)

x = torch.arange(train_size, dtype=torch.float)
t = torch.arange(train_size, dtype=torch.float)
t += torch.randn_like(t)

w = torch.tensor(0.5, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

optimizer = optim.Adam(params=[w, b], lr=0.01)
loss_fn = torch.nn.MSELoss()
loss_li = []

EPOCHS = 10
for epoch in range(EPOCHS):
    y = w * x + b
    loss = loss_fn(y, t)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    loss_li.append(loss.item())

print(f"w = {w.item()}")
print(f"b = {b.item()}")

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].set_title("Loss")
axs[0, 0].plot(loss_li)
axs[0, 0].set_xlabel('Epochs')
axs[0, 0].set_ylabel('Loss')

axs[0, 1].set_title(f"Linear Regression: $y = {w.item():.2f}x + {b.item():.2f}$")
axs[0, 1].scatter(x.numpy(), t.numpy(), label="Data")
x_vals = torch.linspace(-1.0, 10.0, steps=51)
y_vals = w * x_vals + b
axs[0, 1].plot(x_vals.numpy(), y_vals.detach().numpy(), 'b-', label="Fit Line")
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('t')
axs[0, 1].legend()

axs[1, 0].set_title(f"Linear Regression: $y = {w.item():.2f}x + {b.item():.2f}$")
axs[1, 0].scatter(x.numpy(), t.numpy(), label="Data")
axs[1, 0].plot(x_vals.numpy(), y_vals.detach().numpy(), 'r-', label="Regression Line")
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('t')
axs[1, 0].legend()

axs[1, 1].set_title("Predicted vs Actual")
axs[1, 1].scatter(t.numpy(), (w * x + b).detach().numpy())
axs[1, 1].plot([min(t), max(t)], [min(t), max(t)], 'k--')
axs[1, 1].set_xlabel('True t')
axs[1, 1].set_ylabel('Predicted t')

plt.tight_layout()
plt.show()
