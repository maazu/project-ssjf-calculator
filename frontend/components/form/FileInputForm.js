import { Col, Button, Layout, Input } from 'antd';
import Column from '../grid';
import UploadButton from '../upload';

const FileInputForm = (props) => {
  const {
    buttonText,
    buttonAction,
    placeholder,
    label,
    inputValues,
    buttonLabel,
    inputName,
    handleInputChange,
  } = props;

  return (
    <>
      <Column>
        <Col span={6}>
          {buttonLabel === true ? (
            <Button
              style={{ width: '95%' }}
              type='primary'
              onClick={buttonAction}
            >
              {buttonText}
            </Button>
          ) : (
            <h3>{label} &#42;</h3>
          )}
        </Col>
        <Col span={12}>
          <Input
            placeholder={placeholder}
            name={inputName}
            value={inputValues[inputName]}
            onChange={handleInputChange}
          />
        </Col>
        <Col span={6}>
          <UploadButton />
        </Col>
      </Column>
      <br />
    </>
  );
};

export default FileInputForm;
