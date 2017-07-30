import React, { Component, PropTypes } from 'react';
import ReactDOM from 'react-dom';

export default class Login extends Component {
  constructor() {
    super();
    this.style = {
      width: '40ex'
    }
  }
  
  spotifyLogin() {
    window.location = "/login";
  }

  componentWillMount() {
  }

  componentWillReceiveProps(nextProps) {
    let nextState = { nextProps };
    this.setState(nextState);
  }

  componentDidUpdate(prevProps, prevState) {
  }
  
  render() {
    return <span style={this.style}>
      <input type='button' value='login' style={this.passwordInputStyle} onClick={this.spotifyLogin} />
    </span>;
  }
}
