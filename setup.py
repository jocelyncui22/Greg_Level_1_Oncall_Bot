from setuptools import setup, find_packages

setup(
    name="greg-oncall-bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "jinja2>=3.0.1",
        "python-multipart>=0.0.5",
        "python-dotenv>=0.19.0",
        "pydantic>=1.8.2",
    ],
    python_requires=">=3.8",
)