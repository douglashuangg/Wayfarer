import React, { useState } from "react";
import { TypeAnimation } from "react-type-animation";
import "./Title.css";
import axios from "axios";

import Loading from "./Loading";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

const finalSpaceCharacters = [
  {
    id: "gary",
    name: "Gary Goodspeed",
    thumb: "/images/gary.png",
  },
  {
    id: "cato",
    name: "Little Cato",
    thumb: "/images/cato.png",
  },
  {
    id: "kvn",
    name: "KVN",
    thumb: "/images/kvn.png",
  },
  {
    id: "mooncake",
    name: "Mooncake",
    thumb: "/images/mooncake.png",
  },
  {
    id: "quinn",
    name: "Quinn Ergon",
    thumb: "/images/quinn.png",
  },
];

const Title = () => {
  const [characters, updateCharacters] = useState(finalSpaceCharacters);

  function handleOnDragEnd(result) {
    if (!result.destination) return;

    const items = Array.from(characters);
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);

    updateCharacters(items);
  }

  const [search, setSearch] = useState("");
  const [isLoading, setLoading] = useState(false);
  const [gotResult, setResult] = useState(false);
  const [itinerary, setItinerary] = useState(
    { id: "1", label: "Steve" },
    { id: "2", label: "Will" },
    { id: "3", label: "Lucas" },
    { id: "4", label: "Mike" },
    { id: "5", label: "Dustin" }
  );

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
        setItinerary(response.data);
        console.log(response);
      });
  }

  const handleChange = (e) => {
    setSearch(e.target.value);
    console.log(search);
  };

  return (
    <>
      {isLoading && <Loading></Loading>}
      {!isLoading && gotResult && (
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
            <button onClick={sendData}>Click me</button>
          </div>
        </div>
      )}
      {!gotResult && (
        <div className="itinerary">
          <DragDropContext onDragEnd={handleOnDragEnd}>
            <Droppable droppableId="characters">
              {(provided) => (
                <ul
                  className="characters"
                  {...provided.droppableProps}
                  ref={provided.innerRef}
                >
                  {characters.map(({ id, name, thumb }, index) => {
                    return (
                      <Draggable key={id} draggableId={id} index={index}>
                        {(provided) => (
                          <li
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                          >
                            <div className="characters-thumb">
                              <img src={thumb} alt={`${name} Thumb`} />
                            </div>
                            <p>{name}</p>
                          </li>
                        )}
                      </Draggable>
                    );
                  })}
                  {provided.placeholder}
                </ul>
              )}
            </Droppable>
          </DragDropContext>
        </div>
      )}
    </>
  );
};

export default Title;
