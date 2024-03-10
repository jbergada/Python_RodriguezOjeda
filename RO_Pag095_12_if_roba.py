#RO_095_12_roba.py

articles = 10
preu_article = 14

if articles <= 5:
    preu = articles*preu_article
elif articles > 5 and articles < 10:
    preu = articles * (preu_article*0.95)
elif articles >= 10:
    preu = articles* (preu_article*0.92)

print("preu a pagar = ",preu)