from vapi_python import Vapi

# Function to read API key from file
def read_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Initialize Vapi client
vapi = Vapi(api_key=read_api_key('vapi_key.txt'))

# Define the assistant configuration
assistant = {
    "firstMessage": "Hello, I'm here to conduct an interview. Please provide your responses clearly.",
    "context": "You are an AI interviewer conducting an interview and summarizing responses.",
    "model": "gpt-3.5-turbo",
    "voice": "jennifer-playht",
    "recordingEnabled": True,
    "interruptionsEnabled": False,
    "analysis": {
        "summary": {
            "prompt": "Summarize the interviewee's response in 2-3 sentences, focusing on key points."
        }
    }
}

# List of interview questions
questions = [
    "Can you tell me about your background and experience?",
    "What are your strengths and weaknesses?",
    "Where do you see yourself in five years?"
]

interviewee_responses = ""

def handle_message(message):
    global interviewee_responses
    # If we are simulating inputs, manually ask for them
    if message['type'] == 'transcript':
        print(f"Interviewee: {message['text']}")
        interviewee_responses += message['text'] + " "
    elif message['type'] == 'status-update':
        print(f"Call status: {message['status']}")
        if message['status'] == 'completed':
            print_summary()

# Conduct the interview
for question in questions:
    print(f"\nInterviewer: {question}")
    response = input("Interviewee's Response: ")  # Prompt for the interviewee's response manually
    handle_message({"type": "transcript", "text": response})
    input("Press Enter to continue to the next question...")


def print_summary():
    call_details = vapi.get_call(call['id'])
    if 'analysis' in call_details:
        print("\nSummary of Interviewee's Response:")
        print(call_details['analysis'].get('summary', 'No summary available'))

# Start the Vapi call
call = vapi.start(assistant=assistant, on_message=handle_message)

# Conduct the interview
for question in questions:
    print(f"\nInterviewer: {question}")
    vapi.send_text(call['id'], question)
    input("Press Enter to continue to the next question...")

# End the call
vapi.stop()