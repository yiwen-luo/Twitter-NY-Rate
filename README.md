# TwitterNYRate

### Introduction
This application will tell whether any breaking news happens in the Great New York Area by monitoring the rates of twitter posted in this ares.

The application consists of two main parts, the data streaming part and monitoring part, where the data steaming part retrieves and displays the data in real-time, and the monitoring part keeps an eye on the rate of tweets people post in Great New York Area.

Main technology involved are: Tweepy API, Google Maps API, Redis, Websocketd, Python, JavaScript, HTML5.


### Components of Application
The following two parts are run by "TweetNYInsert.py":
- The data streaming part retrieves tweets around Great New York Area with geographic locations from Twitter in realtime. Websocketd will send the location data through a websocket in realtime. An HTML page with Google Map API displays each of the location with a pin on the map, where the map is dynamic and supports all Google Map functions. Although the locations are just plotted on a map, other data are also collected like the text of the Tweet and the retweeting numbers.

- The data streaming part also takes down the time each of useful tweets is received and send it to a Redis server for in-memory storage. The message stored in Redis includs two information, the time this tuple of tweet is received and the time difference between last message and current message, a.k.a delta of time.  Each of the messages will be stored in Redis for 600 seconds, i.e. 10 minutes. After such time, it will be dumped. 

The following part is run by "TweetNYAvg.py":
- The moniroting part retrieves tuples from Redis 


### Data Stream
This application utilizes Twitter Streaming API. More specifically, public streams from the API are fetched. The streams of data include tweets from all around the world in realtime. In addition to the content, more information of the tweets is given in the JSON format of data, which is described in detail below.
The original information of the API can be found [here] (https://dev.twitter.com/streaming/public). Detailed application is developed with Python and [tweepy] (https://github.com/tweepy/tweepy) library.



##### Data Utilization
Among all the data, only the "geo", which indicates the latitude of longitude of the location where the tweet is sent, is printed by python and sent by websocket in JSON format.

##### Data Amount
Raw data with or without geographic information are expected to have more than 4,000 tuples per seconds. However, rate of tweets with geographic locations is only around 10 per second, which is reasonable and feasible for visualization.

### How to start
1. Start a local Redis Server with default settings. (If not installed, it can be installed by Homebrew: 
    ```brew install redis```)
2. run StartServer.sh (which will run TwitterGet.py)
3. open index.html

Enjoy!
