import os
from os.path import abspath, dirname, join

from IPython.display import SVG
from pygraphviz import AGraph


def relpath(*parts):
    return abspath(join(dirname(abspath(__file__)), *parts))


def notebook_image_path(basename):
    return relpath('..', 'notebooks', 'images', basename)


diagrams = []


@diagrams.append
def compiler():
    graph = AGraph(directed=True)

    graph.graph_attr['label'] = "CPython Compilation Stages"
    graph.graph_attr['labelloc'] = "t"
    graph.graph_attr['rankdir'] = 'LR'

    graph.add_node('Raw Source Code', shape='rectangle')
    graph.add_node('Source Text', shape='rectangle')
    graph.add_node('Abstract Syntax Tree', shape='rectangle')
    graph.add_node('Bytecode', shape='rectangle')

    graph.add_path([
        'Raw Source Code',
        'Source Text',
        'Abstract Syntax Tree',
        'Bytecode',
    ])

    return graph


@diagrams.append
def decoder():
    graph = AGraph(directed=True)

    graph.graph_attr['rankdir'] = 'LR'

    graph.add_node('Raw Source Code', shape='rectangle')
    graph.add_node('Source Text', shape='rectangle')

    graph.add_path(['Raw Source Code', 'Source Text'])
    return graph


def draw_all():
    for func in diagrams:
        name = notebook_image_path(func.__name__ + '.svg')
        try:
            os.unlink(name)
        except:
            pass
        print("Drawing %s" % name)
        func().draw(name, format='svg', prog='dot')
