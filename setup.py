import os
import re
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise RuntimeError("require Python 3.6+")


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), "cgroup_parser", "__init__.py")
    with open(init_py) as file_in:
        for line in file_in:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        raise RuntimeError("Cannot find version in {}".format(init_py))


setup(
    name="cgroup-parser",
    version=read_version(),
    url="https://github.com/ZhuYuJin/cgroup-parser",
    project_urls={
        "Documentation": "https://github.com/ZhuYuJin/cgroup-parser",
        "Code": "https://github.com/ZhuYuJin/cgroup-parser",
        "Issue tracker": "https://github.com/ZhuYuJin/cgroup-parser/issues",
    },
    maintainer="robertzhu",
    description="cgroup parser for python",
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
    },
    packages=find_packages(include=("cgroup_parser", "cgroup_parser.*")),
)
