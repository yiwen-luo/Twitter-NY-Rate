# TwitterNYRate

### Introduction
This application will tell whether any breaking news happens in the Great New York Area by monitoring the rates of twitter posted in this ares.

The application consists of two main parts, the data streaming part and monitoring part, where the data steaming part retrieves and displays the data in real-time, and the monitoring part keeps an eye on the rate of tweets people post in Great New York Area.

Main technology involved are: Tweepy API, Google Maps API, Redis, Websocketd, Python, JavaScript, HTML5.


### Components of Application
#### Rate Track of Data
The following two parts are run by "TweetNYInsert.py":
- The data streaming part retrieves tweets around Great New York Area with geographic locations from Twitter in realtime. It takes down the time each of useful tweets is received and send it to a Redis server for in-memory storage. The message stored in Redis includs two information, the time this tuple of tweet is received and the time difference between last message and current message, a.k.a delta of time.  Each of the messages will be stored in Redis for 600 seconds, i.e. 10 minutes. After such time, it will be dumped. 

- The data streaming part also visualizes the received data in real-time on Google Maps. Websocketd on port 8080 will send the location data through a websocket in realtime. 


#### Alert System Monitoring the Rate
The following two parts are run by "TweetNYAvg.py":
- The moniroting part retrieves tuples from Redis and calculate the average rate of message in a 10-minute window. The program will monitor the trend of increasing or decreaing of the rate. The default status of the system is "green". If the rate is higher than the pervious second, the counter will increase 1. If the rate is lower than the pervious second, the counter will decrease 1. If the counter hits 20, the status will be turnd into "yellow", which indicates a medium probability of happening of a breaking news. If the counter hits 50, the status will be turned into "red", which indicates a high probability of happening of a breaking news. 

- A division on the webpage of Google Maps will display the status and rate. Another websocket on port 8081 will send the rate and status information to frontend in real-time.

#### Human-readable System and Data Visulization
The following two parts are run by "index.html":
An HTML page with Google Map API displays each of the location with a pin on the map, where the map is dynamic and supports all Google Map functions. Although the locations are just plotted on a map, other data are also collected like the text of the Tweet and the retweeting numbers.


### How to start
1. Start a local Redis Server with default settings. (If not installed, it can be installed by Homebrew: 
    ```brew install redis```)
2. run StartServer.sh (which will run TwitterGet.py)
3. open index.html

Enjoy!
