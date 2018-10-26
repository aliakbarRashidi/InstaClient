import random
import time

from .instaclient import InstaClient
from .userinfo import UserInfo

#use userinfo
ui = UserInfo()
ui.search_user(user_name="login")

#take following
ui.get_following()
following = ui.following

#take followers
ui.get_followers()
followers = ui.followers

#favorite id list
favorites = ['111', '222', '333']

#some lists
newlist = []
endlist = []
followerslist = []

#get following id
for item in following:
    newlist.append(item['id'])

#get followers id
for item in followers:
    followerslist.append(item['id'])

#create final list with followers
endlist = set.difference(set(newlist), set(favorites), set(followerslist))

#create final list without followers
'''
endlist = set.difference(set(newlist), set(favorites))
'''

#use instaclient
bot = InstaClient('login', 'password')

print('Number of unnecessary subscriptions:', len(endlist), '\n')

for items in endlist:
    rnd = random.randint(1, 16)
    bot.unfollow(items)
    print('Wait', 30 + rnd, 'sec')
    time.sleep(30 + rnd)

print('All done.')