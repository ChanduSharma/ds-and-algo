import React from "react";
import blaver from "blaver";



const CommentDetail = props => {
    return (
        <div className="comment">
            <a href="/" className="avatar">
                <img alt="avatar" src={props.imgSrc} />
            </a>
            <div className="content">
                <a href="/" className="author">
                    {props.author}
                </a>
                <div className="metadata">
                    <span className="date">Today at {props.timeAgo}</span>
                </div>
                <div className="text">
                    Hello I am going to win
                </div>
            </div>
        </div>
    )
}

export default CommentDetail;