from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.route('/')
def upload_form():
	return render_template('download.html')


@app.route('/download_attachment',methods= ["GET"])
def download_file():
	path = "G:\\requirements.txt"
	return send_file(path, as_attachment=True)


app.run(debug=False)