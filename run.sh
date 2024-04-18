#!/bin/bash
# aquivo para rodar o flask
.  env/bin/activate

echo "Digite 1 para desenvolvimento e 2 para publicação"
read opcao

case $opcao in
1)
echo "Desenvolmento"
export FLASK_APP=flaskr
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=main.py
python3 -m flask run
;;
2)
export FLASK_APP=flaskr
export FLASK_APP=main.py
uwsgi --socket 0.0.0.0:5000 --protocol=http -w main:app
;;
*)
echo "Invalido"
;;
esac
