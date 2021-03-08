#Imports
import requests
import json



#Gets The Authentication Token, Needed For Almost Everything
def authentication(clientId, clientSecret):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": clientId,
        "client_secret": clientSecret,
        "grant_type": "client_credentials"
    }
    return requests.post(url=url, params=params).json()



#Searches By Username, I Use This To Get Basic Streamer Info And Specially It's ID So I Can Do Other Types Of Requests
def searchChannel(clientId, authToken, streamerName):
    url = f"https://api.twitch.tv/helix/search/channels?query={streamerName}&first=1"
    headers = {
        "client-id": clientId,
        "Authorization": authToken
    }
    return requests.get(url=url, headers=headers).json()



#Similar To The Above But This One Gives Also The type, The broadcaster_type, The description, The viewer_count And The created_at
def getUser(clientId, authToken, streamerId):
    url = f"https://api.twitch.tv/helix/users?id={streamerId}"
    headers = {
        "client-id": clientId,
        "Authorization": authToken
    }
    return requests.get(url=url, headers=headers).json()



#Similar To The Above But This One Gives Also The game_name
def getChannelInfo(clientId, authToken, streamerId):
    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={streamerId}"
    headers = {
        "client-id": clientId,
        "Authorization": authToken
    }
    return requests.get(url=url, headers=headers).json()



#Gets The Streamer's Total Followers And Information One By One That I Don't Care So I Ignore It
def getUserFollows(clientId, authToken, streamerId):
    url = f"https://api.twitch.tv/helix/users/follows?to_id={streamerId}&first=1"
    headers = {
        "client-id": clientId,
        "Authorization": authToken
    }
    response = requests.get(url=url, headers=headers).json()
    return response



#Gets Stream Info If The Streamer Is Currently Streaming
def getStreamInfo(clientId, authToken, streamerId):
    url = f"https://api.twitch.tv/helix/streams?user_id={streamerId}&first=1"
    headers = {
        "client-id": clientId,
        "Authorization": authToken
    }
    return requests.get(url=url, headers=headers).json()



#Mixes All The Responses
def getAllStreamerInfo(clientId, clientSecret, streamerName):
    authToken = authentication(clientId, clientSecret)
    authToken = f"{authToken['token_type'].capitalize()} {authToken['access_token']}"
    streamerInfo = {}
    streamInfo = {}

    response1 = searchChannel(clientId, authToken, streamerName)
    if response1["data"][0]["broadcaster_login"] != streamerName.lower():
        raise Exception
    streamerInfo["username"] = response1["data"][0]["display_name"]
    streamerInfo["login"] = response1["data"][0]["broadcaster_login"]
    streamerInfo["id"] = response1["data"][0]["id"]
    streamerInfo["language"] = response1["data"][0]["broadcaster_language"]
    streamerInfo["link"] = f"https://www.twitch.tv/{response1['data'][0]['broadcaster_login']}"
    streamerInfo["live"] = response1["data"][0]["is_live"]

    response2 = getUser(clientId, authToken, streamerInfo["id"])
    streamerInfo["global_type"] = response2["data"][0]["type"]
    streamerInfo["streamer_type"] = response2["data"][0]["broadcaster_type"]
    streamerInfo["description"] = response2["data"][0]["description"]
    streamerInfo["avatar"] = response2["data"][0]["profile_image_url"]
    streamerInfo["offline_image"] = response2["data"][0]["offline_image_url"]
    streamerInfo["views"] = response2["data"][0]["view_count"]
    streamerInfo["created"] = response2["data"][0]["created_at"]

    response3 = getChannelInfo(clientId, authToken, streamerInfo["id"])

    response4 = getUserFollows(clientId, authToken, streamerInfo["id"])
    streamerInfo["followers"] = response4["total"]

    if streamerInfo["live"]:
        response5 = getStreamInfo(clientId, authToken, streamerInfo["id"])

        streamInfo["title"] = response5["data"][0]["title"]
        streamInfo["id"] = response5["data"][0]["id"]
        streamInfo["game_id"] = response5["data"][0]["game_id"]
        streamInfo["game"] = response5["data"][0]["game_name"]
        streamInfo["date"] = response5["data"][0]["started_at"]
        streamInfo["viewers"] = response5["data"][0]["viewer_count"]
        streamerInfo["stream"] = streamInfo

    return streamerInfo