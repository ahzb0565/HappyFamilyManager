var React = require('react');
var buttons = require('./buttons.jsx');
var ButtonGroup = buttons.ButtonGroup;
var SmallButton = buttons.SmallButton;
var Button = buttons.Button;
var Modal = require('react-modal');

const customModalStyles = {
  content : {
    top                   : '50%',
    left                  : '50%',
    right                 : 'auto',
    bottom                : 'auto',
    width                 : '30%',
    marginRight           : '-50%',
    transform             : 'translate(-50%, -50%)'
  }
};

function Item(props){
    console.log('Generate list item, name=' + props.name);
    return (<li className="list-group-item">
        {props.name}
        <span style={{float: 'right'}}>
            {props.value}
            {!props.readOnly && <SmallButton onClick={props.remove} value="删除"/>}
        </span>
    </li>);
}

class AddItemModal extends React.Component {
  constructor(props) {
    super(props);
    this.props = props;

    this.state = {
      modalIsOpen: false,
      item: {name: null, value:0, type: this.props.type}
    };

    this.openModal = this.openModal.bind(this);
    this.afterOpenModal = this.afterOpenModal.bind(this);
    this.closeModal = this.closeModal.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  openModal() {
    this.setState({modalIsOpen: true});
  }

  afterOpenModal() {
    // references are now sync'd and can be accessed.
    this.subtitle.style.color = 'black';
  }

  handleInputChange(e){
    let key = e.target.name == 'name'? 'name': 'value';
    let value = e.target.value;

    this.setState((prev) => {
        let newState = prev.item;
        newState[key] = value;
        return newState;
    });
  }

  closeModal() {
    this.setState({modalIsOpen: false});
    console.log('close Modal');
  }

  render() {
    return (
      <div style={{float: 'right'}}>
        <Button onClick={this.openModal} value="添加"/>
        <Modal
          isOpen={this.state.modalIsOpen}
          onAfterOpen={this.afterOpenModal}
          onRequestClose={this.closeModal}
          style={customModalStyles}
          contentLabel="Example Modal"
        >

          <h2 ref={subtitle => this.subtitle = subtitle} style={{textAlign: 'center'}}>添加项目到{this.props.type}</h2>
          <br />
          <form>
            <div className="input-group">
              <span className="input-group-addon" id="basic-addon1">名称：</span>
              <input type="text" className="form-control"
                placeholder="Name" aria-describedby="basic-addon1" name="name"
                onChange={this.handleInputChange}
              />
            </div>
            <br />
            <div className="input-group">
              <span className="input-group-addon" id="basic-addon2">数量：</span>
              <input type="number" className="form-control" placeholder="Value"
                aria-describedby="basic-addon2" name="value"
                onChange={this.handleInputChange}
              />
            </div>
            <br />
            <ButtonGroup create={(e) => {
                e.preventDefault();
                this.props.createItem(this.state.item);
                this.closeModal();
            }} cancel={null} style={{float: 'right'}}/>
          </form>
        </Modal>
      </div>
    );
  }
}


function Account(props){
    console.log('Generate list group, items=' + props.items.map((item) => item.name));
    const items = props.items;
    const readOnly = props.readOnly;
    const headStyle = {
        backgroundColor: '#337ab7',
        color: '#fff'
    };
    const ListItems = items.map((item)=>{
        return (<Item key={item.name + '_' + items.indexOf(item)}
                    name={item.name}
                    value={item.value}
                    remove={() => props.removeItem(item.id)}
                    readOnly={props.readOnly} />)
    });
    return <ul className="list-group col-md-4">
        <li className="list-group-item" style={headStyle}>{props.type}
            {!readOnly && <AddItemModal createItem={props.addItem} type={props.type}/>}
        </li>
        {ListItems}
    </ul>;
}

module.exports = Account;