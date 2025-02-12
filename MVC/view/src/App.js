import React, { useEffect, useState } from 'react';
import './App.css';  

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
     fetch("http://localhost:5000/")  
      .then(response => response.json())
      .then(data => {
        setMessage(data.message);   
      })
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="App">
      <div className="message-container">
        <h1>{message || "Frontend 'App.js'"}</h1>   
      </div>
    </div>
  );
}

export default App;
