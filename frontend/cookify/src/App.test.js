import React from 'react';
import {shallow} from 'enzyme'
import App from './components/App';
import Home from './components/Home';
import Recipe from './components/Recipe'
import CircularCategory from "./components/CircularCategory";
import RecipeDetailed from "./components/RecipeDetailed";
import StepIngredient from "./components/RecipeDetailed";

it('should render without crashing', () => {
    shallow(<App/>)
});

describe('should render home page with lists of top recipes and categories (selected by views)', () => {

    it('should render home page', () => {
        shallow(<Home/>)
    });

    it('should render recipe based on props', () => {
        const wrap = shallow(<Recipe id={3} name="mock" likes={4} prepareTime={100}/>);
        expect(wrap.containsMatchingElement(<p>mock</p>)).toEqual(true);
        expect(wrap.containsMatchingElement(<img alt="mock"/>)).toEqual(true);
        expect(wrap.containsMatchingElement(<p>{4}</p>)).toEqual(true);
        expect(wrap.containsMatchingElement(<p>1:40</p>)).toEqual(true);
        expect(wrap.find('a').at(0).props().href).toEqual('/recipes/3');
    });

    it('should sort recipes basing on views', () => {
            const wrap = shallow(<Home/>);
            wrap.setState({
                recipes: [{
                    name: "Some recipe",
                    id: 1,
                    photoAddress: "some address",
                    views: 10,
                    likes: 15,
                    prepareTime: 100
                },
                    {
                        name: "This should not be included",
                        id: 2,
                        photoAddress: "some address",
                        views: 2,
                        likes: 15,
                        prepareTime: 100
                    },
                    {name: "Some recipe", id: 3, photoAddress: "some address", views: 5, likes: 15, prepareTime: 100},
                    {name: "Some recipe", id: 4, photoAddress: "some address", views: 11, likes: 15, prepareTime: 100}]
            });
            expect(wrap.containsMatchingElement(<Recipe name="This should not be included"/>)).toEqual(false)
        }
    );

    it('should sort categories based on views', () => {
        const wrap = shallow(<Home/>);
        wrap.setState({
            categories: [{id: 1, views: 10, photo: null, name: "some name"},
                {id: 2, views: 15, photo: null, name: "some name"},
                {id: 3, views: 9, photo: null, name: "some name"},
                {id: 4, views: 8, photo: null, name: "this should not be included"},
                {id: 5, views: 14, photo: null, name: "some name"},
                {id: 6, views: 14, photo: null, name: "some name"},
                {id: 8, views: 1, photo: null, name: "this should not be included"},
                {id: 9, views: 19, photo: null, name: "some name"},
            ]
        });
        expect(wrap.containsMatchingElement(<CircularCategory
            categoryName="this should not be included"/>)).toEqual(false)
    })

});

describe('should render recipe page with details', () => {

    it('should render detailed recipe page without crashing', () => {
        shallow(<RecipeDetailed match = {{params: {id: 1}}}/>)
    });

    it('should render detailed recipe based on data from api', () => {
        const wrap = shallow(<RecipeDetailed match = {{params: {id: 1}}}/>);
        wrap.setState({
            activeRecipe: true, currentRecipe: {
                name: "Test recipe",
                photo: "/no/",
                difficultyLevel: "hard",
                description: "Description of a recipe",
                likes: 2,
                prepareTime: 30,
                stepIngredients: [{
                    name: "ingredient 1",
                    quantity: 2,
                    unit: "some unit",
                    isFirst: true
                }, {name: "ingredient 2", quantity: 3, unit: "some unit"}],
                instructions: [{name: "step instruction 1", instruction: "do something"}, {
                    name: "step instruction 2",
                    instruction: "do something"
                }]
            }
        });
        expect(wrap.containsMatchingElement(<h1>Test recipe</h1>)).toEqual(true);
        expect(wrap.containsMatchingElement(<img className="recipe-detailed-image" alt = "Test recipephoto"  src = "http://127.0.0.1:8000/no/"/> )).toEqual(true);
        expect(wrap.containsMatchingElement(<h5>Description of a recipe</h5>)).toEqual(true);
        expect(wrap.containsMatchingElement(<p>0:30</p>)).toEqual(true);
        expect(wrap.containsMatchingElement(<h5>Step 1: step instruction 1</h5>)).toEqual(true);
    })
});