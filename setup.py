from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]

style_packages = ["black==22.3.0", "isort==5.10.1", "pylint==2.15.10"]

test_packages = []

# Define our package
setup(
    name="simple-project",
    version="0.1.0",
    description="Simple Project Showing The Usage of DVC.",
    author="Chinedu Ezeofor",
    author_email="neidu@email.com",
    url="https://github.com/chineidu/DVC-Tutorial",
    python_requires=">=3.8",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages + test_packages + ["pre-commit==2.19.0"],
        "docs": docs_packages,
        "test": test_packages,
    },
)
