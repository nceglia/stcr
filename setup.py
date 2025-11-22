from setuptools import setup, find_packages

setup(
    name='stcr',
    version='0.0.1',
    description='Information theoretic metrics for single cell RNA and TCR sequencing.',
    packages=find_packages(include=['stcr','stcr.metrics','stcr.preprocessing','stcr.plotting','stcr.utils']),
    #install_requires=["scipy","numpy","notebook","sklearn","pandas","scanpy","tqdm","seaborn","matplotlib"],
)
