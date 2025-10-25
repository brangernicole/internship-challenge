"""
Views for the API app
"""
from math import gcd
from functools import reduce
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LCMRequestSerializer, LCMResponseSerializer


def lcm(a, b):
    """Calculate the least common multiple of two numbers"""
    return abs(a * b) // gcd(a, b)


def calculate_lcm_range(x, y):
    """
    Calculate the least common multiple of all numbers in the range [x, y]
    
    Args:
        x: Start of the range (inclusive)
        y: End of the range (inclusive)
    
    Returns:
        The least common multiple of all numbers in the range
    """
    numbers = list(range(x, y + 1))
    result = reduce(lcm, numbers)
    return result


@api_view(['GET', 'POST'])
def calculate_lcm(request):
    """
    Calculate the least common multiple (LCM) of all numbers in a given range.
    
    GET Parameters:
        x: Starting number of the range
        y: Ending number of the range
    
    POST Body (JSON):
        {
            "x": <starting_number>,
            "y": <ending_number>
        }
    
    Returns:
        {
            "x": <starting_number>,
            "y": <ending_number>,
            "result": <lcm_result>
        }
    
    Example:
        GET /api/lcm/?x=1&y=10
        Returns: {"x": 1, "y": 10, "result": 2520}
    """
    
    # Get parameters from either GET query params or POST body
    if request.method == 'GET':
        x = request.query_params.get('x')
        y = request.query_params.get('y')
    else:  # POST
        x = request.data.get('x')
        y = request.data.get('y')
    
    # Prepare data for validation
    data = {'x': x, 'y': y}
    
    # Validate input
    serializer = LCMRequestSerializer(data=data)
    if not serializer.is_valid():
        return Response(
            {
                'error': 'Invalid input',
                'details': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Get validated data
    validated_data = serializer.validated_data
    x = validated_data['x']
    y = validated_data['y']
    
    try:
        # Calculate LCM
        result = calculate_lcm_range(x, y)
        
        # Prepare response
        response_data = {
            'x': x,
            'y': y,
            'result': result
        }
        
        response_serializer = LCMResponseSerializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {
                'error': 'Error calculating LCM',
                'details': str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
