from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from networkx import DiGraph

from labs.util.file_processing.extensions import mk_dir_abs_from_local
from labs.util.file_processing.configuration import DATA_OUTPUT_FOLDER


def single_plot(data: Dict[str, float], identifier: int, name: str, dir_name: str = DATA_OUTPUT_FOLDER) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.barplot(x=list(data.keys()), y=list(data.values()))
    graphic.set(xlabel=name, ylabel="Value")
    graphic.set_xticklabels(graphic.get_xticklabels(), rotation=90, ha="right", fontsize=10)
    graphic.bar_label(graphic.containers[0], fmt="%.2f")
    plt.tight_layout()
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    graphic.get_figure().savefig(f"{directory}/{name.lower()}.png")
    plt.clf()


def multi_plot(data: List[float], identifier: int, name: str, dir_name: str = DATA_OUTPUT_FOLDER) -> None:
    plt.figure(figsize=(12, 8))
    graphic: object = sns.histplot(data=data, kde=False)
    graphic.set(xlabel=name, ylabel="Value")
    graphic.bar_label(graphic.containers[0], fmt="%.2f")
    plt.tight_layout()
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    graphic.get_figure().savefig(f"{directory}/{name.lower()}.png")
    plt.clf()


def graph_plot(nodes: List[Tuple[str, str, int]], identifier: int, name: str,
               dir_name: str = DATA_OUTPUT_FOLDER) -> None:
    graph: DiGraph = nx.DiGraph()
    graph.add_edges_from([(node[0], node[1]) for node in nodes])
    options = {
        'node_color': 'blue',
        'arrowstyle': '-|>',
    }
    nx.draw_spring(graph, with_labels=True, **options)
    directory: str = mk_dir_abs_from_local(f"{dir_name}/{identifier}")
    plt.savefig(f"{directory}/{name.lower()}.png")
    plt.clf()