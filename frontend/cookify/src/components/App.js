import React, {useState, useEffect} from 'react';
import '../static/App.css';
import Heading from './Heading'
import Home from "./Home"
import RecipeDetailed from "./RecipeDetailed"
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

function App() {
    return (
        <Router>
            <div className="App">
                <Heading/>
                <Switch>
                    <Route path="/recipes/:id" component ={RecipeDetailed}>
                    </Route>
                    <Route path="/">
                        <Home/>
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}

export default App;
