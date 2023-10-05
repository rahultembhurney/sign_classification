import os
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    root_dir: Path


@dataclass
class PrepareBaseModelConfig():
    root_dir: Path
    base_model_path: Path
    updated_model_path: Path

