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

// Start from here
init();
