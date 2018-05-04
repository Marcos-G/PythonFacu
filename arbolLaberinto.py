import plotly.offline as py
import plotly.graph_objs as go

import igraph
from igraph import *

nr_vertices = 25
G = Graph() # 2 stands for children number
G.add_vertices(5)
G.add_edges([(0,1),(0,2)])
lines = go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   )
dots = go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='',
                  marker=dict(symbol='dot',
                                size=18,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                  text=labels,
                  hoverinfo='text',
                  opacity=0.8
                  )



axisx = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=True,
            showticklabels=True,
            )
axisy = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

layout = dict(title= 'Tree with Reingold-Tilford Layout',
              font=dict(size=12),
              showlegend=False,
              xaxis=go.XAxis(axisy),
              yaxis=go.YAxis(axisx),
              margin=dict(l=40, r=40, b=85, t=100),
              hovermode='closest',
              plot_bgcolor='rgb(248,248,248)'
              )

data=go.Data([lines, dots])
fig=dict(data=data, layout=layout)
py.plot(fig, filename='laberinto.html')
