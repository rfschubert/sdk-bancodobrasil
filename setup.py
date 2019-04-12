from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name="sdk-bancodobrasil",
    author="Raphael Schubert",
    author_email="rfswdp@gmail.com",
    description="SKD de integracao com Banco do Brasil",
    url="https://github.com/rfschubert/sdk-bancodobrasil",
    version='0.0.1',
    packages=find_packages(exclude=('tests', 'docs')),
    long_description=readme,
    install_requires=[
        'requests',
        # 'xmltodict',
        # 'pendulum',
    ],
    include_package_data=True,
)
