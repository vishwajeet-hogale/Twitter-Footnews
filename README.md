# Twitter-Footnews
Get real time twitter football news

## Steps to make this work 
1) clone the repository 
2) Run command : pip install -r "requirements.txt" 
3) Open 3 terminals 
  * Go to Server directory and run python flowtoMongo.py on one terminal (1/3) 
  * Go to Server directory and run python app.py on second terminal (2/3) 
  * Go to src directory and run npm start on third terminal (3/3)
4) To make any changes to the tweets that you want, 
  * Add multiple keys to tracklist list in Server/flowtoMongo.py file 
5) Every second you'll get new tweets related to your keys. 

Note : presents keys are realted to transfer market news in football
