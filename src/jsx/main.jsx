const React = require('react');
const ReactDOM = require('react-dom');
const Login = require('./Components/Login.jsx').default;
const User = require('./Components/User.jsx').default;
const _ = require('lodash');

console.log(document.syncTuneUser);

ReactDOM.render(<div>
    <h1>SyncTune</h1>
    <Login /> 
    {/* { (document.syncTuneUser 
      && document.syncTuneUser.spotifyId) ? 
        <Login /> : <User />
    } */}
  </div>,
  document.getElementById('sync-tune')
);
