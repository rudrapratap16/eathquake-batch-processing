# Environment Variables Setup

This project requires several environment variables to be set in order to function correctly. These variables are used to connect to various services and configure the project behavior.

### Step 1: Create a `.env` File

In the root directory of your project, create a file named `.env`. This file will contain sensitive information such as bucket names and dataset IDs. Do not push this file to your GitHub repository, as it contains confidential credentials.

### Step 2: Define the Environment Variables

In the `.env` file, define the following environment variables:
- BUCKET_NAME='your_bucket_name' # Google Cloud Storage bucket name
- DATASET_ID='your_dataset_id' # BigQuery dataset ID
- TABLE_ID='your_table_id' # BigQuery table ID
