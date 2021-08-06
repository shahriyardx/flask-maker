import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="flask-maker",
    version="1.0.1",
    description="A tool to create flask projects faster with a scalable setup.",  # Optional
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahriyardx/flask-maker",
    author="Md Shahriyar Alam",
    author_email="contact@shahriyar.dev",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    entry_points={"console_scripts": ["flask-maker = flask_maker:cli", "fm = flask_maker:cli"]},
    keywords="flask, flask-maker",
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=["flask==2.0.1", "click==7.1.2"],
    project_urls={
        "Bug Reports": "https://github.com/shahriyardx/flask-maker/issues",
        "Source": "https://github.com/shahriyardx/flask-maker/",
    },
)
