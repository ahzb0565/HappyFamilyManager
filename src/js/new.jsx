import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

var buttons = require('./common/buttons.jsx');
var ButtonGroup = buttons.ButtonGroup;
var Account = require('./common/account.jsx');


let report = {};
let account_types = [];


function today(){
    // TODO: move to common
    let date = new Date();
    return date.toISOString().substr(0, 10);
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
        let items = this.state.items.filter((item) => isNaN(item.id));
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
            item.id = 'new_' + (this.state.items.length + 1);
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
        if(!isNaN(id)){
            axios.get('/api/delete_item/' + id + '/')
                .then(function(response){
                    console.log('remove item success on server');
                });
        };
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
        axios.get('/api/create_report/' + this.today + '/')
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
                readOnly={false}
            />)
        });

        return(
            <div>
                <div id="content" className="row">
                    {accountList}
                </div>
                <div className="row">
                    <ButtonGroup create={this.submit} cancel={this.backHome} style={{float: 'right'}}/>
                </div>
            </div>
        );
    }
}

ReactDOM.render(<Content />, document.getElementById('content'));