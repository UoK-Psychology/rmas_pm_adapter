import requests
import json
from rmas_adapter.conf import settings
import logging
    
def set_ethics_approved(proposal_id):
    '''
        Attempts to set the ethics_approved flag to True for the supplied
        proposal id.
        
        If the proposal doesn't exist then this will throw a ValueError.
        
        Doing this manually looks like:
        
        curl -v -H "Accept: application/json" -H 
        "Content-type: application/json" -X PUT 
        -d ' {"proposal":{"ethics_approved":"true"}}' http://0.0.0.0:3000/proposals/1.json
    '''
    headers = {'content-type': 'application/json', 'Accept':'application/json'}
    data = json.dumps({'proposal':{'ethics_approved':True}})
    
    new_application_request = requests.put(settings.PM_API_PROPOSAL_ENDPOINT % str(proposal_id), 
                                           data=data, 
                                           headers=headers)
    
    if new_application_request.status_code == 200: 
        logging.info('Sucesfully set the ethics_approved flag for id: %s' % str(proposal_id))
    else:
        logging.info('FAILED to set the ethics_approved flag for id: %s' % str(proposal_id))
        
        
        
        