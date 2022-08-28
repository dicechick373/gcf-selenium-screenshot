# gcf-selenium-screenshot

## downroad

```bash
$ git clone https://github.com/dicechick373/gcf-selenium-screenshot.git
$ cd gcf-selenium-screenshot
$ unzip headless-chromium.zip
$ rm headless-chromium.zip
```

## setting

### deploy.sh

change REGION,FUNCTION_NAME and other

```sh
set -ex

# Set constants
REGION="asia-northeast2"
FUNCTION_NAME="selenium-screenshot"

# Deploy the Google Cloud Function
gcloud beta functions deploy ${FUNCTION_NAME} \
  --runtime python37 \
  --region ${REGION} \
  --trigger-http \
  --allow-unauthenticated \
  --memory 2GB \
  --entry-point main \
  --timeout=300s
```

### main.py

set YOUR_BUCKET_NAME

```py
bucket = storage_client.bucket('YOUR_BUCKET_NAME')
```


## deploy

```sh
$ sh deploy.sh
```

