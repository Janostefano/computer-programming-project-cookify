import React from 'react'



function CircularCategory(props) {

    return <a href = {10} className= "circular-category">
        <img className = "circle-img" src={props.photo} alt = {props.categoryName}/>
        <p>{props.categoryName}</p>
    </a>
}


export default CircularCategory