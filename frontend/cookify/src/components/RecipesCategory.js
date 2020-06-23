import Recipe from "./Recipe";
import React from "react";
import axios from "axios";


class RecipesCategory extends React.Component {
    constructor(props) {
        super(props)
        this.state = {recipes: false, activeRecipes:true}
    }

    componentDidMount() {
        console.log(this.props.match.params.id)
        axios.get('http://127.0.0.1:8000/recipes/categories/' + this.props.match.params.id + '/?format=json').then(res => {
            this.setState({recipes: res.data, activeRecipes: true});
        }).catch((error) => {
            console.log(error)
        });
    }

    renderTopRecipes(recipes){
    let recipesList = [];
    let topSixViews = [];
    let idsAlreadyAdded = [];

    recipes.forEach((recipe, index) => {
        if (index < 6) {
            topSixViews.push({id: recipe.id, views: recipe.views, originalIndex: recipesList.length});
            idsAlreadyAdded.push(recipe.id);
            recipesList.push(<Recipe id={recipe.id}
                                     name={recipe.name}
                                     photoAddress={recipe.photo}
                                     views={recipe.views}
                                     likes={recipe.likes}
                                     prepareTime={recipe.prepareTime}/>)
        } else {
            topSixViews.sort((a, b) => a.views - b.views);
            topSixViews.forEach((viewsCount, indexNested) => {
                if (recipe.views > viewsCount.views) {
                    if (idsAlreadyAdded.includes(recipe.id)) {
                        return;
                    }
                    topSixViews[indexNested] = {
                        id: recipe.id,
                        views: recipe.views,
                        originalIndex: viewsCount.originalIndex
                    };
                    idsAlreadyAdded.push(recipe.id);
                    recipesList[viewsCount.originalIndex] = (<Recipe id={recipe.id}
                                                                     name={recipe.name}
                                                                     photoAddress={recipe.photo}
                                                                     views={recipe.views}
                                                                     likes={recipe.likes}
                                                                     prepareTime={recipe.prepareTime}/>)
                }
            });
        }
    });
    return recipesList
}

    render() {
        return !this.state.activeRecipes ? null :
            <div>                <div className="top-categories">
                    <h1>Best recipes from the category</h1>
                    <div className="container">
                        <div className="row categories-list">
                            {this.state.recipes ? this.renderTopRecipes(this.state.recipes) : null}
                        </div>
                    </div>
                </div></div>
    }
}


export default RecipesCategory