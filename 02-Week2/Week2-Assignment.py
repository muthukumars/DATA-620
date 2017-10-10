########### Week2 Assignment
########### Collaborative done by Muthukumar Srinivasan & Rajagopal Srinivasan through various dicussions and programming
########### Learnings


import matplotlib.pyplot as plt
import networkx as nx


graph=nx.Graph()

# create edges
graph.add_edge('andre','beverly')
graph.add_edge('andre','carol')
graph.add_edge('andre','diane')
graph.add_edge('beverly','andre')
graph.add_edge('beverly','diane')
graph.add_edge('beverly','ed')
graph.add_edge('carol','andre')
graph.add_edge('carol','diane')
graph.add_edge('carol','fernando')
graph.add_edge('fernando','garth')
graph.add_edge('fernando','diane')
graph.add_edge('fernando','carol')
graph.add_edge('garth','ed')
graph.add_edge('garth','diane')
graph.add_edge('garth','fernando')
graph.add_edge('garth','heather')
graph.add_edge('ed','beverly')
graph.add_edge('ed','diane')
graph.add_edge('ed','garth')
graph.add_edge('heather','fernando')
graph.add_edge('heather','garth')
graph.add_edge('heather','ike')
graph.add_edge('ike','heather')
graph.add_edge('ike','jane')
graph.add_edge('jane','ike')

# Set node positions explicitly 
position={'andre':(0,1),
     'beverly':(0,-1),
     'carol':(1,2),
     'diane':(1,0),
     'ed':(1,-2),
     'ike':(4,0),
     'garth':(2,-1),
     'jane':(5,0),
     'fernando':(2,1),
     'heather':(3,0)}

# nodes
nx.draw_networkx_nodes(graph,position,node_size=800, node_color='c')

# edges
nx.draw_networkx_edges(graph,position,alpha=0.5,width=6)

# labels
nx.draw_networkx_labels(graph,position,font_size=15,font_family='sans-serif')

plt.axis('off')
plt.show() # display
