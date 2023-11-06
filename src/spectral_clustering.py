import numpy as np
from typing import Union
import networkx as nx
from collections import Counter
import sklearn
import sklearn.metrics
import matplotlib.pyplot as plt


def data_to_coordinates(data_dict):
    sum_of_vals = sum(data_dict.values())
    n_qubits = len(list(data_dict.keys())[0])
    ##
    data_distribution = {k: v / sum_of_vals for k, v in data_dict.items()}
    base_graph = get_allowed_graph("all", n_qubits)
    ## calculate the correlations
    # data_graph = add_mutual_information_to_graph(base_graph, data_distribution)
    data_graph = add_correlation_to_graph(base_graph, data_distribution)
    #
    sp = nx.adjacency_matrix(data_graph, nodelist=base_graph.nodes).toarray()
    for ii in range(n_qubits):
        sp[ii, ii] = -np.sum(sp[ii, :])
    lapl = -sp
    eigvals, eigvecs = np.linalg.eig(lapl)
    eigperm = np.argsort(eigvals)
    perm_eigvals = eigvals[eigperm]
    perm_eigvecs = eigvecs[:, eigperm].T
    coords1 = perm_eigvecs[1]  # /perm_eigvals[1]
    coords2 = perm_eigvecs[2]  # /perm_eigvals[2]  # dividing could be beneficial
    return coords1, coords2


def get_allowed_graph(allowed_topology: Union[str, np.ndarray], number_of_qubits) -> nx.Graph:
    if isinstance(allowed_topology, np.ndarray):
        assert allowed_topology.shape[0] == allowed_topology.shape[1] == number_of_qubits
        return nx.from_numpy_array(allowed_topology)
    elif allowed_topology == "star":
        ## center_qubit = 0
        return nx.star_graph(number_of_qubits)

    elif allowed_topology == "line":
        print("line topology")
        return nx.path_graph(number_of_qubits)

    elif allowed_topology == "all":
        print("all topology")
        return nx.complete_graph(number_of_qubits)

    else:
        raise ValueError("allowed_topology is not 'all', 'line', 'star', or an adjancency matrix")


def add_mutual_information_to_graph(G: nx.Graph, target_distribution: dict):
    new_G = nx.Graph()
    for node_tuple in G.edges:
        samples_x = []
        samples_y = []
        for sample, prob in target_distribution.items():
            val = round(prob * 10000)
            if val >= 1:
                samples_x.extend([sample[node_tuple[0]]] * val)
                samples_y.extend([sample[node_tuple[1]]] * val)

        score = sklearn.metrics.mutual_info_score(
            samples_x,
            samples_y,
        )
        new_G.add_edge(*node_tuple, weight=max(1e-8, score))
    return new_G


def add_correlation_to_graph(G: nx.Graph, target_distribution: dict):
    new_G = nx.Graph()
    for node_tuple in G.edges:
        score = get_corr11_cost(target_distribution, *node_tuple)
        new_G.add_edge(*node_tuple, weight=score)  # max(1e-8, score))
    return new_G


def get_corr11_cost(target_distribution, q1, q2):
    corr11 = 0
    for sample, prob in target_distribution.items():
        if sample[q1] == sample[q2] == 1:
            corr11 += prob
    return 1 - corr11


def draw_graph(G, reference_G=None):
    if reference_G is None:
        reference_G = G

    ed = np.array([edge[2]["weight"] for edge in G.edges(data=True)])
    ed /= max(ed)
    options = {
        "node_color": "#A0CBE2",
        "edge_color": "k",
        "edge_color": plt.cm.Blues(ed),
        "width": 3,
        # "edge_cmap": plt.cm.Blues,
        "with_labels": True,
    }
    nx.draw_networkx(G, **options)
    # labels = nx.get_edge_attributes(G, "weight")
    # pos = nx.circular_layout(reference_G)
    # round labels
    # labels = {pair: round(weight, 3) for pair, weight in labels.items()}
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.gca().axis("off")
