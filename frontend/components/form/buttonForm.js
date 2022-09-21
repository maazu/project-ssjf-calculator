import { Col, Button, Input } from 'antd';
import Column from '../grid';
import { useState } from 'react';
const ButtonForm = (props) => {
  const {
    buttonText,
    buttonAction,
    placeholder,
    inputName,
    inputValues,
    handleInputChange,
  } = props;

  return (
    <>
      <Column>
        <Col span={6}>
          <Button
            style={{ width: '95%' }}
            type='primary'
            onClick={buttonAction}
          >
            {buttonText}
          </Button>
        </Col>
        <Col span={18}>
          <Input
            placeholder={placeholder}
            name={inputName}
            value={inputValues[inputName]}
            onChange={handleInputChange}
          />
        </Col>
      </Column>
      <br />
    </>
  );
};

export default ButtonForm;
