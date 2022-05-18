from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'Projects',
    version = '0.0.1',
    author = 'ADG',
    author_email = 'do this later',
    license = '<the license you chose>',
    description = 'organize your stuff',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/AnusriGnanaprakasam/Projects',
    include_package_data=True,
    py_modules = ['projects,cli'],
    packages = ["projects"],
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: Windows ",
    ],
    #entry_points = {'console_scripts':['projects=projects.:function']}#no need apparently
)