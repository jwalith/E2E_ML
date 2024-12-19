from setuptools import setup, find_packages

E_DOT = '-e .'
def get_requirements(file_path):
    req=[]
    with open(file_path) as f:
        req = f.read().splitlines()

    if E_DOT in req:
        req.remove(E_DOT)
    return req
    

setup(
    name='E2E_ML',
    version='0.1.0',
    author='Jk',
    author_email='jwalithkristam@gmail.com',
    description='A package for end-to-end machine learning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jwalith/E2E_ML',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=get_requirements('requirements.txt'),
)