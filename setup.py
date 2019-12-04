from setuptools import find_packages, setup

setup(
    author="Mateus Vanzo de Padua, Deepak Vashist",
    author_email="mateuspaduaweb@gmail.com, deepaksvashist@gmail.com",
    description="ClearSale Total Anti Fraud Python SDK",
    install_requires=("suds-py3==1.3.4.0", "xmltodict==0.9.2"),
    license="MIT License",
    name="clearsale-python",
    packages=find_packages(),
    python_requires=">=3.8.0",
    url="https://github.com/mateuspadua/clearsale-python",
    version="1.4.0",
    zip_safe=False,
)
