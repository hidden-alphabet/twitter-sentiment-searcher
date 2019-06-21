import setuptools

setuptools.setup(
    name='twitter-sentiment-searcher',
    version='0.0.0',
    author=["Cole Hudson", "Chris Louie"],
    author_email="cole@colejhudson.com",
    description="AWS Lambda function to handle JSON requests and output Time Series Data",
    install_requires=[
        "psycopg2"
    ],
    packages=setuptools.find_packages()
)