import numpy as np


def bitnumber_to_state(number, n_qubits):
    state = np.zeros(2**n_qubits)
    state[number] = 1
    return state


def bitnumber_to_bittuple(bs, n_qubits):
    return tuple(int(s) for s in bin(bs)[2:].zfill(n_qubits))


def bittuple_to_bitstring(bt):
    return "".join(str(int(b)) for b in bt)


def bittuple_to_bitnumber(bt):
    return int(bittuple_to_bitstring(bt), 2)


def bitstring_to_bittuple(bs):
    return tuple(int(s) for s in bs)


def get_bitnumber_energy(bitnumber, H, n_qubits):
    st = bitnumber_to_state(bitnumber, n_qubits)
    return st @ H.dot(st)


def get_2d_topology(Nx: int, Ny: int):
    edge_list = []

    for ny_counter in range(Ny):
        # connects inside rows
        edge_list.extend([(ii, ii + 1) for ii in range(ny_counter * Nx, (ny_counter + 1) * Nx - 1)])
        # connects between rows
        if ny_counter + 1 < Ny:
            edge_list.extend(
                [(ii, ii + Nx) for ii in range(ny_counter * Nx, (ny_counter + 1) * Nx)]
            )

    return edge_list
