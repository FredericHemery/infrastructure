du coup pour réaliser ce tp dans un premier temps en plus des app.py j'ai du ajouter des dockerfiles dans chaques services (user et order)

ajouter des requirements.txt pour ajouter le requests en dépendance injectée

mon jsonify ne prenais pas les tuples dans e service-user/app.py présenté sur la photo.
je l'ai remplacé par une liste de dict: return jsonify([
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
])

ensuite c'est bon, mon curl présente bien:
✗ curl http://127.0.0.1:5002/orders
{"orders":["Order 1 for Alice","Order 2 for Bob"]}