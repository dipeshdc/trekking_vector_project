import { useState } from "react";
import axios from "axios";
import TrekList from "./TrekList";

function App() {
  const [input, setInput] = useState("");
  const [treks, setTreks] = useState([]);
  const [error, setError] = useState(null);
  const hasResults = treks.length > 0 || error;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setTreks([]);
    try {
      const res = await axios.get("http://backend:8000/api/search", {
        params: { query: input },
      });
      setTreks(res.data.result || []);
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
          <TrekList treks={treks} />
        </div>
      )}
    </div>
  );
}

export default App;
