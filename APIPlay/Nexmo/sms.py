import nexmo

client = nexmo.Client(key='29492de1', secret='UoZqHZhgB9hRHpTt')

client.send_message({
    'from': '14372662415',
    'to': '1778_______',
    'text': 'Text notification test',
})
