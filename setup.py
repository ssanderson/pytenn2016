from setuptools import setup


def install_requires():
    return [
        'jupyter[all]',
        'codetransformer>=0.6',
        'hy>=0.11.1',
        'pygraphviz>=1.3.1',
    ]


def extras_require():
    return {'extra': ['numba>=0.23.1', 'Cython>=0.23']}


def main():
    setup(
        name='ssanderson-pytenn-2016',
        version='0.1',
        description="PyTennessee Talk 2016",
        author="Scott Sanderson",
        author_email="scott.b.sanderson90@gmail.com",
        packages=['pytenn2016'],
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


if __name__ == '__main__':
    main()
