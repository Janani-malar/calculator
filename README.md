Calculator Application

This is a simple calculator web application built using Django. The application allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. It also includes a clear button to reset calculations.



Features:

  Perform basic arithmetic operations: +, -, *, /

  Display results dynamically

  Clear previous calculations

  User-friendly interface


Technologies Used:

  Backend: Django (Python)

  Frontend: HTML, CSS

  Session Management: Django session framework
  

Installation:

1.Clone the Repository

git clone <repository_url>
cd calculator

2.Create a Virtual Environment

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

3.Install Dependencies

pip install -r requirements.txt

4.Run Migrations

python manage.py migrate

5.Run the Development Server

python manage.py runserver

6.Access the Application
Open a web browser and go to:

http://127.0.0.1:8000/



Project Structure:

CalculatorApp/
├── calculator/
│   ├── __init__.py
│   ├── views.py        # Core logic for calculations
│   ├── urls.py         # URL routing
│   ├── templates/      # HTML files
│       ├── calculator.html  # Main calculator interface
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── ...


Usage Instructions:

1.Enter numbers and operators using the buttons on the calculator interface.

2.Press the = button to evaluate the expression.

3.Press the C button to clear the current calculation.

4.The result will be displayed in the input field.


Troubleshooting:

Issue: Calculator retains the previous input after pressing C.

Solution: Ensure that the session variable current_expression is reset when the C button is clicked. Refer to the logic in the views.py file:

if expression == "C":
    request.session['current_expression'] = ''  # Reset session variable
    return render(request, 'calculator.html', {'result': ''})


Future Enhancements:

  Add support for parentheses in expressions.

  Implement advanced operations like square root and exponentiation.

  Enhance UI/UX with JavaScript for real-time updates.

  Add a history feature to store and display past calculations.


License:

This project is licensed under the MIT License. Feel free to use and modify it as needed.



Contact:

For any questions or feedback, please contact:

 Email: jananimalarsoul@gmail.com

