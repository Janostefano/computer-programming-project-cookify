import React from 'react'
import Recipe from "./Recipe";
import CircularCategory from "./CircularCategory";
import axios from 'axios'

class Home extends React.Component {
    constructor(props) {
        super(props)
        this.state = {recipes: null, categories: null}
    }

    componentDidMount() {
        axios.get("http://127.0.0.1:8000/recipes/").then((res) => {
            this.setState({recipes: res.data})
        });
        axios.get("http://127.0.0.1:8000/recipes/categories/").then((res) => {
            this.setState({categories: res.data})
        })
    }

    renderTopRecipes(recipes) {
        let recipesList = [];
        let topThreeViews = [];
        let idsAlreadyAdded = [];

        recipes.forEach((recipe, index) => {
            if (index < 3) {
                topThreeViews.push({id: recipe.id, views: recipe.views, originalIndex: recipesList.length});
                idsAlreadyAdded.push(recipe.id);
                recipesList.push(<Recipe id={recipe.id}
                                         name={recipe.name}
                                         photoAddress={recipe.photo}
                                         views={recipe.views}
                                         likes={recipe.likes}
                                         prepareTime={recipe.prepareTime}/>)
            } else {
                topThreeViews.sort((a, b) => a.views - b.views);
                topThreeViews.forEach((viewsCount, indexNested) => {
                    if (recipe.views > viewsCount.views) {
                        if (idsAlreadyAdded.includes(recipe.id)) {
                            return;
                        }
                        topThreeViews[indexNested] = {
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

    renderTopCategories(categories) {
        let categoriesList = [];
        let topSixCategories = [];
        let idsAlreadyAdded = [];

        categories.forEach((category, index) => {
            if (index < 6) {
                topSixCategories.push({id: category.id, views: category.views, originalIndex: categoriesList.length});
                idsAlreadyAdded.push(category.id)
                categoriesList.push(<div className="col-lg-2 col-md-3 col-sm-4"><CircularCategory photo={category.photo}
                                                                                                  categoryName={category.name}
                                                                                                    id = {category.id}/>
                </div>)
            } else {
                topSixCategories.sort((a, b) => a.views - b.views);
                topSixCategories.forEach((viewsCount, indexNested) => {
                    if (idsAlreadyAdded.includes(category.id)) {
                        return;
                    }
                    if (category.views > viewsCount.views) {
                        topSixCategories[indexNested] = {
                            views: category.views,
                            originalIndex: viewsCount.originalIndex
                        };
                        categoriesList[viewsCount.originalIndex] = (
                            <div className="col-lg-2 col-md-3 col-sm-4"><CircularCategory photo={category.photo}
                                                                                          categoryName={category.name}/>
                            </div>);
                        idsAlreadyAdded.push(category.id)
                    }
                })
            }
        });

        return categoriesList;
    }

    render() {
        return (<div>
                <div className="container recipes-container">
                    <div className="row recipes-row">
                        {this.state.recipes ? this.renderTopRecipes(this.state.recipes) : null}
                    </div>
                </div>
                <div className="top-categories">
                    <h3>Top categories</h3>
                    <div className="container">
                        <div className="row categories-list">
                            {this.state.categories ? this.renderTopCategories(this.state.categories) : null}
                        </div>
                    </div>
                </div>
            </div>

        )

    }
}

export default Home