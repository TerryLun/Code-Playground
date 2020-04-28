from flask import Flask, render_template, request, redirect
import nexmo

API_KEY = '29492de1'
API_SECRET = 'SECRET STRING'
NEXMO_NUMBER = '14372662415'

# Create a new Nexmo Client object:
client = nexmo.Client(key=API_KEY, secret=API_SECRET)

# Initialize Flask:
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send_sms():
    if request.method == 'POST':
        number = request.form['number']
        message = request.form['message']
        # send message
        client.send_message({
            'from': NEXMO_NUMBER,
            'to': number,
            'text': message,
        })
        return redirect('/')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
