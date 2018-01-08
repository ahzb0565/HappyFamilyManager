var React = require('react');

function Button(props){
    return <button className="btn btn-primary" onClick={props.onClick}>{props.value}</button>;
};

function ButtonGroup(props){
    const style = props.style;
    return (
        <div className="btn-group"  style={style}>
            <Button onClick={props.create} value="新建" />
            <Button onClick={props.cancel} value="取消" />
        </div>
    );
};

function SmallButton(props){
    return <a className="badge" onClick={props.onClick} style={props.style}>{props.value}</a>;
};

module.exports = {
    Button: Button,
    ButtonGroup: ButtonGroup,
    SmallButton: SmallButton
};