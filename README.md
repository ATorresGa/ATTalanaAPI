Prueba Tecnica de Talana

endpoints 

-http://localhost:8080/ mensaje de bienvenida no se necesitan datos

-http://localhost:8080/talatrivia/create-user/ -> diccionario de datos

{
    "email":string,
    "password":string -> ej aA12345* 
} , POST

-http://localhost:8080/talatrivia/login/ ->
{
    "email":string
    "password":string
} , POST

-http://localhost:8080/talatrivia/get-users/ ->
GET

-http://localhost:8080/talatrivia/logout/ -> POST, no funciona por problemas de implementacion en la libreria

-http://localhost:8080/talatrivia/edit-user/ ->

{
    "email": string,
    "role":string,
    "triviaId":int
}

-http://localhost:8080/talatrivia/create-trivia/ ->

{
  "name": String,
  "description": String,
  "questions": [
    {
      "question": String,
      "correctAnswer": String,
      "difficulty": String->definido por enums,
      "answers": [
        {"answer":String},
        {"answer":String},
        {"answer":String},
        {"answer":String}
      ]
    },
   }
  ]
}, POST

-http://localhost:8080/talatrivia/get-questions-by-trivia/->obtiene las preguntas sin respuestas

{
    "id":int
}, GET

-http://localhost:8080/talatrivia/participate/->

{
    "userId":int,
    "answers":[
        {"answer":String},
    ]
}, POST

-http://localhost:8080/talatrivia/get_rank_by_trivia_id/->

{
    "triviaId":int
},POST
