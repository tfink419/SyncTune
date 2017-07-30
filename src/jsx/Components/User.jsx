import React, { Component, PropTypes } from 'react';
import ReactDOM from 'react-dom';
// import Note from './Note.jsx';
// import NoteFeatures from './NoteFeatures.jsx';
import axios from 'axios';

export default class User extends Component {
  // static propTypes = {
    // text: PropTypes.string.isRequired
  // };

  // static defaultProps = {
    // minLength: 1,
    // maxLength: 256
  // };

  // state = {
    // text: this.props.text
  // };

  componentWillMount() {
  }

  componentWillReceiveProps(nextProps) {
    let nextState = { nextProps };
    this.setState(nextState);
  }

  componentDidUpdate(prevProps, prevState) {
  }
  
  logout(event) {
    console.log(event);
  };

  render() {
    return <div>
      {/* <Note />
      <NoteFeatures /> */}
      <button onClick={ this.logout } >Logout</button>
    </div>;
  }
}
