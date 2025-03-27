import requests
import json
from google.cloud import storage
from datetime import datetime, timedelta
import sys
from dotenv import load_dotenv
import os

load_dotenv()

cred_path = sys.argv[1]

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')+"&endtime="+(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

BUCKET_NAME = os.getenv('BUCKET_NAME')
BLOB_NAME = 'earthquake_data_'+(datetime.now() - timedelta(2)).strftime('%Y-%m-%d')+"_to_"+(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')+"_new"


def get_data_and_load_gcs(url, bucket_name, blob_name):

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        print(f'weather data available : {len(weather_data)}')
        storage_client = storage.Client.from_service_account_json(cred_path)
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(
            data=json.dumps(weather_data),
            content_type='application/json'
            )
        
        print(f"Data uploaded to GCS as {blob_name}")

    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")

get_data_and_load_gcs(URL, BUCKET_NAME, BLOB_NAME)