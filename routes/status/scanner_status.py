from db_store.scan import db_scan_data as db
from bson import ObjectId
from flask import jsonify
from utils import db_connection as dc

collection = dc.get_collection()

def status_response(id):
     scan_data = collection.find_one({"_id": ObjectId(id)})

     if scan_data:
          scan_data[id] = str(scan_data['id'])
          return jsonify(scan_data)
     else:
          return jsonify({"error": "Data not found"}), 404