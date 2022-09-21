const modlimits = (values) => {
  console.log('start wrokin', values);
  const testNumber = values.testNumber;
  const modlimits = values.modulelimits.split(',');
  if (testNumber == '' || modlimits == '') {
    alert('test number and module limit list required to test module limits');
    return;
  }
  const loopFlag = false;
  const result = 0;
  const counter = 1;
  while (loopFlag === false && counter < testNumber) {
    const remainder = testNumber % counter;
    const result_match_flag = modlimits.filter((item, index) => {
      return item == remainder;
    });
    if (result_match_flag.length > 0) {
      loopFlag = true;
    } else {
      counter++;
    }
  }
  console.log('module LIMIT is ===>', counter);
  return counter;
};

export default modlimits;
