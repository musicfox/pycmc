#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "pycmc"
DESCRIPTION = "A Python client for the chartmetric.com API."
URL = "https://github.com/musicfox/pycmc"
EMAIL = "dev@musicfox.io"
AUTHOR = "Jason R. Stevens, CFA | Musicfox, Inc. | https://musicfox.io"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = "0.0.5"

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution…")
        os.system("{0} setup.py sdist bdist_wheel ".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")


        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=[
        "attrs==19.3.0",
        "certifi==2020.4.5.1",
        "chardet==3.0.4",
        "coverage==5.1",
        "idna==2.9",
        "importlib-metadata==1.6.0; python_version < '3.8'",
        "more-itertools==8.2.0",
        "numpy==1.18.4",
        "packaging==20.3",
        "pandas==1.0.3",
        "pluggy==0.13.1",
        "psutil==5.7.0",
        "py==1.8.1",
        "pyparsing==3.0.0a1",
        "pytest==5.4.2",
        "pytest-cov==2.8.1",
        "python-dateutil==2.8.1",
        "pytz==2020.1",
        "requests==2.23.0",
        "six==1.14.0",
        "urllib3==1.25.9",
        "wcwidth==0.1.9",
        "zipp==3.1.0",
    ],
    extras_require={
        "dev": [
            "alabaster==0.7.12",
            "appdirs==1.4.4",
            "attrs==19.3.0",
            "babel==2.8.0",
            "backcall==0.1.0",
            "black==19.10b0",
            "bleach==3.1.5",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2020.4.5.1",
            "cffi==1.14.0",
            "chardet==3.0.4",
            "click==7.1.2",
            "colorama==0.4.3",
            "commonmark==0.9.1",
            "cryptography==2.9.2",
            "decorator==4.4.2",
            "distlib==0.3.0",
            "docutils==0.16",
            "idna==2.9",
            "imagesize==1.2.0",
            "importlib-metadata==1.6.0; python_version < '3.8'",
            "ipython==7.14.0",
            "ipython-genutils==0.2.0",
            "jedi==0.17.0",
            "jeepney==0.4.3; sys_platform == 'linux'",
            "jinja2==3.0.0a1",
            "keyring==21.2.1",
            "markupsafe==2.0.0a1",
            "orderedmultidict==1.0.1",
            "packaging==20.3",
            "parso==0.7.0",
            "pathspec==0.8.0",
            "pep517==0.8.2",
            "pexpect==4.8.0; sys_platform != 'win32'",
            "pickleshare==0.7.5",
            "pip-shims==0.5.2",
            "pipenv-setup==3.0.1",
            "pipfile==0.0.2",
            "pkginfo==1.5.0.1",
            "plette[validation]==0.2.3",
            "prompt-toolkit==3.0.5",
            "ptyprocess==0.6.0",
            "pycparser==2.20",
            "pygments==2.6.1",
            "pyparsing==3.0.0a1",
            "python-dateutil==2.8.1",
            "pytz==2020.1",
            "readme-renderer==26.0",
            "recommonmark==0.6.0",
            "regex==2020.5.7",
            "requests==2.23.0",
            "requests-toolbelt==0.9.1",
            "requirementslib==1.5.7",
            "secretstorage==3.1.2; sys_platform == 'linux'",
            "six==1.14.0",
            "snowballstemmer==2.0.0",
            "sphinx==3.0.3",
            "sphinxcontrib-applehelp==1.0.2",
            "sphinxcontrib-devhelp==1.0.2",
            "sphinxcontrib-htmlhelp==1.0.3",
            "sphinxcontrib-jsmath==1.0.1",
            "sphinxcontrib-qthelp==1.0.3",
            "sphinxcontrib-serializinghtml==1.1.4",
            "toml==0.10.0",
            "tomlkit==0.6.0",
            "tqdm==4.46.0",
            "traitlets==4.3.3",
            "twine==3.1.1",
            "typed-ast==1.4.1",
            "typing==3.7.4.1",
            "urllib3==1.25.9",
            "vistir==0.5.0",
            "wcwidth==0.1.9",
            "webencodings==0.5.1",
            "wheel==0.34.2",
            "zipp==3.1.0",
        ]
    },
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand,},
    project_urls={
        "Documentation": "https://pycmc.docs.musicfox.io",
        "Bug Reports": "https://github.com/musicfox/pycmc/issues",
        "Source Code": "https://github.com/musicfox/pycmc",
        "Musicfox": "https://musicfox.io",
    },
)
