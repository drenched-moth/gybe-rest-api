sudo docker run --rm     -v /home/toucanite/Documents/gybe-rest-api:/local openapitools/openapi-generator-cli generate     -i /local/gybe-rest-api-design.yaml     -g python-flask     -o /local/out/
