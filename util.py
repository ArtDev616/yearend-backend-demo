from flask import Response, json
def custom_response(res, status_code, status_msg):

	return Response(
		mimetype="application/json",
		response=json.dumps({ 'status_code': status_code, 'status_msg': status_msg, 'data':res }),
		status=status_code
	)
