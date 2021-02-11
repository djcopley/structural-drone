from setuptools import find_packages, setup

setup(
    name='structural-drone',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "opencv-python",
        "tensorflow",
        "mavsdk",
        "pycairo",
        "PyGObject"
    ],
    setup_requires=[
        "setuptools_scm"
    ],
    use_scm_version={
        "relative_to": __file__,
        "write_to": "src/version.py"
    },
)
