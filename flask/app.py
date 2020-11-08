#!/usr/bin/env python3

from flask import Flask, request, make_response, render_template

app = Flask(__name__)
got = "google.com"

def returnWeb(x):
	"""this func used to control the headers of the app"""
	if  ".html" in x:
		if x[-5:] ==  ".html":
			r = make_response(render_template(x))
			
	else:
		r = make_response(x)
	#r.headers.set("Server","Blank")
	r.headers['Server'] = "Apache/2.4.6 () OpenSSL/1.0.2k-fips PHP/7.2.7"
	return r


def deTag(tag):
	"""deTag Func for filtering input from js codes"""
	return tag.replace("<","&lt;").replace(">","&gt;")


@app.route("/",methods=["GET","POST"])
def index():
	if request.method == "GET":
		pass
	else:
		print("req form -- > ",request.form)
		
	r= returnWeb( "this New Script <br><h3>[script doesn't works , cuz of deTag Func]</h3><br>"+deTag(f"\
			<script>alert('js Don't run here')</script>[<a src={got}>]"))

	return r


@app.errorhandler(404)
def page_not_found(e):
    return "<h2>404 Error From Flask Server	!!!</h2>"



if __name__ == "__main__":
	app.run(debug=True, port=80, host="0.0.0.0")
