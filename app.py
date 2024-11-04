#!/usr/bin/env python
from flask import Flask, render_template, request
import os
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
   result = ''
   if request.method == "POST":
      try:
         expression = request.form["display"]
         # Evaluate the expression safely using eval
         result = eval(expression)
      except Exception as e:
         result = "Error"
   return render_template("index.html", result=result)

if __name__ == "__main__":
   port = int(os.environ.get('PORT', 9000))
   app.run(debug=True, host='0.0.0.0', port=port)