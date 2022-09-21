export const add = (number1, number2) => {
  return parseFloat(number1) + parseFloat(number2);
};

export const multiply = (number1, number2) => {
  return parseFloat(number1) * parseFloat(number2);
};

export const subtract = (number1, number2) => {
  return parseFloat(number1) - parseFloat(number2);
};

export const divide = (number1, number2) => {
  return parseFloat(number1) / parseFloat(number2);
};

export const factorial = (n) => {
  let answer = 1;
  if (n == 0 || n == 1) {
    return answer;
  } else {
    for (var i = n; i >= 1; i--) {
      answer = answer * i;
    }
    return answer;
  }
};
