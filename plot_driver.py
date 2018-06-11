# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask,request
from flask import Flask
import cherrypy
from paste.translogger import TransLogger
import re
from flask import jsonify
from flask_cors import CORS
import os,sys,glob
import pandas as pd
from tdirdlotmg.model.businesslogic import car_entry,car_exit
from tdirdlotmg.utils.comman_utils import generate_loggers
from tdirdlotmg.core.exception import format_exception
app = Flask(__name__)
app.debug = True
CORS(app)
app.url_map.strict_slashes = False

try:
    logger_path=os.path.dirname(os.path.realpath(__file__))+"Parkinglot.log"
    print(logger_path)
    logger = generate_loggers(log_path=logger_path)
except Exception:
    exp = format_exception()
    logger.error("Environment Properties Exception : %s" % exp)
    #sys.exit(1)



slotlist=["aa","ab","ac","ad","ae"]
slotdatapath="C:\\Users\\MADHU\\PycharmProjects\\Projectlotmg\\datap\\slotdata.csv"
exitdf=pd.read_csv(slotdatapath)
Total_no_slot=5

@app.route("/plot/carentry", methods=['POST'])
def Plms_carentry():
    try:
        logger.info("/plot/carentry Function")
        carid = request.json.get('carid')
        avial_slot,car_slotid=car_entry(slotdatapath,slotlist,exitdf,Total_no_slot,carid)
        if avial_slot==0:
            return jsonify(
            {'CarParrking_avialable_slot': avial_slot, "Status": "No Space"})
        else:
            return jsonify(
                {'CarParrking_avialable_slot': avial_slot, "car_slotid": car_slotid})
    except Exception:
        exp = format_exception()
        logger.error("Exception: %s" % exp)



@app.route("/plot/carexit", methods=['POST'])
def Plms_carexit():
    try:
        logger.info("/plot/carexit Function")
        carid = request.json.get('car_slotid')
        car_slotid,avial_slot=car_exit(slotdatapath,carid,exitdf)
        return jsonify(
                {'CarParrking_avialable_slot': avial_slot, "Remove_car_slotid": car_slotid})
    except Exception:
        exp = format_exception()
        logger.error("Exception: %s" % exp)

if __name__ == "__main__":
    app.run()
