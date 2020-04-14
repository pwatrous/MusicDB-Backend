# from py2neo import Graph, NodeMatcher
#
# import auth
# from Nodes import Track
#
# def node_exists(graph, label, node):
#     print(type(node))
#     matcher = NodeMatcher(graph)
#     match = matcher.match(label, id=node["id"]).first()
#     return match
#
#
# def main():
#     graph = Graph("bolt://localhost:7687", user=auth.user, password=auth.password)
#
#     tx = graph.begin()  # creates a transaction
#
#     tracks = []
#     # TODO parse inputs from frontend and fill tracks
#
#     for track in tracks:
#         if node_exists(graph, "Track", track) is None:  # track does not already exist in graph
#             track.commit_to_graph(graph)  # FIXME add param track first?
#
#     tx.commit()  # commits the transaction
