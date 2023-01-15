import React, { useState } from "react";
import { TypeAnimation } from "react-type-animation";
import "./Title.css";
import axios from "axios";
import { AiOutlineArrowLeft, AiOutlineArrowRight } from "react-icons/ai";
import Loading from "./Loading";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

const Title = () => {
  const [characters, updateCharacters] = useState(finalSpaceCharacters);

  function handleOnDragEnd(result) {
    if (!result.destination) return;

    const items = Array.from(characters);
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);

    updateCharacters(items);
  }

  const test = () => {
    console.log("it worked sheesh");
    setCurrDay(currDay + 1);
  };

  const [search, setSearch] = useState("");
  const [isLoading, setLoading] = useState(false);
  const [gotResult, setResult] = useState(false);
  const [itinerary, setItinerary] = useState([[]]);
  const [destination, setDestination] = useState("");
  const [days, setDays] = useState(0);
  const [currDay, setCurrDay] = useState(0);
  const [currItinerary, setCurrItinerary] = useState([]);
  const url = "http://127.0.0.1:8000/save";

  function sendData() {
    setLoading(true);
    axios
      .post(url, {
        title: "Hello World",
        text: search,
      })
      .then((response) => {
        setLoading(false);
        setResult(true);
        setItinerary(response.data[1]);
        setDestination(response.data[0]);
        setDays(response.data[2] - 1);
        setCurrDay(0);
        setCurrItinerary(itinerary[currDay]);
      });
  }

  const handleChange = (e) => {
    setSearch(e.target.value);
    console.log(search);
  };

  return (
    <>
      {isLoading && <Loading></Loading>}
      {!isLoading && !gotResult && (
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
              className="searchbarname"
              id="search"
              name="search"
              onChange={handleChange}
              value={search}
            ></input>
            <button onClick={sendData}>→</button>
          </div>
        </div>
      )}
      {gotResult && (
        <div className="itinerary">
          <h2>Your trip to {destination}</h2>
          <div className="nav">
            {currDay !== 0 && (
              <AiOutlineArrowLeft onClick={test} className="btn" />
            )}
            <h3>Day {currDay + 1}</h3>
            {currDay < days && (
              <AiOutlineArrowRight onClick={test} className="btn" />
            )}
          </div>
          <DragDropContext onDragEnd={handleOnDragEnd}>
            <Droppable droppableId="characters" direction="horizontal">
              {(provided) => (
                <div
                  className="characters"
                  {...provided.droppableProps}
                  ref={provided.innerRef}
                >
                  {currItinerary.map(
                    ({ name, description, links, images, price }, index) => {
                      return (
                        <Draggable key={name} draggableId={name} index={index}>
                          {(provided) => (
                            <div
                              className="attraction"
                              ref={provided.innerRef}
                              {...provided.draggableProps}
                              {...provided.dragHandleProps}
                            >
                              <h3>{name}</h3>
                              <p>{description}</p>
                              <p>${price}</p>
                            </div>
                          )}
                        </Draggable>
                      );
                    }
                  )}
                  {provided.placeholder}
                </div>
              )}
            </Droppable>
          </DragDropContext>
        </div>
      )}
    </>
  );
};

export default Title;
