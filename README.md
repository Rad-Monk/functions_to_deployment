[![Makefile CI](https://github.com/Rad-Monk/functions_to_deployment/actions/workflows/makefile.yml/badge.svg)](https://github.com/Rad-Monk/functions_to_deployment/actions/workflows/makefile.yml)

# functions_to_deployment
 ### to call microservice
 use something like below
 """bash
 curl -X 'POST' \
  'https://automatic-tribble-pjjr79xqww7fx6p-8081.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsift",
  "length": 3
}'
 """

 ### contanerize using
 `docker build .`
 `docker image ls`

 ### run container
 `docker run -p 127.0.0.1:8080:8081 <Image-id>`
 get the image id from running the 2nd command from contanerize section

 ### invoke POST
`run invoke.sh`