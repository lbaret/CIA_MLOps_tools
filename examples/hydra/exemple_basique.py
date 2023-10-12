import hydra
from omegaconf import DictConfig

@hydra.main(version_base=None, config_path="config", config_name="config")
def run(cfg : DictConfig) -> DictConfig:
    # Le code doit obligatoirement se situer ici. L'encapsulation par le décorateur empêche un quelconque return.
    print(cfg)
    
    
if __name__ == "__main__":
    run()
