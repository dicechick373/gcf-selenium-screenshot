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


