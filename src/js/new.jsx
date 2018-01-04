import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import Modal from 'react-modal'

let report = {};
let account_types = [];
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


function today(){
    // TODO: move to common
    let date = new Date();
    return date.toISOString().substr(0, 10);
}

function SmallButton(props){
    return <a className="badge" onClick={props.onClick} style={props.style}>{props.value}</a>;
}

function Item(props){
    console.log('Generate list item, name=' + props.name);
    return (<li className="list-group-item">
        {props.name}
        <span style={{float: 'right'}}>
            {props.value}
            <SmallButton onClick={props.remove} value="删除"/>
        </span>
    </li>);
}

function Account(props){
    console.log('Generate list group, items=' + props.items.map((item) => item.name));
    const items = props.items;
    const headStyle = {
        backgroundColor: '#337ab7',
        color: '#fff'
    };
    const ListItems = items.map((item)=>{
        return (<Item key={item.name + '_' + items.indexOf(item)}
                    name={item.name}
                    value={item.value}
                    remove={() => props.removeItem(item.id)} />)
    });
    return <ul className="list-group">
        <li className="list-group-item" style={headStyle}>{props.type}
            <AddItemModal createItem={props.addItem} type={props.type}/>
        </li>
        {ListItems}
    </ul>;
}

function Button(props){
    return <button className="btn btn-primary" onClick={props.onClick}>{props.value}</button>;
}

function ButtonGroup(props){
    const style = {float: 'right'};
    return (
        <div className="btn-group"  style={style}>
            <Button onClick={props.create} value="新建" />
            <Button onClick={props.cancel} value="取消" />
        </div>
    );
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
            }} cancel={null} />
          </form>
        </Modal>
      </div>
    );
  }
}

class Content extends React.Component{
    constructor(props, context){
        super(props, context);
        this.today = today();
        this.month = null;
        this.state = {items: []};
        this.types = [];
        this.submit = this.submit.bind(this);
        this.backHome = this.backHome.bind(this);
        this.addItem = this.addItem.bind(this);
        this.removeItem = this.removeItem.bind(this);
    }

    submit(){
        let items = this.state.items;
        let items_left = items.length;
        let self = this;
        for(let i = 0; i< items.length; i++){
            console.log('Creating item ' + items[i].name);
            axios.post('/api/create_item/', items[i])
                .then(function(response){
                    items_left -= 1;
                    if (items_left <= 0)
                        self.backHome();
                });
        }
        console.log('Submitted');
    }

    backHome(){
        console.log('Back home');
        window.location.href = '/';
    }

    addItem(item){
        console.log('add item');
        if(!item.id){
            const max = Math.max.apply(null, this.state.items.map((item) => item.id));
            item.id = max + 1;
        };
        item.month = this.today;
        this.setState((prev)=>{
            let prevItems = prev.items;
            prevItems.push(item);
            return {items: prevItems};
        });
    }

    removeItem(id){
        console.log('remove item');
        this.setState((prev) => ({items: prev.items.filter((item) => item.id != id)}));
    }

    componentDidMount(){
        console.log('did mount');
        let self = this;
        // Get types
        axios.get('/api/get_acount_types/')
        .then(function(response){
            self.types = response.data;
        });
        // create monthly report
        axios.get('/api/create_report/' + today() + '/')
            .then(function(response){
                self.setState({items: response.data.items});
            });
    }

    render(){
        const items = this.state.items;
        const accounts = {};
        this.types.forEach((type) => accounts[type] = []);
        this.state.items.forEach((item) => accounts[item.type].push(item));

        const accountList = Object.keys(accounts).map((type) => {
            return (<Account
                key={type}
                items={accounts[type]}
                type={type}
                removeItem={this.removeItem}
                addItem={this.addItem}
            />)
        });

        return(
            <div>
                <div id="content" className="row">
                    {accountList}
                </div>
                <div className="row">
                    <ButtonGroup create={this.submit} cancel={this.backHome} />
                </div>
            </div>
        );
    }
}

ReactDOM.render(<Content />, document.getElementById('content'));