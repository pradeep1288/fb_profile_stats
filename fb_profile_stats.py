from facepy import GraphAPI


OAUTH_TOKEN = 'CAACEdEose0cBADlYYN4H9tMZCMXLAmHkC1dYamrhDZAyPOCnWgWFsQYm5IiKjEwAf6pc7OcnRcWG9phihrnmTh0zTZBbsXnpQxxZASlMzx4IfpuHrZCM6ZAavGiZA04X77s5mRE2ZAdGzXM1JQdjjzBqBt8qcuk1B2chNCGZADRkq5VAZAmyxmlzjvbyF5mLxDh10FlvFkR2dgZAQZDZD'

graph = GraphAPI(OAUTH_TOKEN)

class FBStat:
    def __init__(self, graph):
        self.graph = graph

    def get_number_of_friends(self):
        '''
        This function will return the number of friends of the current user
        '''
        FQL = 'SELECT friend_count FROM user WHERE uid = me()'
        return self.graph.fql(FQL)['data'][0]['friend_count']

    def get_number_male_female_friends(self):
        '''
        This function will return the number of male and female friends of the current user
        '''



    def get_number_of_wall_posts(self):
        '''
        This function will return the number of wall posts made by the current user
        '''
        FQL = 'SELECT wall_count FROM user WHERE uid = me()'
        return self.graph.fql(FQL)['data'][0]['wall_count']

#print get_number_of_friends(graph)
#next_list = graph.get('me/friends?fields=gender')['paging']['next'].replace('https://graph.facebook.com/','')
#friends = graph.get('me/friends',page=True)
#for friend in friends:
#    print len(friend['data'])
obj = FBStat(graph)
print obj.get_number_of_friends()


