from setuptools import find_packages, setup

setup(
    name="skeyes",
    version="1.0.0",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        # GStreamer
    ],
    setup_requires=[
        "setuptools_scm"
    ],
    use_scm_version={
        "relative_to": __file__,
        "write_to": "skeyes/version.py"
    },
    entry_points={
        "console_scripts": [
            "skeyes = skeyes.main:main"
        ],
        "gui_scipts": [
            "gskeyes = skeyes.main:gui"
        ]
    }
)
