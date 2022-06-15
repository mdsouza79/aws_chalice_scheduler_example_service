import os
import json
import datetime
from datetime import timezone
import requests
import uuid
from chalice import Response
from chalicelib.dbConnections import getDbConnection
from chalicelib.miscFunctions import processError

DEBUG_LOG_ENABLE = False

UNKNOWN_MSG_TYPE = 'unknown message type'
UNKNOWN_MSG_VER = 'unknown message version'
PARAMETER_MISSING = 'parameter missing'
DATABASE_ERROR = 'database error'
API_ERROR = 'api error'
UNKNOWN_ERROR = 'unknown error'

def mainService():
    responseMessage = {}
    responseSubMessage = {}
    try:
        print('Hi Malcolm there')

    except Exception as e:
        responseSubMessage['errorCode'] = 1
        responseSubMessage['errorMessage'] = 'some error message'
        responseMessage['type'] = 'error'
        responseMessage['message'] = responseSubMessage
        return Response(body=responseMessage, status_code=400, headers={'Content-Type': 'application/json'})