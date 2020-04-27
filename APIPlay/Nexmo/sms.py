# import nexmo
#
# client = nexmo.Client(key='29492de1', secret='UoZqHZhgB9hRHpTt')
#
# client.send_message({
#     'from': '14372662415',
#     'to': '1778_______',
#     'text': 'Text notification test',
# })

#
# from flask import Flask, render_template, request, redirect
# import nexmo
#
# NEXMO_API_KEY = '29492de1'
# NEXMO_API_SECRET = 'UoZqHZhgB9hRHpTt'
# NEXMO_NUMBER = '14372662415'
#
# # Create a new Nexmo Client object:
# client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
#
# # Initialize Flask:
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     """ A view that renders the Send SMS form. """
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
