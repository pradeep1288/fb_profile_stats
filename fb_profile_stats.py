from facepy import GraphAPI


OAUTH_TOKEN = '<oauth_token>'

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

    def get_number_of_photos(self):
        '''
        Return the number of photos uploaded by the user
        '''
        # First fetch all the user albums, with aid's
        FQL = 'SELECT aid from album where owner = me()'
        albums = graph.fql(FQL)
        no_of_photos = 0
        for album_id in albums['data']:
            TEMP_FQL = 'SELECT photo_count from album where aid =' + album_id['aid']
            no_of_photos += self.graph.fql(TEMP_FQL)['data'][0]['photo_count']
        return no_of_photos

    def get_number_of_likes_on_albums(self):
        '''
        Returns the total number of likes on the albums
        '''
        # get the object_id's of all the albums, as its needed for the like's table
        #ToDo: Verify correntness.
        FQL = 'select object_id from album where owner = me()'
        albums_object_ids = graph.fql(FQL)
        for object_id in albums_object_ids['data']:
            TEMP_FQL = 'SELECT user_id from like where object_id=' + str(object_id['object_id'])
            print len(self.graph.fql(TEMP_FQL)['data'])



obj = FBStat(graph)
#print obj.get_number_of_friends()
#print obj.get_number_male_female_friends()
#print obj.get_number_of_albums()
#print obj.get_number_of_photos()
print obj.get_number_of_likes_on_albums()