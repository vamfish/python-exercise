import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FortuneTower-vamfish", # Replace with your own username
    version="0.1",
    author="vamfish",
    author_email="vamfish@icloud.com",
    description="Game of Fortune Tower",
    url="https://github.com/vamfish/python-exercise/tree/wsl/LearnPython3theHardWay/ex45_game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)