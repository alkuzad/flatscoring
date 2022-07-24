import yaml
from yaml import Loader
from pathlib import Path

def load_settings(settings_path: Path):
    return yaml.load(settings_path.open().read(), Loader=Loader)