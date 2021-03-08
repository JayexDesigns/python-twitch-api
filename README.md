<h1 align="center">Python Twitch API</h1>
<p align="center">A python library to comunicate with the twitch API easily</p>
<br>
<h2>Installing</h2>
<p>For now the way to install this library is to clone this repository or download twitchAPI.py, while having this file in the same folder of your project will make it available to import the library</p>
    <pre lang="python">
        import twitchAPI
    </pre>
<br>
<h2>Authentication</h2>
<p>To use this library first you need to have a twitch application, go to the <a src="https://dev.twitch.tv/console/apps">Twitch developer console</a> and go to the apps tab, then click the register your application button. Add a name and a category to your application and create it, once it's done you can click on manage to get the Client ID and the Client Secret, both needed to use the API</p>
<br>
<p>Once you have both the Client ID and the Client Secret you can use this library, you will need a OAuth Token before using any of the library functions, here is an example code on how to get the OAuth Token:</p>
    <pre lang="python">
        import twitchAPI

        clientId = "Your Client ID"
        clientSecret = "Your Client Secret"

        auth = twitchAPI.authentication(clientId, clientSecret)
        auth.fullToken #This is the OAuth Token you will need to use
    </pre>
<br>
<h2>Use</h2>
<p>Now you can start gathering information and interacting with the API, here there is a list of methods you can call and what they do</p>
<ul>
    <li>searchChannel(clientId, authToken, streamerName) -> This will give you a dictionary with some information of the streamer, including the streamer id</li>
    <li>getUser(clientId, authToken, streamerId) -> This will give you a dictionary with some information of the user such as it's description</li>
    <li>getChannelInfo(clientId, authToken, streamerId) -> This will give you a dictionary with information of the streamer like the game he/she is playing</li>
    <li>getUserFollows(clientId, authToken, streamerId) -> Returns the follower quantity a streamer has</li>
    <li>getStreamInfo(clientId, authToken, streamerId) -> This gives information about the current stream of the given streamer</li>
    <li>getAllStreamerInfo(clientId, authToken, streamerName) -> This method mixes all of the above and returns a dictionary with all the information</li>
</ul>
