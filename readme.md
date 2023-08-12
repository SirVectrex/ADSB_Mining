# ADSB Data Analytics

### Features
Printing JSON Answers from FR24 API - Business Subscription required.
Receiving flights in Munich - seperated by runway

### Usage

Please install requirements using: 
```shell
$ pip install -r requirements.txt
```
and install the OpenSkyPackage manually as described here: [Github Readme](https://github.com/openskynetwork/opensky-api)

Run the App with:
```shell
$ streamlit run .\app\app.py
```

Collect the data with running main.py in /datacollector:
```shell
$ python datacollector/main.py
```
