
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .features.basic_functions import compute_addition, compute_exponent, compute_mutliplication, compute_squareroot, compute_subtraction, compute_division, compute_factorial
from .features.step_two import compute_step_two
from .features.step_three import compute_step_three
from .features.step_four import compute_step_four


@api_view(['GET', 'POST'])
def calulator_funtions(request):
    if request.method == 'POST':

        request_payload = request.data

        compute_function = request_payload['calFunction']

        if compute_function == 'add':
            result = compute_addition(request_payload)

        elif compute_function == 'subtract':
            result = compute_subtraction(request_payload)

        elif compute_function == 'multiply':
            result = compute_mutliplication(request_payload)

        elif compute_function == 'divide' or compute_function == 'division':
            result = compute_division(request_payload)

        elif compute_function == 'squareroot':
            result = compute_squareroot(request_payload)

        elif compute_function == 'exponent':
            result = compute_exponent(request_payload)

        elif compute_function == 'factorial':
            result = compute_factorial(request_payload)

        elif compute_function == 'step2' or compute_function == 'modlimits':
            result = compute_step_two(request_payload)

        elif compute_function == 'step3':
            return compute_step_three(request_payload)

        elif compute_function == 'step4':
            result = compute_step_four(request_payload)

        elif compute_function == 'step5':
            result = 'In progress'

        else:
            result = 'Invalid Calculator function'

        return Response(str(result))
