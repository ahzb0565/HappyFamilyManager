import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

function Item(props){
    return (<a href={'/details/?date='+ props.report.date} className="list-group-item">
        <h4 className="list-group-item-heading">{props.report.date}</h4>
        <p className="list-group-item-text">总共{props.report.total}， 收入{props.report.income}， 支出{props.report.outcome}</p>
    </a>)
}

class Reports extends React.Component{
    constructor(){
        super();
        this.state = {reports: []};
    }

    getReports(){
        axios.get('/api/get_reports/')
            .then((response)=>{
                console.log(response.data);
                this.setState({reports: response.data});
            });
    }

    componentDidMount(){
        this.getReports();
    }

    render(){
        let reports = this.state.reports;
        let items = reports.map((item)=><Item key={reports.indexOf(item)} report={item} />)
        return (
            <div className="list-group">
                {items}
            </div>
        )
    }
}

ReactDOM.render(
    <Reports />,
    document.getElementById('reports')
);