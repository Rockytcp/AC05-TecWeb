function adicionar() {
    var time = document.getElementById("time").value;
    var lista = document.getElementById("lista").innerHTML;
    lista = lista +"<li>"+time+"</li>"; 
    document.getElementById("lista").innerHTML = lista;
}