from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def fulfillment(request):
    print(request.JSON)
    intend = request.JSON['action']
    entities = request.JSON['parameters']

    print(intend)
    for entity in entities:
        print(entity)

    return JsonResponse({})

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