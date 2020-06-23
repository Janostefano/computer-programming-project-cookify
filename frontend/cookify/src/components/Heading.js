import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function Heading(props) {
    return <div>
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark navbar-adjust">
            <a className="navbar-brand" href="/">Cookify</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText"
                    aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarText">
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item active">
                        <Link to="/" className="nav-link">Home</Link>
                    </li>
                    <li className="nav-item">
                        <Link to="/contact" className="nav-link" href="/contact">Contact</Link>
                    </li>
                </ul>

            </div>
        </nav>
    </div>
}

export default Heading
