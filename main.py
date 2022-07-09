import requests, time, os
from text import send_message
import logging
import config

#logger
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

#twitch api client
client_id = config.TWITCH_CLIENT_ID
client_secret = config.TWITCH_CLIENT_SECRET
body = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
r = requests.post('https://id.twitch.tv/oauth2/token', body)
keys = r.json()
headers = {'Client-ID': client_id, 'Authorization': 'Bearer ' + keys['access_token']}

#get streamer info and last game
def getStreamerData(streamer_name):
    #get data
    stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
    stream_data = stream.json()

    #if live get current game
    if(len(stream_data['data']) == 1):
        last_game = stream_data['data'][0]['game_name']
    else:
        last_game = ''

    #get last_game content
    if(os.path.exists('{}.txt'.format(streamer_name))):
        with open('{}.txt'.format(streamer_name)) as f:
            game_check = f.read()
    else:
        game_check = ''

    global last_check

    #last_check is last_game
    last_check = game_check

    #if last_game (saved from txt) doesnt equal the current game overwrite last_game.txt
    if(game_check != last_game):
        with open('{}.txt'.format(streamer_name), 'w') as f:
            f.write(last_game)

    #return stream data
    return stream_data

#check streamers game
def checkGame(streamer_name):
    data = getStreamerData(streamer_name)

    #if user is live
    if len(data['data']) == 1:
        data = data['data'][0]
        #check if current game equals last game (from last_game.txt)
        if(data['game_name'] == last_check):
            #true == no text
            print("{} | no game change".format(streamer_name))
        else:
            #true == send text
            gameR = data['game_name'].replace(":", "")
            text = "{} is playing {}".format(data['user_name'], gameR)
            #print("{} | game change/live".format(streamer_name))
            #send text
            try:
                send_message(config.PHONE_NUMBER, config.PHONE_CARRIER, text)
            except Exception as e:
                print(f"Message error: {e}")
                logger.error(e)


    else:
        #user is not live do nothing
        #print("{} is not live right now".format(streamer_name))
        if(os.path.exists('{}.txt'.format(streamer_name))):
            os.remove('{}.txt'.format(streamer_name))

#check streamers game with filter
def checkGameFilter(streamer_name, filter):
    data = getStreamerData(streamer_name)

    #if user is live
    if len(data['data']) == 1:
        data = data['data'][0]
        #check if current game equals last game (from last_game.txt)
        if(data['game_name'] == last_check):
            #true == no text
            print("{} | no game change".format(streamer_name))
        else:
            #true == send text
            for game in filter:
                if(data['game_name'].lower() == game):
                    gameR = data['game_name'].replace(":", "")
                    text = "{} is playing {}".format(data['user_name'], gameR)
                    #print("{} | game change/live".format(streamer_name))
                    #send text
                    try:
                        send_message(config.PHONE_NUMBER, config.PHONE_CARRIER, text)
                    except Exception as e:
                        #print(f"Message error: {e}")
                        logger.error(e)
                    break
    else:
        #user is not live do nothing
        #print("{} is not live right now".format(streamer_name))
        if(os.path.exists('{}.txt'.format(streamer_name))):
            os.remove('{}.txt'.format(streamer_name))

#check every x amount of seconds if user is live/game changed
starttime = time.time()
while True:
    try:
        for streamer in config.StreamerList:
            checkGame(streamer)
        for streamer in config.StreamerListFilter:
            checkGameFilter(streamer['name'], streamer['games'])
    except Exception as e:
        #print(f"Loop error: {e}")
        logger.error(e)
    time.sleep(config.CHECKTIME - ((time.time() - starttime) % config.CHECKTIME))