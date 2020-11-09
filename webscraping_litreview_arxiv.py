import openpyxl
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium import webdriver
import re
import requests
from lxml import html
from lxml import etree
import urllib
import re   
import unicodedata
import time
import networkx as nx
import pandas as pd
import arxiv


myquery = 'Ovarian Cancer'
max_papers = 100

# Get an interator over query results
result = arxiv.query(
  query=myquery,
  max_chunk_results=100,
  max_results=max_papers,
  iterative=True
)

# Sometimes the variable result is weird. So making an array.
papers = []
for paper in result():
  papers += [paper]

titles = []
urls = []

def get_content(paper):

    title = paper['title']
    summary = paper['summary']
    summary = summary.replace('\n',' ').replace(',', ' ').rstrip('\r\n')
    title = title.replace('\n',' ').replace(',', ' ').rstrip('\r\n') 
    url = paper['arxiv_url']
    titles.append(title)
    urls.append(url)
    content = title + ',' + summary
    return content

for paper in papers:
    content = get_content(paper)    

data = {'title': titles, 'urls':urls} 
df2 = pd.DataFrame(data) 
print(df2)
df2.to_excel('output.xlsx') 


'''
# Graph Stuff
nodes = []
edges = []
new_ids=[]
for i in range(len(refs)):
  temp = refs[i]
  name=str(pmids[i])
  if temp:
    if name not in nodes:
      nodes.append(name)
    temp2 = temp[0]
    A = temp2.get('Reference')
    for j in range(len(A)):
      temp3 = A[j].get('ArticleIdList')
      try:
        name2 = str(temp3[0])
        if name2 not in nodes:
          nodes.append(name2)
          new_ids.append(name2)

        edges.append((name,name2))
      except:
        pass

g = nx.Graph()
g.add_nodes_from(nodes)
for i in range(len(edges)):
  B = edges[i]
  g.add_edge(B[0], B[1])

color_map = []
for node in nodes:
    if node in pmids:
        color_map.append('blue')
    else: 
        color_map.append('red')      

nx.draw(g,node_size=100, node_color=color_map,alpha=0.5)                  
'''