let name = "Pranay masulkar"
let age = 32
let experience = 7

console.log(`My name is ${name} and i have ${experience} years of experience nad i am ${age} yers old.`)

// data types in javascript
let string = "pranay"
let numbe = 30
let floatalsoNumber = 35.5
let boolean = true
let none = null
let array = [23,43,545]
let object = {name: "Pranay", age: 32}
let udefined = undefined

console.log(`These are the deferant types in javascript. String - ${string}, Number - ${numbe}, float also ins the number like, 30.4, -23, -43.5, 442424 these all are number in javascript ${floatalsoNumber}, boolean - ${boolean}, none - ${none}, array - ${array}, object - ${object}, undefind - ${udefined}`);

// Type checking in javascript

console.log(typeof string, typeof numbe, typeof floatalsoNumber, typeof boolean, typeof none, typeof array, typeof object, typeof undefined);

//type conversion
let years = "30"
console.log(typeof years)
console.log(typeof Number(years))

// Assignment in js
let student = {
    sname :"Pranay Masulkar",
    age : 32,
    city: "Tumsar",
    percentage: 67,
    course_name: "Python + JS",
    enrolled: true
}

console.log(student.sname, student.age, student.city, student.percentage, student.course_name, student. enrolled)

// Basic calculator

let a = 23
let b = 3
console.log(a + b)
console.log(a - b)
console.log(a * b)
console.log(a % b)
console.log(a ** b)
console.log(a / b);

//   Type conversion in js
let price = "1500"
let quantity = "3"
console.log(Number(price) * Number(quantity));