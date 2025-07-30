import { useState } from "react";
import axios from "axios";
import TrekList from "./TrekList";

function App() {
  const [input, setInput] = useState("");
  const [treks, setTreks] = useState(null);
  const [error, setError] = useState(null);
  const hasResults = treks?.payloads?.length > 0 || error;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setTreks(null);
    try {
      const res = await axios.get("http://localhost:8000/api/search", {
        params: { query: input },
      });
      console.log("API Response:", res.data.result);
      setTreks(res.data.result || null);
    } catch (err) {
      setError("Failed to fetch data");
    }
  };

  return (
    <div
      style={{
        padding: "2rem",
        fontFamily: "Arial, sans-serif",
        minHeight: "100vh",
        display: hasResults ? "block" : "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
      }}
    >
      <div style={{ textAlign: "center" }}>
        <h2>Trek Search</h2>
        <form
          onSubmit={handleSubmit}
          style={{
            display: "flex",
            justifyContent: "center",
            marginTop: "1rem",
            gap: "10px",
          }}
        >
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter trek keyword"
            style={{ padding: "10px", width: "300px" }}
          />
          <button type="submit" style={{ padding: "10px 20px" }}>
            Search
          </button>
        </form>
        {error && <p style={{ color: "red", marginTop: "1rem" }}>{error}</p>}
      </div>

      {hasResults && (

        <div style={{ marginTop: "2rem" }}>
          {treks?.llmText && (
            <p style={{ fontStyle: "italic", marginBottom: "1rem" }}>
              {treks?.llmText?.result}
            </p>
          )}
          <TrekList treks={treks?.payloads} />
        </div>
      )}
    </div>
  );
}

export default App;
