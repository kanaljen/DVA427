import numpy as np
import networkx as nx

fname = 'city.txt'
dt = np.dtype('str, str, uint8')

dataset = np.loadtxt(fname, dtype='str', skiprows=3)

def get_distance(A,B):

G = nx.Graph()
G.add_node(1)
