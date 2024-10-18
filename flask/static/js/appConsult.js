function consult_user(){
   let id = document.getElementById("ident"),value
   fetch('/consult_user', {
     'method': 'post',
     'headers': {'content-Type':'aplication/json'},
     'body': JSON.stringify(id)
   })
}