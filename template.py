import os


dirs = [
    "source_data",
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",  # For creating DVC pipelines
    "params.yaml",  # For storing all parameters
    ".gitignore",
    os.path.join("src", "__init__.py"),
    "README.md",
    "LICENSE",
]

for file_ in files:
    with open(file_, "w") as f:
        pass
