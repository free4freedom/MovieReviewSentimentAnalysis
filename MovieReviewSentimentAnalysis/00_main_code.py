import twitter
import json

def oauth_login():
    CONSUMER_KEY = 'Il4zL2aYkiv5gK48rOnf20ygT'
    CONSUMER_SECRET = 'uzmhD58Q7VRT6ygeVUUorcMsGr2fZXfnloIS5ZUPRZPQkQYbbn'
    OAUTH_TOKEN = '404911413-2wMh9NfTpr6CkLGIkdrbBsaAMZ7FnGWUcHbn8zh5'
    OAUTH_TOKEN_SECRET = 'Gx2oSgxv13BQ8ROQQATncCn8tjjB6qATpCZirqqZgs55M'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#------------------------------------------------------------------------------------------------
def twitter_search(twitter_api, q, max_results=1000, **kw) :
    #***************************************************
    #Hyderabad coordinates

    '''
    latitude=17.3850440
    longitude=78.4866710
    max_range=50

    search_results = twitter_api.search.tweets(q=q, geocode = "%f,%f,%dkm" % (latitude, longitude, max_range),
                                              count=100, lang='en', **kw)
    '''
    #***************************************************
    
    search_results = twitter_api.search.tweets(q=q, count=1000, lang='en', **kw)
    statuses = search_results['statuses']

    print max_results
    max_results = min(1000, max_results)
    print max_results

    for _ in range(20) :
        try :
            next_results = search_results['search_metadata']['next_results']
        except :
            break

        kwargs = dict([ kv.split('=')
                            for kv in next_results[1:].split("&") ])

        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

        if len(statuses) > max_results :
            break

    return statuses

#------------------------------------------------------------------------------------------------
twitter_api = oauth_login()


#**********************************
'''Right now commenting it to reduce the no. of twitter api hits.
But ideally, we can take user i/p & decide.
'''
#result1 = twitter_api.geo.search(query="India", granularity="country")
#place_id1 = result1['result']['places'][0]['id']

#place_id1 = 'b850c1bfd38f30e0' #India
#place_id1 = '96683cc9126741d1' #USA


#**********************************
search_query = "bajrangi bhaijaan"
results = twitter_search(twitter_api, search_query, max_results=1000)

#print json.dumps(results[0], indent=1)

#Clear a file & then open it.
f = open("data/Bajrangi_Bhaijaan.txt", "w")

for i in range(len(results)) :
     f.write( results[i]['text'].encode('utf-8') + "\n" )


f.close()
print "Fectched results - " + str(len(results) )
