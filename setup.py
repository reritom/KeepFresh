from setuptools import setup, find_packages
import os

SRC_DIR = os.path.join(os.path.dirname(__name__), 'src')

def get_readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name="keepfresh",
    version="0.0.1",
    description="Filesystem event polling",
    author="Tomas Sheers",
    author_email="t.sheers@outlook.com",
    keywords=["FILESYSTEM", "EVENT", "POLLING"],
    long_description=get_readme(),
    package_dir={'': SRC_DIR},
    packages=find_packages(SRC_DIR),
    entry_points={
        'console_scripts': [
            'keepfresh = keepfresh.command_line:main [keepfresh]',
        ]
    },
)
