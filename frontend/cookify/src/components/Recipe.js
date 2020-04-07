import React, {Component} from 'react'
import {IoIosThumbsUp, IoIosThumbsDown} from 'react-icons/io'
import {FaRegClock} from 'react-icons/fa'

class Recipe extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="col-lg-4 col-md-6 col-sm12">
                <div className="recipe-card">
                    <a href={"/recipes/" + this.props.id}>
                        <img className="recipe-image" src={this.props.photoAddress} alt={this.props.name}/>
                        <p>{this.props.name}</p>
                    </a>
                    <div className="table">
                        <IoIosThumbsUp className = "thumbs"/>
                        <p>{this.props.likes}</p>
                        <FaRegClock/>
                        <p>{Math.floor(this.props.prepareTime / 60) + ":" + (this.props.prepareTime % 60 === 0 ? "00": this.props.prepareTime % 60) }</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default Recipe