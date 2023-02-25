from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
import pymongo


application = Flask(__name__)
app = application

@app.route("/", methods = ['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")


def get_reviews_from_html(flipkart_html, searchString):
    bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
    del bigboxes[0:3]
    box = bigboxes[0]
    productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
    prodRes = requests.get(productLink)
    prodRes.encoding='utf-8'
    prod_html = bs(prodRes.text, "html.parser")
    commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

    reviews = []
    for commentbox in commentboxes:
        try:
            #name.encode(encoding='utf-8')
            name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
        except:
            name="name"

        try:
            #rating.encode(encoding='utf-8')
            rating = commentbox.div.div.div.div.text
        except:
            rating = 'No Rating'

        try:
            #commentHead.encode(encoding='utf-8')
            commentHead = commentbox.div.div.div.p.text
        except:
            commentHead = 'No Comment Heading'
        try:
            comtag = commentbox.div.div.find_all('div', {'class': ''})
            #custComment.encode(encoding='utf-8')
            custComment = comtag[0].div.text
        except Exception as e:
            print(e)

        mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                    "Comment": custComment}
        reviews.append(mydict)
    print("Total no of reviews found for {} - {}".format(searchString, len(reviews)-1))
    return reviews


def store_data(reviews):
    try:
        client = pymongo.MongoClient("mongodb+srv://dyamrit:3PVF8bxy4jP1oswe@cluster0.clbgotk.mongodb.net/?retryWrites=true&w=majority")
        db = client['web_scraping']
        collection = db['reviews']
        collection.insert_many(reviews)
    except Exception as e:
        print(e)


@app.route("/review" , methods = ['POST' , 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = urlopen(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")

            reviews = get_reviews_from_html(flipkart_html, searchString)
            store_data(reviews)
            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            print(e)
            return 'something is wrong'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
	#app.run(debug=True)
