function f1(x,y){
  return x + y
}

function f2(x,y){
  return x*y
}

const f3 = function(x,y) {
  return x(10,20) + y(30,40)
}
console.log(f3(f1,f2))