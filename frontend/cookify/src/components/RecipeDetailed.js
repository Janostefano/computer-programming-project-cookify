import React from 'react'
import {IoIosThumbsUp, IoIosThumbsDown} from 'react-icons/io'
import {FaRegClock} from 'react-icons/fa'
import axios from 'axios'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

export function StepIngredients(props) {

    function renderSteps(ingredients) {
        let list = [];
       ingredients.forEach((ingredient) => {
            list.push(<p className="single-ingredient">{ingredient.name + " " + ingredient.quantity + " " + ingredient.unit}</p>)
        });
        return list
    }

    return <div className="step-ingredients">
        <h5 className={props.isFirst ? "" : "mt-4"}>{props.step.name}</h5>
        {renderSteps(props.step.ingredient)}
    </div>
}

function StepInstructions(props) {
    return <div className="step-instructions">
        <h2>{props.name}</h2>
        <p></p>
    </div>
}

class RecipeDetailed extends React.Component {



    constructor(props) {
        super(props);
        this.state = {shareBarFixed: false, activeRecipe : false, currentRecipe : null};
        this.handleScroll = this.handleScroll.bind(this)
    };

    componentDidMount() {
        window.addEventListener("scroll", this.handleScroll)
        axios.get('http://127.0.0.1:8000/recipes/' + this.props.match.params.id + '/?format=json').then(res => {
            this.setState({currentRecipe: res.data, activeRecipe: true});
        }).catch((error) =>{console.log(error)});
    };

    componentWillUnmount() {
        window.removeEventListener("scroll", this.handleScroll)
    };

    handleScroll() {
        let relPosition = document.getElementById("shareBarDiv").getBoundingClientRect().y;
        if (relPosition < 0) {
            this.setState({shareBarFixed: true});
        } else {
            this.setState({shareBarFixed: false});
        }
    }

    renderSteps(steps, containsPrepareStep) {
        let stepsList = [];
        if (containsPrepareStep) {
            stepsList.push(<li></li>)
        }
        steps.forEach((step, index) => {
            stepsList.push(<div key={index}><h5>{"Step " + (index + 1) + ": " + step.name}</h5><p>{step.instruction}</p></div>)
        });

        return stepsList
    }

    renderIngredients(ingredients){
        let ingredientsList = [];
        ingredients.forEach((stepIngredient, index) => {
            if (index === 0){
                ingredientsList.push(<StepIngredients step = {stepIngredient} isFirst = {true}/>)
            } else {
                ingredientsList.push(<StepIngredients step = {stepIngredient} isFirst = {false}/>)
            }
        });

        return ingredientsList;
    }

    render() {
        return (!this.state.activeRecipe ? null : (<div className="container recipe-detailed-container">
            <div className="title-description mt-5">
                <h1>{this.state.currentRecipe.name}</h1>
                <div className="recipe-info mt-3">
                    <img className="avatar" src={"http://127.0.0.1:8000" + this.state.currentRecipe.photo} alt="avatar"/>
                    <Link to={"author"}>{"author"}</Link>
                    <p>Added on: {"15.03.2020"}</p>
                    <p>Difficulty: {this.state.currentRecipe.difficultyLevel}</p>
                </div>
                <h5 className="mt-3">{this.state.currentRecipe.description}</h5>
            </div>
            <div className="row photo-row mt-5">
                <div className="col-lg-1 col-md-2 col-sm-12 share-bar-div" id="shareBarDiv">
                    <div className={"sharebar" + (this.state.shareBarFixed ? " docked" : "")}>
                    <span className="button-span">
                        <a className="fixed-button">
                            <IoIosThumbsUp className = "sharebar-icon"/>
                            <p>{this.state.currentRecipe.likes}</p>
                        </a>
                    </span>
                        <span>
                        <a className="fixed-button latter-button">
                            <FaRegClock className = "sharebar-icon"/>
                            <p>{Math.floor(this.state.currentRecipe.prepareTime / 60) + ":" + this.state.currentRecipe.prepareTime % 60}</p>
                        </a>
                    </span>
                        <span>
                        <a className="fixed-button latter-button"></a>
                    </span>
                        <span>
                        <a className="fixed-button latter-button"></a>
                    </span>
                    </div>
                </div>
                <div className="col-lg-11 col-md-10 col-sm-12  title-image">
                    <div className="row image-row">
                        <div className="col-md-8 col-sm-12 pr-0">
                            <img className="recipe-detailed-image" src={"http://127.0.0.1:8000" + this.state.currentRecipe.photo} alt={this.state.currentRecipe.name + "photo"}/>
                        </div>
                    </div>
                    <div className="row steps-row">
                        <div className="col-lg-3 col-md-12 ingredients-table mt-3">
                            {this.renderIngredients(this.state.currentRecipe.stepIngredients)}
                        </div>
                        <div className="col-lg-9 col-md-12 step-instructions mt-3">
                            {this.renderSteps(this.state.currentRecipe.instructions, false)}
                        </div>
                    </div>
                </div>
            </div>


        </div>))
    }
}

export default RecipeDetailed
