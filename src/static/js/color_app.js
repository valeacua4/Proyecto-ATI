let boton = document.getElementById("guardar_app")
let color = document.getElementById("color_app")
let menu = document.getElementsByClassName("sidebar")
const cambiar = () => {
    boton.style.backgroundColor = color.value;
    menu[0].style.backgroundColor = color.value;    
    localStorage.setItem('color_fav',color.value)
}
if(boton!==null){
    boton.addEventListener("click",cambiar,false)
}

if(localStorage.getItem("color_fav")){
    let nuevo = localStorage.getItem("color_fav")
        boton !== null ?  (boton.style.backgroundColor = nuevo) : null
        color !== null ?  (color.value = nuevo) : null
        menu[0].style.background = nuevo;   
        console.log(nuevo)
}