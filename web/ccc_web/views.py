from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import couchdb

# find the host ip for couchDB instance
f = open("hosts",'r')
lines = f.readlines()
for i in range(len(lines)):
    if lines[i] == "[couchDB_instance_group]\n":
        db_host = lines[i+1][:-1]
server_ip = 'http://admin:admin@'+db_host+':5984/'

# get data
couch = couchdb.Server(server_ip)
poor = []
rich = []
db = couch["poor_tweet"]
db2 = couch["wealth_tweet"]

for item in db.view('twitter/get_tweets',descending=True,limit=100):
    poor.append([item.value["id"],item.value["text"],item.value["created_at"]])
for item in db2.view('twitter/get_tweets',descending=True,limit=100):
    rich.append([item.value["id"],item.value["text"],item.value["created_at"]])

poor_count = db.info()["doc_count"]
rich_count = db2.info()["doc_count"]

def index(request):
    return render(request,'index.html')

def tweets(request):
    context={'poor':poor,'rich':rich,'c1':poor_count,'c2':rich_count}
    return render(request,'tweets.html',context)

def results(request):
    return render(request,'results.html')

def members(request):
    return render(request,'members.html')

