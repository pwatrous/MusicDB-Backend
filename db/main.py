from py2neo import Graph

import auth
from Nodes import Track


def main():
    graph = Graph("bolt://localhost:7687", user=auth.user, password=auth.password)

    tx = graph.begin()  # creates a transaction

    tracks = []
    # TODO parse inputs from frontend and fill tracks

    for track in tracks:
        track.commit_to_graph(tx)  # FIXME add param track first?

    tx.commit()  # commits the transaction
