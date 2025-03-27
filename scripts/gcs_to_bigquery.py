from google.cloud.storage import Client
from google.cloud import bigquery
from datetime import datetime, timedelta
import json
import pandas as pd
import os
import sys
from dotenv import load_dotenv
import os

load_dotenv()

CRED_PATH = sys.argv[1]
BUCKET_NAME = os.getenv('BUCKET_NAME')
DATASET_ID = os.getenv('DATASET_ID')
TABLE_ID = os.getenv('TABLE_ID')

BLOB_NAME = 'earthquake_data_'+(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')+"_to_"+(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')+"_new"

def get_content_from_gcs():
    client = Client.from_service_account_json(CRED_PATH)
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.get_blob(BLOB_NAME)
    downloaded_json_file = json.loads(blob.download_as_text(encoding="utf-8"))
    return downloaded_json_file

def filter_data(data):
    earthquake_data = []
    for feature in data['features']:
        properies = feature['properties']
        geometry = feature['geometry']

        earthquake = {
            "mag": properies['mag'],
            "place":properies['place'],
            "time":properies['time'],
            "updated":properies['updated'],
            "tz":properies['tz'],
            "url":properies['url'],
            "detail":properies['detail'],
            "felt":properies['felt'],
            "cdi":properies['cdi'],
            "mmi":properies['mmi'],
            "alert":properies['alert'],
            "status":properies['status'],
            "tsunami":properies['tsunami'],
            "sig":properies['sig'],
            "net":properies['net'],
            "code":properies['code'],
            "ids":properies['ids'],
            "sources":properies['sources'],
            "types":properies['types'],
            "nst":properies['nst'],
            "dmin":properies['dmin'],
            "rms":properies['rms'],
            "gap":properies['gap'],
            "magType":properies['magType'],
            "type":properies['type'],
            "title":properies['title'],
            'latitude': geometry['coordinates'][0],
            'longitude': geometry['coordinates'][1],
            'depth': geometry['coordinates'][2]
            }
        earthquake_data.append(earthquake)
    return earthquake_data

def upload_to_bq(data,table_id):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CRED_PATH

    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    print(df.columns)

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    write_disposition="WRITE_TRUNCATE",  # Option: 'WRITE_APPEND' to append
    )

    # Upload DataFrame to BigQuery
    load_job = client.load_table_from_dataframe(
        df, table_id, job_config=job_config
    )

    # Wait for the job to complete
    load_job.result()  # Wait for the job to finish

    print(f"Data uploaded to {table_id} in BigQuery")

if __name__ == '__main__':
    data = get_content_from_gcs()
    earthquake_data = filter_data(data)
    upload_to_bq(earthquake_data, TABLE_ID)
