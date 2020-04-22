from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import scrappingValues
import nammaMysuru
# from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route("/")
def hello():
    return "Home page"
@app.route("/sms", methods=['POST'])
def sms_reply():
    msg=request.form.get('Body')
    resp = MessagingResponse()
    if msg=='Give info' or 'hi' or 'hey' or 'hii' or 'hello':
        resp.message("Hey there, I'm an automated bot, I can help you to get updated with realtime no. of active cases \nSelect the option\na. Nation wide\nb. State wise data\nc. Mysuru")
        msg=request.form.get('Body')
    elif msg=='a':
        active,total,death,recovered=scrappingValues.nationalCases()
        resp.message("The no. cases of COVID-19 Nation wide are\nTotal confirmed cases: "+total +"\nWhich includes:-\nActive cases: "+active+"\nDeath cases: "+death+"\nRecovered: "+recovered)
    elif msg=='b':
        resp.message(
            "To get the info of State wise corona affected people\nSelect accordingly\n1.   Andhra Pradesh\n2.   Andaman and Nicobar\n3.   Arunachal Pradesh\n4.   Assam\n5.   Bihar\n6.   Chandigarh\n7.   Chhattisgarh\n8.   Delhi\n9.   Goa\n10. Gujarat\n11. Haryana\n12. Himachal Pradesh\n13. Jammu and Kashmir\n14. Jharkhand\n15. Karnataka\n16. Kerala\n17. Ladakh\n18. Madhya Pradesh\n19. Maharashtra\n20. Manipur\n21. Mizoram\n22. Odisha\n23. Puducherry\n24. Punjab\n25. Rajasthan\n26. Tamil Nadu\n27. Telengana\n28. Uttarakhand\n29. Uttar Pradesh\n30. West Bengal")
    elif msg=='c':
        active, total, death, recovered = nammaMysuru.nammaMysuru()
        resp.message(
            "The no. cases of COVID-19 in Mysuru are\nTotal confirmed cases: " + total +"Which includes:-\nActive cases: " + active +"Recovered: " + recovered + "Death cases: " + death)

    elif msg.isdigit():
        if(int(msg)>0 and int(msg)<31):
            statecases,statename=scrappingValues.statewise(msg)
            resp.message("Total no. of confirmed cases in "+statename+" are "+statecases)
            # resp.message("Ministry Of Health has withdrawn the state-wise data from the official website\nSorry for the inconvenience")
        else :
            resp.message("Invalid request please try giving request \n'Give info'\n and follow the instructions")
    else:
        resp.message("Invalid request please try giving request \n'Give info' or 'hi'\n and follow the instructions")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)