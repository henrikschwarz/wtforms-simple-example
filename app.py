from flask import render_template, Flask, jsonify
# forms are stored in the forms folder
from forms.questions import QuestionsForm


#Creating the flask "application"
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
## templates reload without "server restart"
app.config['TEMPLATES_AUTO_RELOAD'] = True

#A standard entry point to be served accepting both GET and POST calls.
@app.route("/", methods=["POST","GET"])
def questions():
    form = QuestionsForm(csrf_enabled=False)

    # If the form can be validated then return the data as json
    if form.validate_on_submit():
        return jsonify((form.data))


    return render_template("questions.html", form=form) # render the templates/questions.html page
	

if __name__=="__main__":
	app.debug = True;
	app.run(debug=true)