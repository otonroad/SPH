import React from "react";
import axios from "axios";

const App = () => {
  const [showElement, setShowElement] = React.useState(true);
  let active = true;

  const handleClick = () => {
    setShowElement(!showElement);
  };

  const reload = () => {
    if (active) {
      setTimeout(() => {
        window.location.reload();
      }, 5000);
    }
  };

  reload();

  return (
    <div>
      <h1>
        Below is an active search for every word in the spanish dictioanary
        (that i could find)
      </h1>

      <button onClick={handleClick}>Stop</button>
      <br />
      {showElement ? (
        <>
          <img
            src="http://c139-2a00-23c7-1706-d301-c57c-9a19-61ba-2fd5.ngrok.io"
            alt="image"
          />
        </>
      ) : null}
    </div>
  );
};

export default App;
