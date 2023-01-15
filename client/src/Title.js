import React, { useState } from "react";
import { TypeAnimation } from "react-type-animation";

const Title = () => {
  const [search, setSearch] = useState("");
  const [isLoading, setLoading] = useState(false);
  const [gotResult, setResult] = useState(false);

  const handleChange = (e) => {
    setSearch(e.target.value);
  };

  const handleSubmit = (e) => {};

  return (
    <>
      <div className="box">
        <div className="title">
          <h1>Wayfarer</h1>
        </div>
        <div className="example">
          <TypeAnimation
            sequence={[
              "Plan a day trip to Hamilton for under $100", // Types 'One'
              1000, // Waits 1s
              "Plan a day trip to Ottawa for under $200", // Deletes 'One' and types 'Two'
              2000, // Waits 2s
              "Plan a 2 day trip to New York for a group of 4", // Types 'Three' without deleting 'Two'
              () => {
                console.log("Done typing!"); // Place optional callbacks anywhere in the array
              },
            ]}
            wrapper="div"
            cursor={true}
            repeat={Infinity}
            style={{ fontSize: "1em" }}
          />
        </div>
        <div className="searchBox">
          <input
            id="search"
            name="search"
            onChange={handleChange}
            value={search}
          ></input>
        </div>
      </div>
    </>
  );
};

export default Title;
