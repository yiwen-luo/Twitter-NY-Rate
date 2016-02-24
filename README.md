# TwitterNYRate

### Introduction
This application will tell whether any breaking news happens in the Great New York Area by monitoring the rates of twitter in the ares.

The application consists of two main parts, the data streaming part and monitoring part:

The data streaming part retrieves tweets around Great New York Area with geographic locations from Twitter in realtime. Websocketd will send the location data through a websocket in realtime. An HTML page with Google Map API displays each of the location with a pin on the map, where the map is dynamic and supports all Google Map functions.

Although the locations are just plotted on a map, other data are also collected like the text of the Tweet and the retweeting numbers. With other information, it is possbile to conduct multiple analyses, such as trend analyses, emotion analyses, etc.


### Data Stream
This application utilizes Twitter Streaming API. More specifically, public streams from the API are fetched. The streams of data include tweets from all around the world in realtime. In addition to the content, more information of the tweets is given in the JSON format of data, which is described in detail below.
The original information of the API can be found [here] (https://dev.twitter.com/streaming/public). Detailed application is developed with Python and [tweepy] (https://github.com/tweepy/tweepy) library.



##### Data Utilization
Among all the data, only the "geo", which indicates the latitude of longitude of the location where the tweet is sent, is printed by python and sent by websocket in JSON format.

##### Data Amount
Raw data with or without geographic information are expected to have more than 4,000 tuples per seconds. However, rate of tweets with geographic locations is only around 10 per second, which is reasonable and feasible for visualization.

### How to start
1. run StartServer.sh (which will run TwitterGet.py)
2. open index.html

Enjoy!
