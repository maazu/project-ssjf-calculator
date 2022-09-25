import { message } from "antd";
import { calApi } from "../../pages/api/add";
export const add = async (file1, file2) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("numberTwoFile", file2);
  data.append("calFunction", "add");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const subtract = async (file1, file2) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("numberTwoFile", file2);
  data.append("calFunction", "subtract");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const multiply = async (file1, file2) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("numberTwoFile", file2);
  data.append("calFunction", "multiply");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const divide = async (file1, file2) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("numberTwoFile", file2);
  data.append("calFunction", "divide");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const squareroot = async (file1, file2) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("numberTwoFile", file2);
  data.append("calFunction", "squareroot");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const modLimit = async (file1, file2) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("numberTwoFile", file2);
  data.append("calFunction", "step2");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const sqrCapLimit = async (file1) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("calFunction", "squarerootcap");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const factorial = async (file1) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("calFunction", "factorial");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
export const step4 = async (file1) => {
  const data = new FormData();
  data.append("testNumberFile", file1);
  data.append("calFunction", "step4");

  const res = await calApi(data);
  if (res.status === "success") {
    message.success(res.message);
    return res.data;
  } else {
    message.error(res.message);
  }
};
