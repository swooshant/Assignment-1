import wolframalpha

def askWolfram(app_id, message):
	client = wolframalpha.Client(app_id)
	try:
		res = client.query(message)
		return (next(res.results).text)
	except:
		return ("Invalid Message/Question")