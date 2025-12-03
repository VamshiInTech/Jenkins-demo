from myapp import application

@application.route('/')
def home():
    return "Hello Vamshi! This is your Flask app deployed with Docker."

