import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

var buttons = require('./common/buttons.jsx');
var ButtonGroup = buttons.ButtonGroup;
var Account = require('./common/account.jsx');


let report = {};
let account_types = [];

function getDate(){
    let url = new URL(location.href);
    return url.searchParams.get('date');
}

class Content extends React.Component{
    constructor(props, context){
        super(props, context);
        this.today = getDate();
        this.date = getDate();
        this.state = {items: []};
        this.types = [];
        this.backHome = this.backHome.bind(this);
        this.readOnly = true;
    }


    backHome(){
        console.log('Back home');
        window.location.href = '/';
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
        axios.get('/api/get_report/' + this.date + '/')
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
                removeItem={null}
                addItem={null}
                readOnly={this.readOnly}
            />)
        });

        return(
            <div>
                <div id="content" className="row">
                    {accountList}
                </div>
            </div>
        );
    }
}

function ShowDate(){
    return <span>{getDate()}</span>
}

ReactDOM.render(<Content />, document.getElementById('content'));
ReactDOM.render(<ShowDate />, document.getElementById('showdate'));