import React from "react";
import ReactDOM from "react-dom/client";
// import ReactDOM1 from "react-dom";
import blaver from "blaver";
import CommentDetail from "./CommentDetail";
import ApprovalCard from "./ApprovalCard";

const root = ReactDOM.createRoot(document.getElementById("root"));

const App = () => {

    return (
        <div className="ui container comments">
            <ApprovalCard>
                <CommentDetail
                    author="chandra"
                    timeAgo="3:39PM"
                    imgSrc={blaver.image.avatar()}
                />
            </ApprovalCard>
            <ApprovalCard>
                <CommentDetail
                    author="Sam"
                    timeAgo="4:39PM"
                    imgSrc={blaver.image.avatar()}
                />
            </ApprovalCard>
            <ApprovalCard>
                <CommentDetail
                    author="Reks"
                    timeAgo="5:39PM"
                    imgSrc={blaver.image.avatar()}
                />
            </ApprovalCard>

        </div>
    );
};

root.render(<App />);

