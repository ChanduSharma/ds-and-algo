import React from "react";
import ReactDOM from "react-dom/client";

function getButtonText() {
    return { text: "hello" }
}
const App = () => {
    return (
        <div>
            <label className="label" htmlFor="name">Enter Name</label>
            <input id="name" type="text" />
            <button style={{ backgroundColor: 'blue', color: 'white' }}>{getButtonText().text}</button>
        </div >
    );
};

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<App />);