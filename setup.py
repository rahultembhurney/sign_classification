from setuptools import setup, find_packages

def get_requirements(filepath):
    EXCLUSION = "-e ."
    with open(filepath, "r") as f:
        requirements = []
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            if line == EXCLUSION:
                pass
            else:
                requirements.append(line)

    return requirements


setup(
    name="sign_classification",
    version="0.0.1",
    author="rahultembhurney",
    author_email="rtembhurney7@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
    )

