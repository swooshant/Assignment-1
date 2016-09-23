import wolframalpha

def askWolfram(app_id, question):
	client = wolframalpha.Client(app_id)
	try:
		res = client.query(question)
		return (next(res.results).text)
	except:
		return ("Invalid Message/Question")