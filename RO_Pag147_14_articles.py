#RO_Pag147_14_articles.py
diners = 1000
articles = [454, 725, 1000, 2343]
articles_comprar = 0
for n in range(0,4):
    if diners >= articles[n]:
        articles_comprar = articles_comprar + 1
        print("podem comprar ", diners//articles[n], " unitats de l'article ", n+1)
    if n == len(articles)-1:
        print("articles que podem comprar = ", articles_comprar)

#diners = 1000
#articles = [454, 725, 1000, 2343]
articles_comprar = 0

k = 1
for n in articles:
    if diners >= n:
        articles_comprar = articles_comprar + 1
        print("podem comprar ", diners//n , "unitats de l'article ", k)
        
    if k == len(articles):
            print("articles que podem comprar = ", articles_comprar)
    k = k + 1

#diners = 1000
#articles = [454, 725, 1000, 2343]
articles_comprar = 0

i = 0
while i < len(articles):
    if diners >=+ articles[i]:
        articles_comprar = articles_comprar + 1
        print("podem comprar ", diners//articles[i], " unitats de l'article ", i+1)
    if i == len(articles)-1:
        print("articles que podem comprar = ", articles_comprar)
    i = i + 1