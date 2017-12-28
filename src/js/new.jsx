import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

let report = {};
let account_types = [];

// Get or create today's report
function init(){
    const today = ()=>{
        let date = new Date();
        return date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate();
    };
    // create monthly report
    axios.get('/api/create_report/' + today() + '/')
        .then(function(response){
            report = response.data;
            console.log('Create report success, report='+report);
        });
    // Get account types
    axios.get('/api/get_acount_types/')
        .then(function(response){
            account_types = response.data;
            console.log('Account types=' + account_types);
        });
}

function Item(props){
    console.log('Generate list item, name=' + props.name);
    return (<li className="list-group-item">
        {props.name}<span style={{float: "right"}}>{props.value}</span>
    </li>);
}

function Account(props){
    if (!props.items)
        return null;
    console.log('Generate list group, items=' + props.items.map((item) => item.name));
    const items = props.items;
    const ListItems = items.map((item)=><Item key={item.name + '_' + items.indexOf(item)} name={item.name} value={item.value} />);
    return <ul className="list-group">
        <li className="list-group-item active">{props.type}<span style={{float: 'right'}}>+</span></li>
        {ListItems}
    </ul>;
}

class Content extends React.Component{
    constructor(){
        super();
        this.state = {
            cashAndBackup: [],
            income: [],
            investment: [],
            insurance: []
        };
        this.submit = this.submit.bind(this);
        this.cancel = this.cancel.bind(this);
    }

    submit(){
        console.log('Submitted');
    }
    cancel(){
        console.log('Canceled');
    }

    componentDidMount(){
        const items = [
            {name: 'first', value: 100, type: 'cash'},
            {name: 'Second', value: 200, type: 'cash'},
            {name: 'third', value: 300, type: 'cash'}
        ];
        this.setState({cashAndBackup: items});
        this.setState({income: items});
        this.setState({investment: items});
        this.setState({insurance: items});
    }

    render(){
        return(
            <div>
                <div id="content" className="row">
                    <div className="col-md-4">
                        <Account items={this.state.income} type="收入" />
                    </div>
                    <div className="col-md-4">
                        <Account items={this.state.cashAndBackup} type="现金备用金" />
                    </div>
                    <div className="col-md-4">
                        <Account items={this.state.investment} type="投资账户" />
                    </div>
                    <div className="col-md-4">
                        <Account items={this.state.insurance} type="保险账户" />
                    </div>
                </div>
                <div className="row">
                    <ButtonGroup create={this.submit} cancel={this.cancel} />
                </div>
            </div>
        );
    }
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

// Start from here
init();

ReactDOM.render(<Content />, document.getElementById('content'));