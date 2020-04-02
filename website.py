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
        resp.message("Hey there, I'm an automated bot, I can help you to get updated with realtime no. of active cases \nSelect the option\na. Nation wide\nb. State wise data")
        msg=request.form.get('Body')
    elif msg=='a':
        active,total,death,recovered=scrappingValues.nationalCases()
        resp.message("The no. cases of COVID-19 Nation wide are\nTotal confirmed cases:"+total+"\nWhich includes:-\nActive cases: "+active+"\nDeath cases: "+death+"\nRecovered: "+recovered)
    elif msg=='b':
        resp.message(
            "To get the info of State wise corona affected people\nSelect accordingly\n1. Andhra Pradesh\n2. Andaman and Nicobar\n3. Assam\n4. Bihar\n5.Chandigarh\n6. Chhattisgarh\n7. Delhi\n8. Goa\n9. Gujarat\n10. Haryana\n11. Himachal Pradesh\n12. Jammu and Kashmir\n13. Jharkhand\n14. Karnataka\n15. Kerala\n16. Ladakh\n17. Madhya Pradesh\n18. Maharashtra\n19. Manipur\n20. Mizoram\n21. Odisha\n22. Puducherry\n23. Punjab\n24. Rajasthan\n25. Tamil Nadu\n26. Telengana\n27. Uttarakhand\n28. Uttar Pradesh\n29. West Bengal")

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