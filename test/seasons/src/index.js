import React from 'react';
import ReactDOM from 'react-dom/client';

import SeasonDisplay from './SeasonDisplay';
import Spinner from './Spinner';

const root = ReactDOM.createRoot(document.getElementById('root'));


class App extends React.Component {


    state = { lat: null, errorMessage: null };

    componentDidMount() {
        window.navigator.geolocation.getCurrentPosition(
            position => this.setState({ lat: position.coords.latitude }),
            err => this.setState({ errorMessage: err.message })
        );
    }

    render() {

        if (this.state.errorMessage) {
            return <div>Error: {this.state.errorMessage}</div>
        }
        if (this.state.lat) {
            return (
                <SeasonDisplay lat={this.state.lat} />
            );
        }
        return <Spinner message="Please accept the location request" />;
    }
}

root.render(<App />)