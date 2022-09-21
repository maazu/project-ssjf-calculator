import { count, mod } from 'mathjs';

const ExecuteStep4 = (values, setInputValues) => {
  const modResultArray = [];
  const modResultWithNumber = [];
  const uniqueArray = [];
  const selectValue_List = [];
  const minusResultArray = [];
  const lists = [];

  const getMod = () => {
    for (const i = 1; i <= 36; i++) {
      const result = mod(i * i, 36);
      modResultArray.push(result);
      modResultWithNumber.push({ value: i, result: result });
    }
  };

  const getDifferenceArray = (values) => {
    console.log('values', values);
    const ModResult_compare = mod(values.testNumber, 36);
    for (const i = 0; i < uniqueArray.length; i++) {
      for (const j = 0; j < uniqueArray.length; j++) {
        const result = uniqueArray[j] - uniqueArray[i];
        result = mod(result, 36);
        if (result == ModResult_compare) {
          selectValue_List.push(uniqueArray[j]);
          selectValue_List.push(uniqueArray[i]);
        }
        minusResultArray.push(result);
      }
    }
  };

  const makeList = () => {
    selectValue_List.map((item, index) => {
      lists.push({ name: item, array: [], part: 0 });
    });
  };

  const fillListWithArray = () => {
    lists.map((itemI, indexI) => {
      modResultWithNumber.map((itemJ, indexJ) => {
        if (itemI.name == itemJ.result) {
          lists[indexI].array.push(itemJ.value);
        }
      });
    });
  };

  const divideList = () => {
    lists.map((item, index) => {
      const stop = false;
      const i = 1;
      const difference = item.array[1] - item.array[0];
      while (stop == false && i < item.array.length) {
        if (item.array[i] - item.array[i - 1] != difference) {
          const secondHalf = item.array.slice(i);
          lists[index].array = item.array.slice(0, i);
          lists[index].part = item.part + 1;
          const partValue = item.part;
          const val = item.name;

          lists.push({
            name: val,
            array: secondHalf,
            part: partValue + 1,
          });
          stop = true;
        } else {
          i++;
        }
      }
    });
  };

  const stepFour = (values, setInputValues) => {
    let startTime = performance.now();

    setInputValues({
      ...values,
      ['additionalRunningLog']: 'Findout Mod ......',
    });

    // mod 1 to 36
    getMod();
    console.log('Step 4 Step one', modResultWithNumber);

    //unique array
    uniqueArray = [...new Set(modResultArray)];
    setInputValues({
      ...values,
      ['additionalRunningLog']:
        'Findout Mod .....' +
        '\nComputing Unique Array .....' +
        '\nUnique array computation finished' +
        '\nComputing array by difference from unique array',
    });

    // make array by difference from unique array
    getDifferenceArray(values);
    console.log('selectValue_List', selectValue_List);
    setInputValues({
      ...values,
      ['additionalRunningLog']:
        'Findout Mod .....' +
        '\nComputing Unique Array .....' +
        '\nUnique array computation finished' +
        '\nComputing array by difference from unique array\n' +
        '\nArray by difference from unique array' +
        '\nMaking List with name started',
    });

    // make List with name
    makeList();
    console.log('lists', lists);
    setInputValues({
      ...values,
      ['additionalRunningLog']:
        'Findout Mod .....' +
        '\nComputing Unique Array .....' +
        '\nUnique array computation finished' +
        '\nComputing array by difference from unique array\n' +
        '\nArray by difference from unique array' +
        '\nMaking List with name started' +
        '\nMaking List with name completed',
    });

    // make List with array

    fillListWithArray();
    console.log('after update lists', lists);

    // make List with sub array equal difference
    setInputValues({
      ...values,
      ['additionalRunningLog']:
        'Findout Mod .....' +
        '\nComputing Unique Array .....' +
        '\nUnique array computation finished' +
        '\nComputing array by difference from unique array\n' +
        '\nArray by difference from unique array' +
        '\nMaking List with name started' +
        '\nMaking List with name completed' +
        '\nMaking List sub array with equal difference',
    });

    divideList();
    console.log('Step 4 Final List Pairs', lists);

    setInputValues({
      ...values,
      ['additionalRunningLog']:
        'Findout Mod ..... 1-36 range' +
        '\nComputing Unique Array .....' +
        '\nUnique array computation finished' +
        '\nComputing array by difference from unique array' +
        '\nArray by difference from unique array' +
        '\nMaking List with name started' +
        '\nMaking List with name completed' +
        '\nMaking List sub array with equal difference' +
        '\nSub part lists ....\nProcess completed',
    });

    const endTime = performance.now();
    return (
      lists +
      ' Step 4 Execution completed in ' +
      (endTime - startTime).toPrecision(4) +
      ' ms.'
    );
  };

  return stepFour(values, setInputValues);
};

export default ExecuteStep4;
