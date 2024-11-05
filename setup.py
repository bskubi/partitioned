from setuptools import setup

setup(
    name='partitioned',
    version='0.1.0',
    py_modules=['partitioned'],
    author='Benjamin Skubi',
    author_email='skubi@ohsu.edu',
    description='Determine if a series of lines is partitioned (all identical lines sequential).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bskubi/partitioned',  # Update this if applicable
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)