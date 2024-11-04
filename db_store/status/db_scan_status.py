from utils import db_connection as dc
from db_store.scan import db_scan_data as db
from services.status import scan_status as sc
from utils import scan_id

db = dc.get_db()
collection = db['scan_status']

status = sc.scan_response()
uoid = scan_id.generate_uoid()

def db_scan_status_data():
     status = sc.api_scan_status()
     uoid = scan_id.generate_uoid()
     start_time , end_time = db.resp_time()

     scan_status = {
          "_id" : uoid,
          "Start_Time" : start_time,
          "End_Time" : end_time,
          "status" : status
     }

     collection.insert_one(scan_status)
