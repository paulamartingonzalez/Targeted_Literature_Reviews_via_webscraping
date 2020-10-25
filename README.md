![alt text](https://github.com/paulamartingonzalez/Targeted_Literature_Reviews_via_webscrapping/blob/main/repository-open-graph-template.jpg)

# Targeted Literature Reviews_via webscrapping

Web scraping to get articles for a given query. It returns an spreadsheet with titles, abstracts, doi and references of the article

It works on Pubmed and it is based on biopython: https://biopython.org

You can run it on Google Colab without downloading anything locally! :) https://research.google.com/colaboratory/faq.html

For a given query, you can get:

1) an xlsx file with the titles and abstracts of the papers in your query
2) a graph with the papers in your query and their references. This lets us find highly cited papers in a given field
3) an xlsx file with the titles and abstracts of the references as well together with their degree (i.e. the number of connections in the graph). The higher the degree, the more papers in your query citing it

For the example query "Radiomics"AND"CT"AND"Ovarian Cancer" we get:

![alt text](https://github.com/paulamartingonzalez/WebScrappingLiterature/blob/main/Unknown-7.png)


If you have any suggestion to improve the code, please feel free to raise an Issue!
