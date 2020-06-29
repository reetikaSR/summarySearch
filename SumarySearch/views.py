from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SumarySearch.compute_match import match
from .serializers import BookSerializer
from django.http import HttpResponseBadRequest


@api_view(['POST'])
@csrf_exempt
def search_summary(request):
    """
    :param request: request with POST type and data with list of queries and number of results needed for each query.
    :return: response with the matching results of all the queries in the query list.
    """

    queries = request.data.getlist('queries', None)
    k = request.data.get('k')

    if not queries:
        return HttpResponseBadRequest("Missing required fields: queries")
    if not k:
        return HttpResponseBadRequest("Missing required fields: k")

    data = []

    for query in queries:
        matching_results = match(query, int(k))
        results_data = BookSerializer(matching_results, many=True, context={'query': query}).data
        data.extend(results_data)

    return Response(data)
