# Copyright (C) 2019-2020 HERE Europe B.V.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# License-Filename: LICENSE

"""Project setup file."""

from codecs import open
from os import path

from setuptools import find_packages, setup

__version__ = "0.0.1"

here = path.abspath(path.dirname(__file__))

# Get the core dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [
    x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")
]

# Get extra dependencies
with open(path.join(here, "requirements_dev.txt"), encoding="utf-8") as f:
    dev_reqs = f.read().strip().split("\n")

download_url = (
    "https://github.com/heremaps/xyz-spaces-python"
    "/archive/" + __version__ + ".zip"
)

setup(
    # download_url=download_url,
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    # scripts=["bin/xyzspaces"],
    extras_require={"dev": dev_reqs},
)
