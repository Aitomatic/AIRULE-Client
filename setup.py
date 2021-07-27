import json
from pathlib import Path
from setuptools import find_packages, setup
from types import SimpleNamespace


AIRULE_CLIENT_PACKAGE_NAME = 'airule'


current_dir_path = Path(__file__).parent

metadata = SimpleNamespace(**json.load(open(current_dir_path /
                                       AIRULE_CLIENT_PACKAGE_NAME /
                                       'metadata.json')))


setup(
    name=metadata.PACKAGE,
    version=metadata.VERSION,
    description=metadata.DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=metadata.AUTHOR,
    maintainer=metadata.AUTHOR,
    url=metadata.URL,
    download_url=metadata.DOWNLOAD_URL,
    packages=find_packages(include=[f'{AIRULE_CLIENT_PACKAGE_NAME}.*']),
    py_modules=[],
    scripts=[],
    classifiers=metadata.CLASSIFIERS,
    license='MIT',
    keywords=metadata.KEYWORDS,
    # package_dir={'': ''},
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').readlines(),
    entry_points=dict(console_scripts=['airule=airule.cli:airule']),
    extras_require={},
    python_requires='>= 3.8',
    setup_requires=[],
    namespace_packages=[]
)
