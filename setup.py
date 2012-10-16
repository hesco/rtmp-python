from setuptools import find_packages
from setuptools import setup


setup(
    name='rtmp-python',
    version='0.0',
    description="RTMP",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='',
    author_email='',
    url='',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'PyAMF',
        'setuptools',
        ],
    entry_points="""
    # -*- Entry points: -*-

    """)