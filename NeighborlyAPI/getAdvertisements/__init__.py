import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://thanhhai1299cosmosdb:QRsxuWhsl9cd7YYC29Y732uNcXL4lAcWGtFTk2elzz9WXrU0WLHQ34N1jWinEkeF2R7hQuaaS6xfrLhzbPpHDA==@thanhhai1299cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@thanhhai1299cosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['neighborlydb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

