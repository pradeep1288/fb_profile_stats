from facepy import GraphAPI


OAUTH_TOKEN = 'CAACEdEose0cBAEdJqi0bzZCGlfrTNWZCqWUrbvZBoj3PE81cVojE60p8VSNFm2iSBYZBg9QAGZCLNRnAcLl4VBeQ45QRpZCLfQ9lekiMmHZCdbgqBF5auKoCURcSo0bjMkTfnAVbJAsrLMkhTSyvZBEZC6ZA7I0f1HZBysuQS7kbkxK4pVfgQrFSHSt5qjF2OEpSSKlYXDfCWZAJxwZDZD'

graph = GraphAPI(OAUTH_TOKEN)




def get_number_of_friends(graph):
    FQL = 'SELECT friend_count FROM user WHERE uid = me()'
    return graph.fql(FQL)['data'][0]['friend_count']

def get_friends_gender(graph):
    pass

def get_number_of_wall_posts(graph):
    FQL = 'SELECT wall_count FROM user WHERE uid = me()'
    return graph.fql(FQL)['data'][0]['wall_count']

#print get_number_of_friends(graph)
#next_list = graph.get('me/friends?fields=gender')['paging']['next'].replace('https://graph.facebook.com/','')
#friends = graph.get('me/friends',page=True)
#for friend in friends:
#    print len(friend['data'])