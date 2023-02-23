from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
import pymongo
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logger_filename = os.path.join(BASE_DIR, "scrapper.log")
logging.basicConfig(filename=logger_filename , level=logging.INFO)

app = Flask(__name__)

@app.route("/", methods = ['GET'])
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
            logging.info("name")

        try:
            #rating.encode(encoding='utf-8')
            rating = commentbox.div.div.div.div.text
        except:
            rating = 'No Rating'
            logging.info("rating")

        try:
            #commentHead.encode(encoding='utf-8')
            commentHead = commentbox.div.div.div.p.text
        except:
            commentHead = 'No Comment Heading'
            logging.info(commentHead)
        try:
            comtag = commentbox.div.div.find_all('div', {'class': ''})
            #custComment.encode(encoding='utf-8')
            custComment = comtag[0].div.text
        except Exception as e:
            logging.info(e)

        mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                    "Comment": custComment}
        reviews.append(mydict)
    logging.info("Total no of reviews found for {} - {}".format(searchString, len(reviews)-1))
    return reviews


def store_data(reviews):
    try:
        client = pymongo.MongoClient("mongodb+srv://dyamrit:3PVF8bxy4jP1oswe@cluster0.clbgotk.mongodb.net/?retryWrites=true&w=majority")
        db = client['web_scraping']
        collection = db['reviews']
        collection.insert_many(reviews)
    except Exception as e:
        logging.info(e)


@app.route("/review" , methods = ['POST' , 'GET'])
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
            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            logging.info(e)
            return 'something is wrong'
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
