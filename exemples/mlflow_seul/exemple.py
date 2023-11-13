import random

from mlflow import log_metric, log_param, start_run

# Contrairement à l'exemple de MLFlow avec Pytorch Lightning, je vous demande un peu d'imagination !
EPOCHS = 100
LEARNING_RATE = 0.01
WEIGHT_DECAY = 0.95


with start_run() as r:
    log_param('epochs', EPOCHS)
    log_param('learning_rate', LEARNING_RATE)
    log_param('weight_decay', WEIGHT_DECAY)
    
    # Boucle d'entrainement
    for i in range(EPOCHS):
        # Les batchs ont fini
        
        log_metric('train_accuracy', random.random())
        log_metric('train_loss', random.random())
        log_metric('valid_accuracy', random.random())