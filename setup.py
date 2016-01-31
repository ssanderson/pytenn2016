from setuptools import setup, find_packages


def install_requires():
    return ['IPython', 'jupyter[all]']


def main():
    setup(
        name='ssanderson-pytenn-2016',
        version='0.1',
        description="PyTennessee Talk 2016",
        author="Scott Sanderson",
        author_email="scott.b.sanderson90@gmail.com",
        packages=find_packages(include='pytenn2016.*'),
        include_package_data=True,
        zip_safe=True,
        url="https://github.com/ssanderson/pytenn-2016",
        classifiers=[
            'Framework :: IPython',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python',
        ],
        install_requires=install_requires(),
    )
