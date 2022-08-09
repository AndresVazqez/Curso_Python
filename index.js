console.log("Este es un msj de js")

let num= 37373473;

console.log(typeof(num));

(typeof(num) == "number") ? console.log("Es un numero") : console.log("");
if (typeof(num) == 'string')console.log("Es un String"); else console.log("")


array = ["Andres", "Juan", "Alex", "Javi", "Guille", "Aida"]

object = {
    name : "Andres",
    lastname: "Vazquez",
    age : 31
}

for (let i in array){
    console.log(i)
};

console.log("-------------------------------------------------");

for (let i of array){
    console.log(i)
};

console.log("---------------------- Object ---------------------------")

for (let i in object){
    console.log(`${i} ${object[i]}`)
}

array2 = [
    ["Andres", "Maria", "Juan"],
    ["Naranja", "Pera", "Manzana"],
    ["Toyota", "Mazda", "Seat"]
]

for (let i=0; i < array2.length; i ++){
    for (let j = 0; j < array2[i].length; j++){
        console.log(array2[i][j])
    }
}

console.log("_________________________________")

const saluda = (name) => "Hola desde la funcion que se auto ejecuta!! " + name

console.log(saluda("Andres"))