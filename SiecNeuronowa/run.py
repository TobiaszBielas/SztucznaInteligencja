import torch
from torch import nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from matplotlib import pyplot as plt
import sys


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # layer initialization
        self.fc1 = nn.Linear(28*28, 400)
        self.fc2 = nn.Linear(400, 200)
        self.fc3 = nn.Linear(200, 100)
        self.fc4 = nn.Linear(100, 50)
        self.fc5 = nn.Linear(50, 10)

    def forward(self, x):
        # flatten image input
        x = x.view(x.size(0), -1)
        # relu activation function
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = nn.functional.relu(self.fc3(x))
        x = nn.functional.relu(self.fc4(x))
        x = self.fc5(x)
        return nn.functional.log_softmax(input=x, dim=1)


try:
    epochs = int(sys.argv[1])
except:
    epochs = 5
# initialize the neural network model
model = Net()

# stochastic gradient descent optimicer
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
# loss function
criterion = nn.NLLLoss()

# data set
batch_size = 32
transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
training_collection = datasets.MNIST('data', train=True, download=True, transform=transform)
training_collection = DataLoader(training_collection, batch_size=batch_size, shuffle=True)
testing_collection = datasets.MNIST('data', train=False, download=True, transform=transform)
testing_collection = DataLoader(testing_collection, batch_size=batch_size, shuffle=True)

training_loss = []
training_success = []
testing_loss = []
testing_success = []
current_epoch = []

print(f"Start: {epochs}-epochs")
# main loop
for epoch in range(epochs):
    losses = []
    successes = []
    # training loop
    for image, target in training_collection:
        optimizer.zero_grad()
        result = model.forward(image)
        loss = criterion(result, target)
        model.zero_grad()
        loss.backward()
        optimizer.step()
        successes.append(target.eq(result.detach().argmax(dim=1)).float().mean())
        losses.append(loss.item())

    training_loss.append(torch.tensor(losses).mean())
    training_success.append(round(float(torch.tensor(successes).mean()) * 100, 2))
    print(f"Epoch: {epoch+1} || training loss: {training_loss[-1]:.3f}")
    print(f"Epoch: {epoch+1} || training success: {training_success[-1]}%")

    print("================================================================")
    # testing loop
    losses = []
    successes = []
    for image, target in testing_collection:
        with torch.no_grad():
            result = model.forward(image)
        loss = criterion(result, target)
        successes.append(target.eq(result.detach().argmax(dim=1)).float().mean())
        losses.append(loss.item())
        
    testing_loss.append(torch.tensor(losses).mean())
    testing_success.append(round(float(torch.tensor(successes).mean()) * 100, 2))
    print(f"Epoch: {epoch+1} || testing loss: {testing_loss[-1]:.3f}")
    print(f"Epoch: {epoch+1} || testing success: {testing_success[-1]}%")

    print("================================================================")
    current_epoch.append(epoch+1)
    

plt.subplot(2, 2, 1)
plt.xlabel("Epoch")
plt.ylabel("Success rate (%)")
plt.title("Training success rate")
plt.plot(current_epoch, training_success)

plt.subplot(2, 2, 3)
plt.xlabel("Epoch")
plt.ylabel("Loss rate")
plt.title("Training loss rate")
plt.plot(current_epoch, training_loss)

plt.subplot(2, 2, 2)
plt.xlabel("Epoch")
plt.ylabel("Success rate (%)")
plt.title("Testing success rate")
plt.plot(current_epoch, testing_success)

plt.subplot(2, 2, 4)
plt.xlabel("Epoch")
plt.ylabel("Loss rate")
plt.title("Testing loss rate")
plt.plot(current_epoch, testing_loss)

plt.show()