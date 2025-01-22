from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calculate(request):
    if request.method == "POST":
        expression = request.POST.get('expression', '')

        # Reset calculator if "C" is pressed
        if expression == "C":
            request.session['current_expression'] = ''  # Reset session variable
            return render(request, 'calculator.html', {'result': ''})

        # Perform calculation if "=" is pressed
        if expression == "=":
            try:
                # Safely evaluate the mathematical expression
                result = eval(request.session.get('current_expression', '0'))
                request.session['current_expression'] = ''  # Reset after evaluation
                return render(request, 'calculator.html', {'result': result})
            except Exception:
                return render(request, 'calculator.html', {'result': 'Error'})

        # Append to the current expression
        current_expression = request.session.get('current_expression', '') + expression
        request.session['current_expression'] = current_expression
        return render(request, 'calculator.html', {'result': current_expression})

    return render(request, 'calculator.html')
