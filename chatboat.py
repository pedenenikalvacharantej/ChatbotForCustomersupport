import re


rules = {
    'greeting': {
        'keywords': ['hello', 'hii', 'hey', 'greetings'],
        'response': 'Hello! How can I assist you with your order, refund, or account today?'
    },
    'goodbye': {
        'keywords': ['bye', 'goodbye', 'see you'],
        'response': 'Goodbye! Have a great day.'
    },
    'order_status': {
        'keywords': ['order status', 'where is my order', 'track my order'],
        'response': 'To check your order status, please provide your order number.'
    },
    'refund_policy': {
        'keywords': ['refund', 'return policy', 'money back'],
        'response': 'You can request a refund within 30 days of purchase. Please visit our website\'s refund section for more details.'
    },
    'account_help': {
        'keywords': ['account', 'password', 'login', 'username'],
        'response': 'For account issues, please contact our support team at support@example.com.'
    },
    'default': {
        'keywords': [],
        'response': "I'm sorry, I don't understand that. You can ask me about order status, refunds, or your account."
    }
}

def get_response(user_input):
    """
    Finds a response based on keywords in the user's input.
    """
    user_input = user_input.lower()
    
    for intent, data in rules.items():
        # Use regex to find a match for any of the keywords
        if any(re.search(r'\b' + keyword + r'\b', user_input) for keyword in data['keywords']):
            return data['response']
            
    return rules['default']['response']

def start_chat():
    """
    Main function to run the chatbot conversation.
    """
    print("Chatbot: Hello! I am your virtual assistant. Type 'bye' to exit.")
    
    while True:
        user_message = input("You: ")
        
        if any(re.search(r'\b' + bye_keyword + r'\b', user_message.lower()) for bye_keyword in rules['goodbye']['keywords']):
            print(f"Chatbot: {rules['goodbye']['response']}")
            break
            
        response = get_response(user_message)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    start_chat()