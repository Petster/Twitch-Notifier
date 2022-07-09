# Twitch Streamer Notifier
Dont want to miss a minute of a stream? Use the Twitch Streamer Notifier to get instant text messages when your favorite streamer goes live!

---

### This app allows you to:
- Check if a certain streamer is live
- check if a certain streamer is playing a certain game

---

### How it works:
Every x amount of minutes the app calls the twitch api to check if a streamer is live. If they are live you get a text message on your phone. The app will send a message to a designated email, which will then get sent to your phone via text. If you have filters setup it will only send text messages if the streamer is playing that certain game/category

You can keep the app running on your desktop or you can do what I do and have a raspberry pi running the script in the background

---

## Setup
Setup is really simple, just fill out the __config.py__ file

| Field      | Description | Default |
| ----------- | ----------- | ----------- |
| CHECKTIME      | The amount of seconds to check if a streamer is live       | 240.0 |
| EMAIL   | The Gmail that will be used to send text messages        | "" |
| EMAIL_PASSWORD   | The __App Password__ for the email*        | "" |
| TWITCH_CLIENT_ID   | The Twitch Client ID**        | "" |
| TWITCH_CLIENT_SECRET   | The Twitch Client Secret**       | "" |
| PHONE_NUMBER   | Your Phone Number        | 1234567890 |
| PHONE_CARRIER   | Your Phone Carrier***        | "" |
| StreamerList   | List of streamers you want to know when they go live, and when they switch games        | [""] |
| ParaStreamerListFilter   | List of streamers you want to know when they are live playing a certain game       | [{"name": "", "games": ""}] |

__*__ Setting up your Gmail's __App Password__:
- I recommend creating a new Gmail for this
- Access [Google Account](https://myaccount.google.com/u/1/security) and look for App Passwords
- Under __Select App__ click __Other__
- Enter any name (Twitch Notifier)
- Click Generate
- Copy the generated password into the __EMAIL_PASSWORD__ field

__**__ Setting up your Twitch API Client:
- You can use your existing Twitch account
- Access [Twitch Dev Console](https://dev.twitch.tv/console)
- Click __Register your Application__
- Enter a name (Twitch Notifier)
- You can enter http://localhost as the __OAuth Redirect URL__
- __Category__ Analytics Tool
- Create and click __Manage__
- Copy the generated Client ID to __TWITCH_CLIENT_ID__
- Click __New Secret__ and Copy the generated Secret to __TWITCH_CLIENT_SECRET__

__***__ Phone Carrier List:
- Currently the app only has support to send messages through Gmail using the following Phone Carriers:
  - AT&T
  - T-Mobile
  - Verizon
  - Sprint

If you have any bugs please feel free to contact me, and if you have any suggestions to make the app better let me know :)