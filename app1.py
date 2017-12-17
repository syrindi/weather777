#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    #return r




    #speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')
    speech = "This is a return"
    print("Response:")
    print(speech)
    
    
    data = {
  "items": [
    {
      "simpleResponse": {
          "textToSpeech":"This is the first simple response for a basic card"
      }
    },
    {
      "basicCard": {
        "title":"Title: this is a title",
        "formattedText":"This is a basic card.  Text in a\n      basic card can include \"quotes\" and most other unicode characters\n      including emoji 📱.  Basic cards also support some markdown\n      formatting like *emphasis* or _italics_, **strong** or __bold__,\n      and ***bold itallic*** or ___strong emphasis___ as well as other things\n      like line  \nbreaks",
        "subtitle":
        "This is a subtitle",
        "image": {
          "url":"https://image.freepik.com/free-icon/apple-logo_318-40184.jpg",
          "accessibilityText":"Image alternate text"
        },
        "buttons": [
          { 
            "title":"This is a button",
            "openUrlAction":{ 
              "url":"https://assistant.google.com/"
            }
          }
        ]
      }
    },
    {
      "simpleResponse": {
        "textToSpeech":"This is the 2nd simple response ",
        "displayText":"This is the 2nd simple response"
      }
    }
  ],
  "suggestions": 
  [
    {"title":"Basic Card"},
    {"title":"List"},
    {"title":"Carousel"},
    {"title":"Suggestions"}
  ]
}
    

    return {
        "speech": speech,
        "displayText": speech,
         "data": speech,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
