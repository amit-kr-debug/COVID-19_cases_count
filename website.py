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
        resp.message("Hey there, I'm an automated bot, I can help you to get updated with realtime no. of active cases \n Select the option\n a. Nation wide\n b. State wise data")
        msg=request.form.get('Body')
    elif msg=='a':
        active,total,death,recovered=scrappingValues.nationalCases()
        resp.message("The no. cases of COVID-19 Nation wide are\nTotal confirmed cases:"+total+"\nWhich includes:-\nActive cases: "+active+"\nDeath cases: "+death+"\nRecovered: "+recovered)
    elif msg=='b':
        resp.message("To get the info of State wise corona affected people\nSelect accordingly\n1. Andhra Pradesh\n2. Andaman and Nicobar\n3. Bihar\n4. Chandigarh\n5. Chhattisgarh\n6. Delhi\n7. Goa\n8. Gujarat\n9. Haryana\n10. Himachal Pradesh\n11. Jammu and Kashmir\n12. Karnataka\n13. Kerala\n14. Ladakh\n15. Madhya Pradesh\n16. Maharashtra\n17. Manipur\n18. Mizoram\n19. Odisha\n20. Puducherry\n21. Punjab\n22. Rajasthan\n23. Tamil Nadu\n24. Telengana\n25. Uttarakhand\n26. Uttar Pradesh\n27. West Bengal")
    elif msg.isdigit():
        if(int(msg)>0 and int(msg)<28):
            statecases,statename=scrappingValues.statewise(msg)
            resp.message("Total no. of confirmed cases in "+statename+" are "+statecases)
            # resp.message("Ministry Of Health has withdrawn the state-wise data from the official website\nSorry for the inconvenience")
        else :
            resp.message("Invalid request please try giving request \n'Give info'\n and follow the instructions")
    else:
        resp.message("Invalid request please try giving request \n'Give info'\n and follow the instructions")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)