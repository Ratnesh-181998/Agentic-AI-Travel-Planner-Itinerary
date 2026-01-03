from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Agent-Based-Travel-Reasoning-System",
    version="0.1",
    author="Ratnesh Kumar Singh",
    packages=find_packages(),
    install_requires = requirements,
)