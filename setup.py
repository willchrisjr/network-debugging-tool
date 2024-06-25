from setuptools import setup, find_packages

setup(
    name="network-debugging-tool",
    version="0.1.0",
    description="A comprehensive command-line utility for network diagnostics",
    author="Your Name",
    author_email="email@example.com",
    url="https://github.com/yourusername/network-debugging-tool",
    packages=find_packages(),
    install_requires=[
        "dnspython==2.3.0",
        "requests==2.31.0"
    ],
    entry_points={
        "console_scripts": [
            "network-debugging-tool=cli.cli_handler:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)