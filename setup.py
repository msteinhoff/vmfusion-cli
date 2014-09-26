from setuptools import setup

setup(
    name='vmfusion-cli',
    version='0.1.0',
    author='Mario Steinhoff',
    author_email='steinhoff.mario@gmail.com',
    url='https://github.com/msteinhoff/vmfusion-cli',
    license='LICENSE.txt',
    description='A simple python CLI replacement for the VMware Fusion GUI.',
    install_requires=[
        "pyyaml >= 3.11",
        "vmfusion >= 0.2.0"
    ],
    scripts=[
        "bin/vmfusion-cli"
    ]
)
