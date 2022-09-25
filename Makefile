
# - - - - - - - - - - - - - - - - - - - - - - - - -
# model

train:
	python -m trainer.trainer  # if the provided model.joblib does not load

# - - - - - - - - - - - - - - - - - - - - - - - - -
# api 🤖

run_api:
	uvicorn api.fast:app --reload

# - - - - - - - - - - - - - - - - - - - - - - - - -
# docker 🐳

# 🚨 1. set your correct project id in GCP_PROJECT_ID

# 🚨 2. for Apple Silicon machine (Mac M1)
#       - check if you are using an Apple Silicon machine:
#         👉 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/lewagon/setup/master/utils/macos_list_processor_type.sh)"
#       - if you are using an Apple Silicon machine
#         👉 run the additional docker_build_m1 step to build your image for production

GCP_PROJECT_ID=lewagon-batch-941
DOCKER_IMAGE_NAME=spotify
GCR_MULTI_REGION=eu.gcr.io
GCR_REGION=europe-west1

docker_params:
	@echo "project id: ${GCP_PROJECT_ID}"
	@echo "image name: ${DOCKER_IMAGE_NAME}"
	@echo "multi region: ${GCR_MULTI_REGION}"
	@echo "region: ${GCR_REGION}"

docker_build:
	docker build -t ${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME} .

docker_run:
	docker run -e PORT=8000 -p 8000:8000 ${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/spotify

# 🚨 additional step for apple silicon only (you will not be able to run this new image locally but it will work on production)
docker_build_m1:
	docker buildx build --platform linux/amd64 -t eu.gcr.io/lewagon-batch-941/spotify --load .

docker_push:
	docker push eu.gcr.io/lewagon-batch-941/spotify

docker_deploy:
	gcloud run deploy --image eu.gcr.io/lewagon-batch-941/spotify --platform managed --region europe-west1
