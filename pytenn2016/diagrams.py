import os
from os.path import abspath, dirname, join

from IPython.display import SVG
from pygraphviz import AGraph


def relpath(*parts):
    return abspath(join(dirname(abspath(__file__)), *parts))


def notebook_image_path(basename):
    return relpath('..', 'notebooks', 'images', basename)


def path_graph(nodes):
    graph = AGraph(directed=True)

    for node in nodes:
        graph.add_node(node, shape='rectangle')

    graph.add_path(nodes)
    return graph


diagrams = []


@diagrams.append
def compiler():
    graph = path_graph([
        'Raw Source (Bytes)',
        'Source Text (Unicode)',
        'Abstract Syntax Tree',
        'Bytecode',
        'Execution',
    ])

    graph.graph_attr['label'] = "CPython Code Representations"
    graph.graph_attr['labelloc'] = "t"
    graph.graph_attr['rankdir'] = 'LR'

    return graph


@diagrams.append
def decoder():
    graph = path_graph(['Raw Source (Bytes)', 'Source Text (Unicode)'])
    graph.graph_attr['rankdir'] = 'LR'

    return graph


@diagrams.append
def importhook():

    graph = path_graph([
        'Module Name',
        'Raw Source (Bytes)',
        'Source Text (Unicode)',
        'Abstract Syntax Tree',
        'Bytecode',
        'Execution',
    ])

    graph.add_edge('Module Name', 'Bytecode', color='red', label='Import Hook')

    graph.graph_attr['rankdir'] = 'LR'

    return graph


@diagrams.append
def bytecode():
    graph = path_graph(['Bytecode', 'Execution'])
    graph.add_edge('Bytecode', 'Bytecode', label='Bytecode Transformer')

    graph.graph_attr['rankdir'] = 'LR'
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
