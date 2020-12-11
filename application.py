from flask import Flask
from flask import request
app = Flask(__name__)
from .util import custom_response


@app.route("/api/price", methods=['POST'])
def calculatePrice():
  status_msg, status_code, result = '', 200, 0
  req_data = request.get_json()
  try:
    if "market_val" not in req_data or "quantity" not in req_data:
      raise ValueError('Missing Required Params')
    market_val = req_data['market_val']
    quantity = req_data['quantity']
    
    if market_val < 0 or quantity < 0:
      raise ValueError('Params are invalid')
    
    result = market_val * quantity
    status_code = 200
    status_msg = 'success'
  except ValueError as e:
    print(format(str(e)))
    status_code = 400
    status_msg = e
  except Exception as e:
    print(format(str(e)))
    status_code = 500
    status_msg = 'The Server API Error.'
  finally:
    return custom_response(result, status_code, status_msg)
