#I didn't want to stress the api call incase there were limitations, so I keep it at about 4-5 minutes
CHECKTIME = 240.0

#enter the email you want to use for this (I recommend using a new email)
EMAIL = ""
#enter the App password for the email (you can get this at https://myaccount.google.com/u/1/security then look for App passwords)
EMAIL_PASSWORD = ""

#enter your twitch client ID/client Secret (you can get this at https://dev.twitch.tv/console/apps)
TWITCH_CLIENT_ID = ""
TWITCH_CLIENT_SECRET = ""

#your phone number
PHONE_NUMBER = "1234567890"

#phone carrier (only att, tmobile, verizon, and sprint are currently available)
PHONE_CARRIER = ""
# "att" "tmobile" "verizon" "sprint"

#this program comes with two ways to check if a streamer is live
#first you can just do a general check to see if they are live using the below list

StreamerList = ['xqc']

#if you are looking to see if a streamer is playing a certain game
#you can use the below list to filter by game

StreamerListFilter = [
    {
        'name': 'sodapoppin',
        'games': ['just chatting', 'world of warcraft', 'league of legends']
    }
]