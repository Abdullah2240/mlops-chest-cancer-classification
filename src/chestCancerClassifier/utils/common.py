import os
from box import ConfigBox, BoxValueError
from chestCancerClassifier import logger
import yaml
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    "Read Yaml file, Takes file path and return the ConfigBox"
        
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    "Creates a list of directories, very simple"
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    "Loaded a binary file from a path and return the content of the file"
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data

@ensure_annotations
def save_bin(data: Any, path: Path):
    "Saves binary file, give it data to sace and hte file path to save it to  and it will save that daat in a binary file at that path"

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def get_size(path: Path) -> Any:
    "get the size in KB, takes path to file and return the size in KB"
    size_in_kb = round(os.path.getsize(path//1024))
    return f"~ {size_in_kb} KB"

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    "Load a json file takes the file path to a json file and return the contents of that file in ConfigBox format"

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file successfully loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_json(path: Path, data: dict):
    "Saves a json json data to a file"

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved to {path}")

@ensure_annotations
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    