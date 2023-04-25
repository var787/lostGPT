import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  // Set up state to manage messages and user input
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  // Function to send a message to the chatbot and receive a response
  const sendMessage = async (event) => {
    event.preventDefault();

    // Add the user's message to the list of messages
    setMessages([...messages, { type: "user", content: input }]);
    // Clear the input field
    setInput("");

    // Send a request to the backend API to get the chatbot's response
    try {
      const response = await axios.post("http://localhost:8000/api/chat", {
        prompt: input,
      });
      // Add the chatbot's response to the list of messages
      setMessages((prevState) => [
        ...prevState,
        { type: "bot", content: response.data.response },
      ]);
    } catch (error) {
      console.error("Error fetching chat response:", error);
    }
  };

  return (
    <div className="App">
      <h1>LostGPT</h1>
      {/* Display the chat messages */}
      <div className="chat-container">
        {messages.map((message, index) => (
          <div key={index} className={`chat-message ${message.type}`}>
            {message.content}
          </div>
        ))}
      </div>
      {/* Form for user input */}
      <form onSubmit={sendMessage}>
        <input
          type="text"
          value={input}
          onChange={(event) => setInput(event.target.value)}
          placeholder="Type your message here..."
          required
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
