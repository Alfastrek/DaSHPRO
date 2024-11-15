from urllib import request
import os
from bson import json_util
import pymongo
from pymongo import MongoClient
from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
import json
load_dotenv()

mongo_connection_string = os.getenv('MONGO_CONNECTION_STRING')
if not mongo_connection_string:
    raise ValueError("No MongoDB connection string set in environment variables")

client = MongoClient(mongo_connection_string)
db = client['Datafile']
collection = db['Assignment']

    # connection completed

# function to call country vs intensity chart data
def country_intensity_datas(request):
    result = collection.find({"$and": [{"country": {"$exists": True, "$ne": None}}, {"intensity": {"$exists": True, "$ne": None}}]})
    data = []
    for doc in result:
        data.append(doc)
    data_json = json.dumps(data, default=json_util.default)
    context = {'data': json.loads(data_json)}
    return JsonResponse(json.loads(data_json),
                        safe=False)

# function to call country vs relevance chart data
def relevance_pestle_datas(request):
    result = collection.find({
        "$and": [
            {"relevance": {"$exists": True, "$ne": None}},
            {"pestle": {"$exists": True, "$ne": None}}
        ]
    })
    data = []
    for doc in result:
        data.append(doc)
    data_json = json.dumps(data, default=json_util.default)
    context = {'data': json.loads(data_json)}
    return JsonResponse(json.loads(data_json),
                        safe=False)

 #function to call complete data   
def datas(request):
    result = collection.find()
    data = []
    for doc in result:
        data.append(doc)


    data_json = json.dumps(data, default=json_util.default)
    context = {'data': json.loads(data_json)}
    return JsonResponse(json.loads(data_json),
                        safe=False)


    

        




def intensity(request):
    pipeline = [
    {
    "$group": {
    "_id": "$country",
    "total_intensity": {"$sum": "$intensity"}
    }
    }
    ]
    result = collection.aggregate(pipeline)
    

    # Extract countries and respective intensity values from the result
    country_intensity_dict = {}
    for doc in result:
        country = doc['_id']
        intensity = doc['total_intensity']
        
        country_intensity_dict[country] = intensity
    country_intensity_dict = dict(sorted(country_intensity_dict.items(), key=lambda item: item[1]))  
    country_intensity_dict.popitem()
    country_intensity_dict.popitem()
    return JsonResponse(country_intensity_dict, safe=False)      

    # return render(request, 'dashboard.html', context)

def base(request):
    template_path = os.path.join('layouts', 'base.html')
    return render(request, template_path)

def reports(request):
    template_path = os.path.join('reports.html')
    return render(request, template_path)

def datatabels(request):
    template_path = os.path.join('datatables.html')
    return render(request, template_path)

def profile(request):
    template_path = os.path.join('profile.html')
    return render(request, template_path)
