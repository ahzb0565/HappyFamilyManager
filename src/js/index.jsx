import React from 'react';
import ReactDOM from 'react-dom';
import {Navbar} from 'react-bootstrap';


const navbarInstance = (
    <Navbar>
        <Navbar.Header>
            <Navbar.Brand>
                <a href="#">Happy Family Manager</a>
            </Navbar.Brand>
        </Navbar.Header>
    </Navbar>
);

ReactDOM.render(navbarInstance, document.getElementById('nav'));
