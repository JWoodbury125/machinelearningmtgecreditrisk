from flask import Flask, request
from baseline import calculate

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        income = None
        credit = None
        IncRat = None
        loan_amount = None
        ltv = None
        state = None
        year = None
        
        try:
            income = float(request.form["income"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["income"])
        try:
            credit = float(request.form["credit"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["credit"])
        try:
            IncRat = float(request.form["IncRat"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["IncRat"])
        try:
            loan_amount = float(request.form["loan_amount"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["loan_amount"])
        try:
            ltv = float(request.form["ltv"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["ltv"])
        try:
            year = float(request.form["year"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["year"])
        try:
            state = request.form["state"]
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(request.form["state"])
            
        # if number1 is not None and number2 is not None:
        if income and credit and IncRat and loan_amount and ltv and year and state:
            result = calculate(income, credit, IncRat, loan_amount, ltv, year, state)
            print(result)
            return '''
                <html>
                <head>
                <title>Baseline Deploy
                </title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" type="image/png" href="static/images/download.png" />
                <link rel="stylesheet" type="text/css" href="static/css/bootstrap.min.css">
                <link rel="stylesheet" type="text/css" href="static/css/font-awesome.min.css">
                <link rel="stylesheet" type="text/css" href="static/css/animate.css">
                <link rel="stylesheet" type="text/css" href="static/css/hamburgers.min.css">
                <link rel="stylesheet" type="text/css" href="static/css/animsition.min.css">
                <link rel="stylesheet" type="text/css" href="static/css/select2.min.css">
                <link rel="stylesheet" type="text/css" href="static/css/daterangepicker.css">
                <link rel="stylesheet" type="text/css" href="static/css/util.css">
                <link rel="stylesheet" type="text/css" href="static/css/main.css">
                </head>
                    <body>
                            <div class="container-contact100">
                            <div class="wrap-contact100">
                            <div class="contact100-form validate-form">
                                <p><font size="16">Status is <b>{result}</b></p>
                                <br>
                                <p><font size="8"><a href="/">Click here to calculate again</a>
                            </div>
                            </div>
                            </div>
                            <div id="dropDownSelect1"></div>
                            <script src="static/scripts/jquery-3.2.1.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/animsition.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/popper.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/bootstrap.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/select2.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script type="56aaf5e216eada531b10eb03-text/javascript">
                            		$(".selection-2").select2({
                            			minimumResultsForSearch: 20,
                            			dropdownParent: $('#dropDownSelect1')
                            		});
                            	</script>
                            <script src="static/scripts/moment.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/daterangepicker.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/countdowntime.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script src="static/scripts/main.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                            <script type="56aaf5e216eada531b10eb03-text/javascript">
                              window.dataLayer = window.dataLayer || [];
                              function gtag(){dataLayer.push(arguments);}
                              gtag('js', new Date());
                              gtag('config', 'UA-23581568-13');
                            </script>
                            <script src="https://ajax.cloudflare.com/cdn-cgi/scripts/a2bd7673/cloudflare-static/rocket-loader.min.js" data-cf-settings="56aaf5e216eada531b10eb03-|49" defer=""></script>
                    </body>
                </html>''' 
                     
    return '''
        <html lang="en">
        <head>
        <title>Baseline Deploy
        </title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" type="image/png" href="static/images/download.png" />
        <link rel="stylesheet" type="text/css" href="static/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="static/css/font-awesome.min.css">
        <link rel="stylesheet" type="text/css" href="static/css/animate.css">
        <link rel="stylesheet" type="text/css" href="static/css/hamburgers.min.css">
        <link rel="stylesheet" type="text/css" href="static/css/animsition.min.css">
        <link rel="stylesheet" type="text/css" href="static/css/select2.min.css">
        <link rel="stylesheet" type="text/css" href="static/css/daterangepicker.css">
        <link rel="stylesheet" type="text/css" href="static/css/util.css">
        <link rel="stylesheet" type="text/css" href="static/css/main.css">
        </head>
           <body>
                <div class="container-contact100">
                <div class="wrap-contact100">
                <form class="contact100-form validate-form" method="post" action=".">
                <span class="contact100-form-title">
                Machine Language Analysis<br>of Mortgage Credit Risk
                </span> 
                <span class="contact100-form-title-abstract">
                <a style="display: block; text-align:center; text-decoration-line: underline; font-family: Poppins-Bold; font-size: 18px; color: #333;" href="#">Download our Abstract<br></a>
                </span> 
                <span style="display: block; text-align:center; font-family: Poppins-Bold; font-size: 24px; color: #333;">
                Enter your details:
                </span> 
                    <div class="wrap-input100 validate-input" data-validate="Name is required">
                    <span class="label-input100">Income</span>
                    <input class="input100" type="text" name="income" placeholder="Enter Income between 10000 to 400000">
                    <span class="focus-input100"></span>
                    </div>
                    <div class="wrap-input100 validate-input" data-validate="Credit is required">
                    <span class="label-input100">Credit</span>
                    <input class="input100"  name="credit" placeholder="Enter Credit in between 0 to 7 Eg: 6">
                    <span class="focus-input100"></span>
                    </div>
                    <div class="wrap-input100 validate-input" data-validate="Income Ratio is required">
                    <span class="label-input100">Income Ratio</span>
                    <input class="input100"  name="IncRat" placeholder="Enter Income Ratio in between 0 to 2 Eg: 1.27">
                    <span class="focus-input100"></span>
                    </div>
                    <div class="wrap-input100 validate-input" data-validate="Loan Amount is required">
                    <span class="label-input100">Loan Amount</span>
                    <input class="input100"  name="loan_amount" placeholder="Enter Loan Amount">
                    <span class="focus-input100"></span>
                    </div>
                    <div class="wrap-input100 validate-input" data-validate="LTV is required">
                    <span class="label-input100">LTV </span>
                    <input class="input100"  name="ltv" placeholder="Enter LTV in between 0 to 1 Eg: 0.75">
                    <span class="focus-input100"></span>
                    </div>
                    <div class="wrap-input100 input100-select">
                    <span class="label-input100">Year</span>
                    <div>
                    <select class="selection-2" name="year">
                    <option>Select Year(between 2010-2017)</option>
                    <option>2010</option>
                    <option>2011</option>
                    <option>2012</option>
                    <option>2013</option>
                    <option>2014</option>
                    <option>2015</option>
                    <option>2016</option>
                    <option>2017</option>
                    </select>
                    </div>
                    <span class="focus-input100"></span>
                    </div>
                    <div class="wrap-input100 input100-select">
                    <span class="label-input100">State</span>
                    <div>
                    <select class="selection-2" name="state">
                    <option>Select State</option>
                    <option>Alabama</option>
                    <option>Alaska</option>
                    <option>Arizona</option>
                    <option>Arkansas</option>
                    <option>California</option>
                    <option>Colorado</option>
                    <option>Connecticut</option>
                    <option>Delaware</option>
                    <option>District of Columbia</option>
                    <option>Florida</option>
                    <option>Georgia</option>
                    <option>Hawaii</option>
                    <option>Idaho</option>
                    <option>Illinois</option>
                    <option>Indiana</option>
                    <option>Iowa</option>
                    <option>Kansas</option>
                    <option>Kentucky</option>
                    <option>Louisiana</option>
                    <option>Maine</option>
                    <option>Maryland</option>
                    <option>Massachusetts</option>
                    <option>Michigan</option>
                    <option>Minnesota</option>
                    <option>Mississippi</option>
                    <option>Missouri</option>
                    <option>Montana</option>
                    <option>Nebraska</option>
                    <option>Nevada</option>
                    <option>New Hampshire</option>
                    <option>New Jersey</option>
                    <option>New Mexico</option>
                    <option>New York</option>
                    <option>North Carolina</option>
                    <option>North Dakota</option>
                    <option>Ohio</option>
                    <option>Oklahoma</option>
                    <option>Oregon</option>
                    <option>Pennsylvania</option>
                    <option>Rhode Island</option>
                    <option>South Carolina</option>
                    <option>South Dakota</option>
                    <option>Tennessee</option>
                    <option>Texas</option>
                    <option>Utah</option>
                    <option>Vermont</option>
                    <option>Virginia</option>
                    <option>Washington</option>
                    <option>West Virginia</option>
                    <option>Wisconsin</option>
                    <option>Wyoming</option>
                    </select>
                    </div>
                    <span class="focus-input100"></span>
                    </div>
                    <div class="container-contact100-form-btn">
                    <div class="wrap-contact100-form-btn">
                    <div class="contact100-form-bgbtn"></div>
                    <button type="submit" class="contact100-form-btn">
                    <span>
                    Submit
                    <i class="fa fa-long-arrow-right m-l-7" aria-hidden="true"></i>
                    </span>
                    </button>
                    </div>
                    </div>
                </form>
                </div>
                </div>
                <div id="dropDownSelect1"></div>
                <script src="static/scripts/jquery-3.2.1.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/animsition.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/popper.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/bootstrap.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/select2.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script type="56aaf5e216eada531b10eb03-text/javascript">
                		$(".selection-2").select2({
                			minimumResultsForSearch: 20,
                			dropdownParent: $('#dropDownSelect1')
                		});
                	</script>
                <script src="static/scripts/moment.min.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/daterangepicker.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/countdowntime.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script src="static/scripts/main.js" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13" type="56aaf5e216eada531b10eb03-text/javascript"></script>
                <script type="56aaf5e216eada531b10eb03-text/javascript">
                  window.dataLayer = window.dataLayer || [];
                  function gtag(){dataLayer.push(arguments);}
                  gtag('js', new Date());
                  gtag('config', 'UA-23581568-13');
                </script>
                <script src="https://ajax.cloudflare.com/cdn-cgi/scripts/a2bd7673/cloudflare-static/rocket-loader.min.js" data-cf-settings="56aaf5e216eada531b10eb03-|49" defer=""></script>
            </body>
        </html>'''