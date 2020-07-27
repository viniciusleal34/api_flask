from flask import Flask, request, jsonify
from flask_cors import CORS
import os

UPLOAD_FOLDER_INDICE = os.path.join(os.getcwd(), 'static', 'upload')

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return" <h1> Hello world</h1>"
    if request.method == 'POST':
        data = request.files
      #  savePath = os.path.join(UPLOAD_FOLDER_INDICE, 'gg.jpg')
       # data.save(savePath)
        latitude = request.form
        print(data)
        print(latitude)
        return jsonify({"status": "ok"})


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",port=port)

if __name__ == "__main__":
    main()