// Does my number look big in this?
function narcissistic(value) {
  arr = (""+value).split("").map(Number);
  s = 0;
  arr.forEach(n => s += Math.pow(n, arr.length));
  return value == s;
}

// Тест для локального запуска https://jsbin.com/?js,console
test = 371;
console.log("Тестовые данные:");
console.log(test);
console.log("Результат:");
console.log(narcissistic(test));

// Лучшие решения:
// const narcissistic = value => +(''+value).split('').reduce((s,n,_,a)=>s + Math.pow(n,a.length),0) == value
// narcissistic = num => num.toString().split("").reduce(function(prev,el) { return prev + Math.pow(el, String(num).length)},0) == num;