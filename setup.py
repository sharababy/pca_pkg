"""
Copyright (c) 2018, Vedant Bassi.
All rights reserved.
This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from setuptools import setup

setup(
    name='pca_pkg',
    version='1.0',
    author='Vedant Bassi',
    author_email='ced15i013@iiitdm.ac.in',
    maintainer='Vedant Bassi',
    maintainer_email='ced15i013@iiitdm.ac.in',
    description='Computations of PCA for a given csv file.',
    py_modules=['pca_module'],
    license='BSD License',
    platforms='Any',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)