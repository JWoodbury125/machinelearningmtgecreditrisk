Method 2 Flask-1

400 error internal server error solved-Not transferring user input values from form to the app.py file

Reasons: References to variables were wrong 

Solved using
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwiz4NKWgI3hAhWPTN8KHU0KAtMQrAIoAzAAegQICRAK&url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F14105452%2Fwhat-is-the-cause-of-the-bad-request-error-when-submitting-form-in-flask-applica&usg=AOvVaw0p-rJ91bqjgTrgrBB-40lG


Snippet from website
Chuckles Sorry, should have been more clear - "Flask raises an HTTP error when it fails to find a key in the args and form dictionaries" - one of the fields you are trying to access in request.form is not there (e. g. you are sending name_feild and looking for name_field - note the mis-spelling), thus the error. (Setting app.debug = True will help you find the error). - Sean Vieira Jan 1 '13 at 3:11 


Solved after which 500 error occur

I changed from python version 3.7 to python version 2.7 as instructed by jennifer to resolve this error

