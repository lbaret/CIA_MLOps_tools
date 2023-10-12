import os
from typing import Tuple

import mlflow.pytorch
import pytorch_lightning as pl
import torch
from mlflow import MlflowClient
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torchmetrics.functional import accuracy
from torchvision import transforms
from torchvision.datasets import MNIST


class MNISTModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)

    def forward(self, x: torch.Tensor):
        y = self.linear(x.view(x.size(0), -1))
        return torch.relu(y)

    def training_step(self, batch: Tuple[torch.Tensor, torch.Tensor], batch_nb: int):
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        pred = logits.argmax(dim=1)
        acc = accuracy(pred, y, task='multiclass', num_classes=10)

        # Enregistrer les métriques souhaitées avec le logger offert par PyTorch Lightning
        self.log("train_loss", loss, on_epoch=True)
        self.log("acc", acc, on_epoch=True)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.02)


def print_auto_logged_info(r):
    tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
    print(f"run_id: {r.info.run_id}")
    print(f"artifacts: {artifacts}")
    print(f"params: {r.data.params}")
    print(f"metrics: {r.data.metrics}")
    print(f"tags: {tags}")

mnist_model = MNISTModel()

# Récupération des données MNIST via torchvision
train_ds = MNIST(
    os.getcwd(), train=True, download=True, transform=transforms.ToTensor()
)
train_loader = DataLoader(train_ds, batch_size=32)

# Initialiser le trainer de PyTorch Lightning
trainer = pl.Trainer(max_epochs=20)

# Auto log de MLflow avec PyTorch
mlflow.pytorch.autolog()

# Entrainer le modèle dans le contexte du logging de MLflow
with mlflow.start_run() as run:
    trainer.fit(mnist_model, train_loader)

# fetch the auto logged parameters and metrics
print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))