from flask import Flask
from flask_restful import Api,Resource
from amazonScraper import AmazonScrape
from FlipkartScraper import FlipkartScrape
from tataScraper import TataScrape

app=Flask(__name__)
api=Api(app)
api.add_resource(AmazonScrape,"/amazonScrape/<string:keyword>")
api.add_resource(FlipkartScrape,"/flipkartScrape/<string:keyword>")
api.add_resource(TataScrape,"/tataCliqScrape/<string:keyword>")


if __name__ == "__main__":
    app.run(debug=True)