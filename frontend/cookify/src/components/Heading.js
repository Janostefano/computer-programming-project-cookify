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
                    <li className="nav-item dropdown">
                        <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Recipes</a>
                        <div className="dropdown-menu">
                            <Link to="/recipes/breakfast" className="dropdown-item" href="/categories/breakfast/">Breakfast</Link>
                            <a className="dropdown-item" href="/categories/lunch/">Lunch</a>
                            <a className="dropdown-item" href="/categories/dinner/">Dinners</a>
                            <a className="dropdown-item" href="/categories/dessert">Desserts</a>
                            <a className="dropdown-item" href="/categories/snack/">Snacks</a>
                            <a className="dropdown-item" href="/categories/drink">Drinks</a>
                        </div>
                    </li>
                    <li className="nav-item">
                        <Link to="/account" className="nav-link" href="/account">Account</Link>
                    </li>
                </ul>

            </div>
        </nav>
    </div>
}

export default Heading
