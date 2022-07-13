// Grasshopper - Summation

var summation = function (num) {
  s = 0;
  for (i = 1; i <= num; i++)
    s += i;
   return s;
}

// Тест для локального запуска https://jsbin.com/?js,console
test = 2;
console.log("Текстовая данные:");
console.log(test);
console.log("Результат:");
console.log(summation(test));

// Лучшее решение:
// const summation = n => n * (n + 1) / 2;