from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'Life_Manager',
    version = '0.0.1',
    author = 'ADG',
    author_email = 'anusri.gnanaprakasom@gmail.com',
    description = 'organize your stuff',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/AnusriGnanaprakasam/Projects',
    include_package_data=True,
    py_modules = ['LifeManager'],
    packages = ["LifeManager"],
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: Windows ",
    ],
    entry_points = {'console_scripts':['life-manager=LifeManager.main:main']}
)