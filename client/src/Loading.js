import React from "react";
import "./loading.css";

const Loading = (props) => {
  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          minHeight: "100vh",
        }}
      >
        <div className="loader"></div>
      </div>
    </div>
  );
};

export default Loading;
