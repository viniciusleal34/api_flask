import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time
from src.comparador import Reconhecer
from src.DescritorImagem import DescritorImagem

UPLOAD_FOLDER_INDICE = os.path.join(os.getcwd(), 'static', 'upload')

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return" <h1> Hello world</h1>"
    if request.method == 'POST':
        data = request.files['myPhoto']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img = ("IMG_{}.png".format(timestr))
        savePath = os.path.join(UPLOAD_FOLDER_INDICE, img)
        data.save(savePath)
        pessoa = DescritorImagem(savePath).gerarMatriz()
        latitude = request.form
        pessoaReconhecida = Reconhecer(pessoa).recoding()
        pessoaReconhecida = str(pessoaReconhecida)
        return jsonify({"status": pessoaReconhecida})



def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1",port=port, debug=True)

if __name__ == "__main__":
    main()