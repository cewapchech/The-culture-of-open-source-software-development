from setuptools import(
    setup,
    find_packages
)

setup(
    name="ndrl",
    version="0.0.0",
    package_dir={"","scr"}
    packages=find_packages(where="scr")
)