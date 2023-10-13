import os
from typing import Any, Optional, Tuple

import mlflow.pytorch
import pytorch_lightning as pl
from pytorch_lightning.utilities.types import STEP_OUTPUT
import torch
from mlflow import MlflowClient
import torch.nn.functional as F
import torch.nn as nn
from torch.utils.data import DataLoader
from torchmetrics.functional import accuracy
from torchvision import transforms
from torchvision.datasets import MNIST

class CIAModel(nn.Module):
    def __init__(self, features_dim: int, num_classes: int) -> None:
        super(CIAModel, self).__init__()
        self.features_dim = features_dim
        self.num_classes = num_classes
        self.linear1 = nn.Linear(features_dim, 16)
        self.linear2 = nn.Linear(16, num_classes)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        y = self.linear1(x)
        y = F.relu(y)
        return self.linear2(y)

class ClassificationWrapper(pl.LightningModule):
    def __init__(self, model: CIAModel):
        super(ClassificationWrapper, self).__init__()
        self.model = model
        self.num_classes = model.num_classes
        self.features_dim = model.features_dim
        
        self.save_hyperparameters()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)

    def training_step(self, batch: Tuple[torch.Tensor, torch.Tensor], batch_nb: int) -> float:
        x, y = batch
        logits = self(x.flatten(start_dim=1))
        loss = F.cross_entropy(logits, y)
        pred = logits.argmax(dim=1)
        acc = accuracy(pred, y, task='multiclass', num_classes=self.num_classes)

        # Enregistrer les métriques souhaitées avec le logger offert par PyTorch Lightning
        self.log("train_loss", loss, on_epoch=True)
        self.log("train_accuracy", acc, on_epoch=True)
        return loss
    
    def validation_step(self, batch: Tuple[torch.Tensor, torch.Tensor], batch_nb: int) -> None:
        x, y = batch
        logits = self(x.flatten(start_dim=1))
        loss = F.cross_entropy(logits, y)
        pred = logits.argmax(dim=1)
        acc = accuracy(pred, y, task='multiclass', num_classes=self.num_classes)

        # Enregistrer les métriques souhaitées avec le logger offert par PyTorch Lightning
        self.log("valid_loss", loss, on_epoch=True)
        self.log("valid_accuracy", acc, on_epoch=True)

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

if __name__ == '__main__':
    base_model = CIAModel(features_dim=28*28, num_classes=10)
    wrapped_model = ClassificationWrapper(base_model)

    # Récupération des données MNIST via torchvision
    train_dataset = MNIST(
        os.getcwd(), train=True, download=True, transform=transforms.ToTensor()
    )
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    
    test_dataset = MNIST(
        os.getcwd(), train=False, download=True, transform=transforms.ToTensor()
    )
    test_load = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # Initialiser le trainer de PyTorch Lightning
    trainer = pl.Trainer(max_epochs=20)

    # Auto log de MLflow avec PyTorch
    mlflow.pytorch.autolog()

    # Entrainer le modèle dans le contexte du logging de MLflow
    with mlflow.start_run() as run:
        trainer.fit(wrapped_model, train_loader, val_dataloaders=test_load)

    # fetch the auto logged parameters and metrics
    print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))