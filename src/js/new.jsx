import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

let report = {};
let account_types = [];

function today(){
    // TODO: move to common
    let date = new Date();
    return date.toISOString().substr(0, 10);
}

// Get or create today's report
function init(){
    // Get account types
    axios.get('/api/get_acount_types/')
        .then(function(response){
            account_types = response.data;
            console.log('Account types=' + account_types);
        });
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
    if (!props.items)
        return null;
    console.log('Generate list group, items=' + props.items.map((item) => item.name));
    const items = props.items;
    const ListItems = items.map((item)=>{
        return (<Item key={item.name + '_' + items.indexOf(item)}
                    name={item.name}
                    value={item.value}
                    remove={props.removeItem} />)
    });
    return <ul className="list-group">
        <li className="list-group-item active">{props.type}<span style={{float: 'right'}}>+</span></li>
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

class Content extends React.Component{
    constructor(props, context){
        super(props, context);
        this.state = {
            month: today(),
            cashAndBackup: [],
            income: [],
            investment: [],
            insurance: []
        };
        this.submit = this.submit.bind(this);
        this.backHome = this.backHome.bind(this);
    }

    submit(){
        let items = [
            this.state.cashAndBackup,
            this.state.income,
            this.state.investment,
            this.state.insurance,
        ].reduce((a, b)=>a.concat(b));
        let items_left = items.length;
        for(let i = 0; i< items.length; i++){
            console.log('Creating item ' + items[i].name);
            axios.post('/api/create_item/', items[i])
                .then(function(response){
                    console.log(response);
                    items_left -= 1;
                    if (items_left <= 0)
                        this.backHome();
                });
        }
        console.log('Submitted');
    }

    backHome(){
        console.log('Back home');
        window.location.href = '/';
    }

    componentDidMount(){
        console.log('did mount');
        // create monthly report
        axios.get('/api/create_report/' + today() + '/')
            .then(function(response){
                console.log(response.data);
                const items = response.data.items;

            });
        const items = [
            {name: 'first', value: 100, type: 'cash', month: today()},
            {name: 'Second', value: 200, type: 'cash', month: today()},
            {name: 'third', value: 300, type: 'cash', month: today()}
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
                    <ButtonGroup create={this.submit} cancel={this.backHome} />
                </div>
            </div>
        );
    }
}

// Start from here
init();

ReactDOM.render(<Content />, document.getElementById('content'));