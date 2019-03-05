import React, { Component } from 'react';
import { connect } from 'dva';
import { Card, Button, Modal, Table, Row, Col, Form, Input, Select } from 'antd';

const Funds = Form.create({ name: 'add_fund' })(
  class extends Component {
    equityFund = '股票基金';

    monetaryFund = '货币基金';

    bondFund = '债券基金';

    mixedFund = '混合基金';

    state = {
      showModal: false,
      selectedRowKeys: [],
      funds: [],
    };

    constructor(props) {
      super(props);
      this.openModal = this.openModal.bind(this);
      this.handleOk = this.handleOk.bind(this);
      this.handleCancel = this.handleCancel.bind(this);
      this.onSelectChange = this.onSelectChange.bind(this);
      this.deleteSelected = this.deleteSelected.bind(this);
      this.deleteFund = this.deleteFund.bind(this);
    }

    componentDidMount() {
      this.fetchFundList();
    }

    fetchFundList = () => {
      const { dispatch } = this.props;
      dispatch({
        type: 'fund/fetchFunds',
      }).then(() => {
        const { fundList } = this.props;
        this.setState({
          funds: [...fundList],
        });
      });
    };

    deleteFund = id => {
      const { dispatch } = this.props;
      dispatch({
        type: 'fund/removeFund',
        id,
      }).then(() => {
        const { funds } = this.state;
        this.setState({
          funds: [...funds.filter(item => item.id !== id)],
        });
      });
    };

    openModal = () => {
      this.setState({
        showModal: true,
        newFund: {
          name: '',
          company: '',
          fundId: '',
          type: '',
        },
      });
    };

    handleOk = () => {
      const { form } = this.props;

      form.validateFields((err, values) => {
        if (!err) {
          const { dispatch } = this.props;
          dispatch({
            type: 'fund/addFund',
            payload: values,
          }).then(
            () => {
              this.setState({
                showModal: false,
              });
              this.fetchFundList();
            },
            error => {
              console.log('error', error);
            }
          );
        }
      });
    };

    handleCancel = () => {
      const { form } = this.props;
      form.resetFields();
      this.setState({
        showModal: false,
      });
    };

    onSelectChange = selectedRowKeys => {
      this.setState({ selectedRowKeys });
    };

    deleteSelected = () => {
      const { selectedRowKeys } = this.state;
      if (selectedRowKeys.length > 0) {
        selectedRowKeys.forEach(id => {
          this.deleteFund(id);
        });
      }
    };

    renderAddFundForm() {
      const {
        form: { getFieldDecorator },
      } = this.props;
      return (
        <Form layout="vertical">
          <Form.Item label="基金名称">
            {getFieldDecorator('name', {
              rules: [{ required: true, message: '请输入基金名称' }],
            })(<Input />)}
          </Form.Item>
          <Form.Item label="基金ID">
            {getFieldDecorator('fund_id', {
              rules: [
                { required: true, message: '请输入基金ID' },
                { required: true, message: '必须为数字', pattern: /\d+/ },
              ],
            })(<Input />)}
          </Form.Item>
          <Form.Item label="基金公司">
            {getFieldDecorator('company', {
              rules: [{ required: true, message: '请输入公司名称' }],
            })(<Input />)}
          </Form.Item>
          <Form.Item label="基金类型">
            {getFieldDecorator('type', {
              rules: [{ required: true, message: '请选择基金类型' }],
            })(
              <Select initialValue={this.equityFund} style={{ width: '100%' }}>
                <Select.Option value={this.equityFund}>{this.equityFund}</Select.Option>
                <Select.Option value={this.monetaryFund}>{this.monetaryFund}</Select.Option>
                <Select.Option value={this.bondFund}>{this.bondFund}</Select.Option>
                <Select.Option value={this.mixedFund}>{this.mixedFund}</Select.Option>
              </Select>
            )}
          </Form.Item>
        </Form>
      );
    }

    render() {
      const { loadingFunds, deletingFunds, addingFund } = this.props;
      const { selectedRowKeys, showModal, funds } = this.state;

      const form = this.renderAddFundForm();

      const rowSelection = {
        selectedRowKeys,
        onChange: this.onSelectChange,
      };

      const columns = [
        { title: 'ID', dataIndex: 'id' },
        { title: '基金名称', dataIndex: 'name' },
        { title: '基金ID', dataIndex: 'fund_id' },
        { title: '基金公司', dataIndex: 'company' },
        { title: '基金类型', dataIndex: 'type' },
      ];

      const tableData = funds.map(item => Object.assign({}, item, { key: item.id }));

      return (
        <Card loading={loadingFunds} title="基金列表">
          <Row
            gutter={24}
            type="flex"
            justify="space-between"
            align="middle"
            style={{ marginBottom: 5 }}
          >
            <Col>
              <Button
                onClick={this.deleteSelected}
                disabled={selectedRowKeys.length === 0}
                loading={deletingFunds}
              >
                删除基金
              </Button>
            </Col>
            <Col>
              <Button type="primary" onClick={this.openModal} loading={addingFund}>
                新增基金
              </Button>
            </Col>
          </Row>
          <Modal
            title="新增基金"
            visible={showModal}
            onOk={this.handleOk}
            onCancel={this.handleCancel}
          >
            {form}
          </Modal>
          <Table rowSelection={rowSelection} columns={columns} dataSource={tableData} />;
        </Card>
      );
    }
  }
);

export default connect(({ fund, loading }) => ({
  fundList: fund.list,
  loadingFunds: loading.effects['fund/fetchFunds'],
  deletingFunds: loading.effects['fund/removeFund'],
  addingFund: loading.effects['fund/addFund'],
}))(Funds);
