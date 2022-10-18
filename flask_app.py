from flask import Flask,jsonify,request
app=Flask(__name__)
contacts=[
    {
        'id':1,
        'name':u'Raghav',
        'contact':u'9823050256',
        'done':False
    },
    {
        'id':2,
        'name':u'Rahul',
        'contact':u'9823470507',
        'done':False
    }
]
@app.route("/add_data",methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Pls Provide the Data"
        },400)
    contact ={
            'id':contacts[-1]['id']+1,
            'name': request.json['name'],
            'contact':request.json.get('contact',""),
            'done':False
    }
    contacts.append(contact)
    return jsonify({
            "status":"success",
            "message":"Task Added Successfully"
        })
@app.route("/get_contact")
def get_contact():
    return jsonify({
        "data":contacts
    })
if(__name__=="__main__"):
    app.run(debug=True)