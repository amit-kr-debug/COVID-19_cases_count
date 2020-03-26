from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import scrappingValues
# from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route("/")
def hello():
    return "Home page"
@app.route("/sms", methods=['POST'])
def sms_reply():
    msg=request.form.get('Body')
    resp = MessagingResponse()
    if msg=='Give info':
        resp.message("Hey there, I'm an automated bot, I can help you to get updated with realtime no. of active cases \n Select the option\n 1. Nation wide\n 2. State wise data")
        msg=request.form.get('Body')
    elif msg=='1':
        nat=str(scrappingValues.nationalCases())
        resp.message("The total no. of active cases nation wide are "+nat)
    elif msg=='2':
        resp.message("To get the info of State wise corona affected people\nSelect accordingly\na. Andhra Pradesh\nb. Bihar\nc. Chhattisgarh\nd. Delhi\ne. Goa\nf. Gujarat\ng. Haryana\nh. Himachal Pradesh\ni. Karnataka\nj. Kerala\nk. Madhya Pradesh\nl. Maharashtra\nm. Manipur\nn. Mizoram\no. Odisha\np. Puducherry\nq. Punjab\nr. Rajasthan\ns. Tamil Nadu\nt. Telengana\nu. Chandigarh\nv. Jammu and Kashmir\nw. Ladakh\nx. Uttar Pradesh\ny. Uttarakhand\nz. West Bengal")
    elif msg.isalpha():
        if(len(msg)==1 and ord(msg)>96 and ord(msg)<123):
            statecases,statename=scrappingValues.statewise(msg)
            resp.message("Total no. of active cases in "+statename+" are "+statecases)
        else :
            resp.message("Invalid request please try giving request \n'Give info'\n and follow the instructions")
    else:
        resp.message("Invalid request please try giving request \n'Give info'\n and follow the instructions")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)