from facepy import GraphAPI


OAUTH_TOKEN = '<your oauth token>'

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

        no_of_friends_by_gender = {}
        no_of_friends_by_gender['male'] = 0
        no_of_friends_by_gender['female'] = 0
        no_of_friends_by_gender['unspecified'] = 0
        friends = self.graph.get('me/friends?fields=gender', page=True)
        for friend_page in friends:
            for single_friend in friend_page['data']:
                if single_friend.has_key('gender'):
                    if single_friend['gender'] == 'male':
                        no_of_friends_by_gender['male'] += 1
                    elif single_friend['gender'] == 'female':
                        no_of_friends_by_gender['female'] += 1
                    else:
                        no_of_friends_by_gender['unspecified'] += 1
                else:
                        no_of_friends_by_gender['unspecified'] += 1

        return no_of_friends_by_gender


    def get_number_of_wall_posts(self):
        '''
        This function will return the number of wall posts made by the current user
        '''
        FQL = 'SELECT wall_count FROM user WHERE uid = me()'
        return self.graph.fql(FQL)['data'][0]['wall_count']

    def get_number_of_albums(self):
        '''
        This function will return the number of albums created by you
        '''
        FQL = 'SELECT aid from album where owner = me()'
        albums = self.graph.fql(FQL)
        return len(albums['data'])


obj = FBStat(graph)
print obj.get_number_of_friends()
print obj.get_number_male_female_friends()
print obj.get_number_of_albums()

