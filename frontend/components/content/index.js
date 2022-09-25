import React, { useEffect, useState } from "react";
import { Upload, message } from "antd";
import { Layout, Input, Button } from "antd";
import ButtonForm from "../form/buttonForm";
import FileInputForm from "../form/FileInputForm";
import { UploadOutlined } from "@ant-design/icons";
import { Col, Row } from "antd";
// Calculator imports
import ExecuteStep4 from "../Calculator/stepFour";
import modlimits from "../Calculator/modlimit";
import { squareRoot, squareRootCap } from "../Calculator/squareroot";
import {
  add,
  subtract,
  multiply,
  divide,
  squareroot,
  modLimit,
  sqrCapLimit,
  factorial,
  step4,
} from "../Calculator/add";

// use the component in your app!

//Content

const Content = () => {
  const { Header, Content, Footer } = Layout;
  const { TextArea } = Input;
  const [resultValue, setResultValue] = useState("");
  const [file1, setFile1] = useState();
  const [file2, setFile2] = useState();
  const [addResult, setAddResult] = useState();
  const [subResult, setSubResult] = useState();
  const [divResult, setDivResult] = useState();
  const [mulResult, setMulResult] = useState();
  const [sqrResult, setSqrResult] = useState();
  const [modLimitResult, setModLimitResult] = useState();
  const [sqrCapResult, setSqrCapResult] = useState();
  const [facResult, setFacResult] = useState();
  const [step4Result, setStep4Result] = useState();

  const [inputValues, setInputValues] = useState({
    testNumber: "",
    squareRoot: "",
    squareRootCap: "",
    modulelimits: "",
    add: "",
    subtract: "",
    multiply: "",
    divide: "",
    factorial: "",
    additionalRunningLog: "",
    stepFourData: "",
  });

  function handleChange(evt) {
    const value = evt.target.value;

    setInputValues({
      ...inputValues,
      [evt.target.name]: value,
    });
  }
  const addOperation = (file1, file2) => {
    add(file1, file2).then((result) => setResultValue(result));
  };
  const subOperation = (file1, file2) => {
    subtract(file1, file2).then((result) => setResultValue(result));
  };
  const divOperation = (file1, file2) => {
    divide(file1, file2).then((result) => setResultValue(result));
  };
  const mulOperation = (file1, file2) => {
    multiply(file1, file2).then((result) => setResultValue(result));
  };
  const sqrOperation = (file1, file2) => {
    squareroot(file1, file2).then((result) => setResultValue(result));
  };
  const modLimitOperation = (file1, file2) => {
    modLimit(file1, file2).then((result) => setResultValue(result));
  };
  const sqrCapOperation = (file1) => {
    sqrCapLimit(file1).then((result) => setResultValue(result));
  };
  const facOperation = (file1) => {
    factorial(file1).then((result) => setResultValue(result));
  };
  const step4Operation = (file1) => {
    step4(file1).then((result) => setResultValue(result));
  };

  useEffect(() => {}, [inputValues]);
  const props = {
    showUploadList: false,
    name: "file",
    action: "https://www.mocky.io/v2/5cc8019d300000980a055e76",
    headers: {
      authorization: "authorization-text",
    },
    beforeUpload: (file) => {
      const isCSV = file.type === "text/plain";
      if (!isCSV) {
        message.error(`${file.name} is not a txt file`);
        return Upload.LIST_IGNORE;
      } else {
        setFile1(file);
        const data = new FormData();
        data.append("file", file);
        message.success(`${file.name} sucessfully upload`);
      }
    },
  };
  const secondProps = {
    showUploadList: false,
    name: "file",
    action: "https://www.mocky.io/v2/5cc8019d300000980a055e76",
    headers: {
      authorization: "authorization-text",
    },
    beforeUpload: (file) => {
      const isCSV = file.type === "text/plain";
      if (!isCSV) {
        message.error(`${file.name} is not a txt file`);
        return Upload.LIST_IGNORE;
      } else {
        setFile1(file);
        const data = new FormData();
        data.append("file", file);
        message.success(`${file.name} sucessfully upload`);
      }
    },
  };
  return (
    <Layout>
      <Header style={{ backgroundColor: "#f0f2f5" }}>
        <title>Project SSJF</title>
        <meta name="description" content="Project ssjf" />
      </Header>

      <Content
        style={{
          padding: "0% 12%",
        }}
      >
        <h1>Project SSJF</h1>
        <div
          style={{
            backgroundColor: "white",
            padding: "20px 20px",
          }}
        >
          <div
            style={{
              display: "flex",
              rowGap: "20px",
              columnGap: "30px",
              flexDirection: "column",
              marginBottom: "50px",
              justifyContent: "center",
            }}
          >
            <div style={{ display: "flex" }}>
              <h3 style={{ marginRight: "30px", width: "270px" }}>
                Upload File for test number:
              </h3>
              <Upload {...props}>
                <Button type="primary">
                  <UploadOutlined />
                  Upload file for test number
                </Button>
              </Upload>
            </div>
            <div style={{ display: "flex" }}>
              <h3 style={{ marginRight: "30px", width: "270px" }}>
                Upload second File for operations:{" "}
              </h3>
              <Upload {...secondProps}>
                <Button type="primary">
                  <UploadOutlined />
                  Upload file for 2nd number
                </Button>
              </Upload>
            </div>
          </div>
          <div
            style={{
              display: "flex",
              rowGap: "20px",
              columnGap: "30px",
              flexWrap: " wrap",
              justifyContent: "center",
            }}
          >
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                sqrCapOperation(file1);
              }}
            >
              {"Square Root Cap operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                modLimitOperation(file1, file1);
              }}
            >
              {"Module limit operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                sqrOperation(file1, file1);
              }}
            >
              {"Squareroot operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                addOperation(file1, file1);
              }}
            >
              {"Add operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                subOperation(file1, file1);
              }}
            >
              {"Subtract operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                divOperation(file1, file1);
              }}
            >
              {"Divide operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                mulOperation(file1, file1);
              }}
            >
              {"Multiply operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                facOperation(file1, file1);
              }}
            >
              {"Factorial operation"}
            </Button>
            <Button
              style={{ width: "20%" }}
              type="primary"
              onClick={() => {
                step4Operation(file1, file1);
              }}
            >
              {"Step 4 operation"}
            </Button>
          </div>
          <br /> <br />
          <h3>Result</h3>
          <TextArea
            rows={4}
            disabled
            placeholder="Result"
            value={resultValue}
          />
          <br /> <br />
          <h3>Program Progress</h3>
          <TextArea
            rows={10}
            disabled
            placeholder="Additional Log"
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
