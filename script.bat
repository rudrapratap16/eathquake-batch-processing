@echo off

set CREDS_PATH=%1

echo Using credentials from: %CREDS_PATH%

echo Installing requirements from requirements.txt...
pip install -r requirements.txt

set GOOGLE_APPLICATION_CREDENTIALS=%CREDS_PATH%

echo GOOGLE_APPLICATION_CREDENTIALS is set to: %GOOGLE_APPLICATION_CREDENTIALS%

python scripts/upload_to_gcs.py %CREDS_PATH%

python scripts/gcs_to_bigquery.py %CREDS_PATH%

cd ./dbt_project

echo Current directory is: %cd%

dbt run --profiles creds/profiles.yml

