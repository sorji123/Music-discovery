Project 1 Sorji1
readme
<h1>Technologies</h1>
VSCode, Git, GitHub, and Heroku
<h1>Frameworks</h1>
 Flask, dotenv
<h1>Libraries</h1>
: Requests, os, random, json
For my python project I used request, os, json and random. Request is used to authorize the API for it to work. Os is used to search for the token in .env file. random is to generate random variables from a given value. Json is used when passing through data like top artist song and album image. 
<h1>API</h1>
I used Spotify API to return artist top track and album image. then used genius API to return the artist song lyrics.
<h1>Forking</h1>
To put this in your repository you will need a Spotify developer account and a genius developer account. then transfer your Spotify personal token. in this case that will be client ID and client secret inside my .env file. then repeat the process for genius but only the client access token. 
Be sure to download all the required installation before forking it to your repository. 
<h1>Heroku URL:</h1>
 Project 1 (lit-dusk-64750.herokuapp.com)  https://lit-dusk-64750.herokuapp.com/
<h1>Question 1</h1>
One of the biggest hurdles I faced was parse a json. In fact, I spent most of my time trying to figure out how to set up the Json file from params to headers. Spotify did an awful job arranging it. I had to use to Json beautifier even that had that helped a lot especially sorting the overload of information. You can only imagine how difficult. To make matters worse that's not the only problem I had. I had issues trying to connect to my app on Heroku. Kept on saying application error. 
<h1>Question 2</h1>
Some of the known problems still in my project are genius api rap lyrics and my HTML format. My genius lyrics won't change, I tried multiple times to have it align with preview song and artist song. But it won't budge. In addition, my HTML format is ridiculous. I tried to put the preview link and lyrics side by side. That didn't budge too.
<h1>Question 3</h1>
In the future I'll probably see if I could make the genius API lyric align with the song artist order song that's playing. 
