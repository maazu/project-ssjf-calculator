import React, { useEffect, useState } from 'react';

import { Layout, Input, Button } from 'antd';
import ButtonForm from '../form/buttonForm';
import FileInputForm from '../form/FileInputForm';

// Calculator imports
import ExecuteStep4 from '../Calculator/stepFour';
import modlimits from '../Calculator/modlimit';
import { squareRoot, squareRootCap } from '../Calculator/squareroot';
import { add, subtract, multiply, divide, factorial } from '../Calculator/add';

// use the component in your app!

//Content

const Content = () => {
  const { Header, Content, Footer } = Layout;
  const { TextArea } = Input;
  const [resultValue, setResultValue] = useState('');

  const [inputValues, setInputValues] = useState({
    testNumber: '',
    squareRoot: '',
    squareRootCap: '',
    modulelimits: '',
    add: '',
    subtract: '',
    multiply: '',
    divide: '',
    factorial: '',
    additionalRunningLog: '',
    stepFourData: '',
  });

  function handleChange(evt) {
    const value = evt.target.value;

    setInputValues({
      ...inputValues,
      [evt.target.name]: value,
    });
  }

  useEffect(() => {}, [inputValues]);

  return (
    <Layout>
      <Header style={{ backgroundColor: '#f0f2f5' }}>
        <title>Project SSJF</title>
        <meta name='description' content='Project ssjf' />
      </Header>

      <Content
        style={{
          padding: '0% 12%',
        }}
      >
        <h1>Project SSJF</h1>
        <div style={{ backgroundColor: 'white', padding: '20px 20px' }}>
          <FileInputForm
            label='Enter Test Number'
            inputName='testNumber'
            inputValues={inputValues}
            handleInputChange={handleChange}
            placeholder={'937'}
          />
          <FileInputForm
            buttonText='Module Limits'
            inputName='modulelimits'
            inputValues={inputValues}
            placeholder={'E.g 1,4,7,8,9,7'}
            handleInputChange={handleChange}
            buttonLabel={true}
            buttonAction={() => setResultValue(modlimits(inputValues))}
          />
          <ButtonForm
            buttonText='SquareRoot'
            inputName='squareRoot'
            placeholder='Square root'
            buttonAction={() =>
              setResultValue(squareRoot(inputValues.squareRoot))
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <ButtonForm
            buttonText='SquareRootCap'
            inputName='squareRootCap'
            placeholder='SquareRoot cap'
            buttonAction={() =>
              setResultValue(squareRootCap(inputValues.squareRootCap))
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <ButtonForm
            buttonText='Add'
            inputName='add'
            placeholder='E.g 212'
            buttonAction={() =>
              setResultValue(add(inputValues.testNumber, inputValues.add))
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <ButtonForm
            buttonText='Subtract'
            inputName='subtract'
            placeholder='E.g 212'
            buttonAction={() =>
              setResultValue(
                subtract(inputValues.testNumber, inputValues.subtract)
              )
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <ButtonForm
            buttonText='Divide'
            inputName='divide'
            placeholder='E.g 21432342'
            buttonAction={() =>
              setResultValue(divide(inputValues.testNumber, inputValues.divide))
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <ButtonForm
            buttonText='Multiply'
            inputName='multiply'
            placeholder='E.g 21432342'
            buttonAction={() =>
              setResultValue(
                multiply(inputValues.testNumber, inputValues.multiply)
              )
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <ButtonForm
            buttonText='Factorial'
            inputName='factorial'
            placeholder='E.g 3434'
            buttonAction={() =>
              setResultValue(factorial(inputValues.factorial))
            }
            handleInputChange={handleChange}
            inputValues={inputValues}
          />
          <Button
            style={{ width: '100%' }}
            type='primary'
            onClick={() =>
              setResultValue(ExecuteStep4(inputValues, setInputValues))
            }
          >
            Execute Step 4
          </Button>
          <br /> <br />
          <h3>Result</h3>
          <TextArea
            rows={4}
            disabled
            placeholder='Result'
            value={resultValue}
          />
          <br /> <br />
          <h3>Program Progress</h3>
          <TextArea
            rows={10}
            disabled
            placeholder='Additional Log'
            value={inputValues.additionalRunningLog}
          />
          <br /> <br />
          <p>
            &#42; Number greater than 1.7976931348623157e+308 will be displayed
            as Infinity.
          </p>
        </div>
      </Content>

      <Footer></Footer>
    </Layout>
  );
};

export default Content;
