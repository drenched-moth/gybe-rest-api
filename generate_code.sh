sudo docker run --rm \
     -v "$(pwd)":/local \
     --user $(id -u):$(id -g) \
     openapitools/openapi-generator-cli generate \
     -i /local/oas3.yaml \
     -g python-flask \
     -o /local/tmp
