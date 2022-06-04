from django.shortcuts import render
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

def index(request):
    return render(request,'index.html')

def gs_params(author_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "api_key": api_key
    }
    return params


def get_author_profile(request):
    if request.method == 'GET':
        context = {}
        author_url = request.GET.get('author_url')
        author_id = str(author_url).partition('user=')[2][:12]
        params = gs_params(author_id)
        search = GoogleSearch(params)
        results = search.get_dict()
        if 'author' in results :
            context["name"] = results["author"]["name"]
            context["total_citations"] = results["cited_by"]["table"][0]["citations"]["all"]
        else:
            context["errors"] = {
                "invalid author url",
                "your search for the month is exhausted",
                "or your api key is invalid. Your API key should be here: https://serpapi.com/manage-api-key"
            }
    
    return render(request,'index.html', context)