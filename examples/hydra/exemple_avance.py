from dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, OmegaConf

@dataclass
class ExperienceConfig:
    nom_modele: str = MISSING
    poids: str = MISSING
    epoques: int = MISSING
    taux_apprentissage: float = MISSING
    optimiseur: str = MISSING
    perte: str = MISSING

@dataclass
class MembreConfig:
    prenom: str = MISSING
    nom: str = MISSING
    id: int = MISSING

@dataclass
class ProjetConfig:
    nom: str = MISSING
    git: str = MISSING

@dataclass
class Config:
    experience: ExperienceConfig = MISSING
    membre: MembreConfig = MISSING
    projet: ProjetConfig = MISSING

cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)

@hydra.main(version_base=None, config_path="config", config_name="config")
def my_app(cfg: Config) -> None:
    config = OmegaConf.to_object(cfg)
    print(config.experience)
    print(config.membre)
    print(config.projet)

if __name__ == "__main__":
    my_app()