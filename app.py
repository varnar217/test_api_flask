import time
from flask import Flask, jsonify, request

from read_json import read_districts , read_streets , read_volunteers
import sys
districts=[]
streets=[]
volunteers=[]

app = Flask(__name__)


@app.route("/districts", methods=["GET"])
def get_districts():
    data=[]
    j=1
    for i in districts:

        sert={"id":i,"title":districts[i]['title']}
        data.append(sert)


    return jsonify(data)


@app.route("/streets", methods=["GET"])
def api_district_list():
    districts_id = int(request.args.get("district"))
    text_404 = "No such districts id"
    dan=[]
    if str(districts_id) in districts:
        dan=districts[str(districts_id)]["streets"]
    else:
        data = {'status': text_404}
        return jsonify(data),404

    den_stret=[]
    ber=0
    for i in (dan):
        for j in streets:
            if i == int(j):
                bufer_key={'id':i,'title':streets[j]["title"],'volunteer':streets[j]["volunteer"]}
                den_stret.append(bufer_key)
    return jsonify(den_stret)



@app.route("/volunteers", methods=["GET"])
def api_volunteer_list():
    streets_id = int(request.args.get("streets"))
    text_404 = "No such streets id"
    dan=[]
    if str(streets_id) in streets:
        dan=streets[str(streets_id)]["volunteer"]
    else:
        data = {'status': text_404}
        return jsonify(data),404

    den_stret=[]
    ber=0
    for i in (dan):
        for j in volunteers:
            if i == int(j):
                bufer_key={'id':i,'name':volunteers[j]["name"],'userpic':volunteers[j]["userpic"],'phone':volunteers[j]["phone"] }
                den_stret.append(bufer_key)
    return jsonify(den_stret)



@app.route("/helpme", methods=["POST"])
def api_helpme_list():
    data_json = request.json
    bool_flag=False
    bufer_strets=[]
    bufer_volonter=[]
    bufer_volonterss=0

    try:
        int(data_json['district'])
        int(data_json['street'])
        int(data_json['volunteer'])
    except ValueError:
        return jsonify({"status":"Error json file"}),500

    if str(data_json['district']) in districts :
        bool_flag=True
        bufer_strets=districts[str(data_json['district'])]['streets']
    else:
        return jsonify({"status":"Error district  id file"}),404
    #return jsonify(data_json['street']),200

    if str(data_json['street']) in streets :
        bool_flag=True
        for ii in bufer_strets :
            if str(ii) == str(data_json['street']):
                bufer_volonter= streets[str(ii)]['volunteer']
    else:
        return jsonify({"status":"Error street  id file"}),404
    if len(bufer_volonter) == 0 :
        return jsonify({"status":"dont find volonter"}),404

    if str(data_json['volunteer']) in volunteers:
        for ii in bufer_volonter :
            if str(ii) == str(data_json['volunteer']):
                bufer_volonterss= volunteers[str(ii)]
    else:
        return jsonify({"status":"Error volunteers  id file"}),404

    if (bufer_volonterss) == 0 :
        return jsonify({"status":"dont find volonter"}),404


    if bool_flag :
        return jsonify({"status":"success"}),200

    return  jsonify({"status":"Error  file"}), 400




if __name__ == '__main__':

    districts=read_districts()
    streets=read_streets()
    volunteers=read_volunteers()
    app.run(debug=True, host='0.0.0.0')
