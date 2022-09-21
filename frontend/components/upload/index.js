import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';
import React from 'react';

const props = {
  name: 'file',
  action: 'https://www.mocky.io/v2/5cc8019d300000980a055e76',
  headers: {
    authorization: 'authorization-text',
  },

  onChange(info) {
    if (info.file.status !== 'uploading') {
      console.log(info.file, info.fileList);
    }

    if (info.file.status === 'done') {
      message.success(`${info.file.name} file uploaded successfully`);
    } else if (info.file.status === 'error') {
      message.error(`${info.file.name} file upload failed.`);
    }
  },
};

const UploadButton = () => (
  <Upload {...props}>
    <Button
      style={{ width: '100%', marginLeft: '10px' }}
      icon={<UploadOutlined style={{ marginLeft: '0px' }} />}
    >
      Read From File
    </Button>
  </Upload>
);

export default UploadButton;
