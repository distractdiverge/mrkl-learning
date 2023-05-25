from setuptools import setup, find_packages

setup(
    name="mrk_learning",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "mrk_learning=mrkl_learning:main",
        ],
    },
    python_requires='>=3.10',
)