import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://thanhhai1299cosmosdb:QRsxuWhsl9cd7YYC29Y732uNcXL4lAcWGtFTk2elzz9WXrU0WLHQ34N1jWinEkeF2R7hQuaaS6xfrLhzbPpHDA==@thanhhai1299cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@thanhhai1299cosmosdb@"
            client = pymongo.MongoClient(url)
            database = client['neighborlydb']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)