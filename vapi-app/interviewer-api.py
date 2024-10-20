from flask import Flask, request, render_template
from vapi_python import Vapi

#app = Flask(__name__)

# Your VAPI assistant credentials
API_KEY = "ef315768-0514-4089-8c7e-17e831657af6"
ASSISTANT_ID = "cc4108b8-369e-4ece-8b69-58d09958da28"

# Initialize the VAPI assistant
#assistant = Assistant(api_key=API_KEY, assistant_id=ASSISTANT_ID)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     assistant_response = None
#     user_message = None

#     if request.method == 'POST':
#         # Get the message from the form
#         user_message = request.form.get('message')
        
#         # Send message to VAPI assistant and get response
#         if user_message:
#             response = vapi.send_message(user_message)
#             assistant_response = response.get('response', 'No response received')

    # Render the HTML template with the assistant's response
    
    # return render_template('index.html', user_message=user_message, assistant_response=assistant_response)

if __name__ == "__main__":
    vapi = Vapi(api_key=API_KEY)
    vapi.start(assistant_id=ASSISTANT_ID)
    # app.run(debug=True)
