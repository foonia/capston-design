from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import actions

@csrf_exempt
def fulfillment(request):
    action = request.JSON['result']['action']
    entities = request.JSON['result']['parameters']

    action_func = getattr(actions, action, None)

    if callable(action_func):
        return {'speech': action_func(**entities)}

    return JsonResponse({'speech': '잘못된 입력입니다. 다시 시도해주세요.'})






"""

{'id': '96c893f1-41e6-48f5-b247-e51e728d4fa6',
 'lang': 'ko',
 'result': {'action': 'stock_search',
            'actionIncomplete': False,
            'contexts': [],
            'fulfillment': {'messages': [{'speech': '', 'type': 0}],
                            'speech': ''},
            'metadata': {'intentId': 'b9300989-9e8d-46b7-874a-a84390b3c0d1',
                         'intentName': 'stock_search',
                         'isFallbackIntent': 'false',
                         'webhookForSlotFillingUsed': 'false',
                         'webhookUsed': 'true'},
            'parameters': {'stock_search_term': '테마별 시세'},
            'resolvedQuery': '테마별 시세 알려줘',
            'score': 1.0,
            'source': 'agent',
            'speech': ''},
 'sessionId': '8a1831ef-c958-6cd4-f1f0-febde94cabaa',
 'status': {'code': 200, 'errorType': 'success'},
 'timestamp': '2018-09-23T05:45:13.379Z'}
 
"""