import json
from pathlib import Path
from setuptools import find_packages, setup


AIRULE_CLIENT_PACKAGE_NAME = 'h1st'


current_dir_path = Path(__file__).parent

metadata = json.load(open(current_dir_path /
                          AIRULE_CLIENT_PACKAGE_NAME /
                          'metadata.json'))

with open(current_dir_path / 'README.md', encoding='utf8') as f:
    long_description = f.read()

with open(current_dir_path / AIRULE_CLIENT_PACKAGE_NAME /
          'requirements.txt') as f:
    requirements = f.readlines()


setup(
    name=metadata['PACKAGE'],
    version=metadata['VERSION'],
    description=metadata['DESCRIPTION'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=metadata['AUTHOR'],
    url=metadata['URL'],
    download_url=metadata['DOWNLOAD_URL'],
    packages=find_packages(include=[f'{AIRULE_CLIENT_PACKAGE_NAME}.*']),
    scripts=[],
    classifiers=metadata['CLASSIFIERS'],
    license='Apache 2.0',
    keywords=metadata['KEYWORDS'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points='',
    python_requires='>= 3.8',
    namespace_packages=[AIRULE_CLIENT_PACKAGE_NAME]
)
