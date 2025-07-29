export default function TrekList({ treks }) {
  if (!treks || treks.length === 0) {
    return <p style={{ textAlign: "center" }}>No results found.</p>;
  }

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
        gap: "1.5rem",
        justifyItems: "center",
        maxWidth: "1200px",
        margin: "0 auto",
      }}
    >
      {treks.map((trek, idx) => (
        <div
          key={idx}
          style={{
            border: "1px solid #ccc",
            borderRadius: "8px",
            padding: "1rem",
            width: "100%",
            marginLeft:"2rem",
            maxWidth: "350px",
            boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
          }}
        >
          <h3>{trek.Trek}</h3>
          <p><strong>Cost:</strong> {trek.Cost.trim()}</p>
          <p><strong>Duration:</strong> {trek.Time.trim()}</p>
          <p><strong>Trip Grade:</strong> {trek["Trip Grade"]}</p>
          <p><strong>Max Altitude:</strong> {trek["Max Altitude"]}</p>
          <p><strong>Accommodation:</strong> {trek.Accomodation}</p>
          <p><strong>Best Travel Time:</strong> {trek["Best Travel Time"]}</p>
          <p>
            <strong>Contact / Book:</strong>{" "}
            <a
              href={trek["Contact or Book your Trip"]}
              target="_blank"
              rel="noopener noreferrer"
            >
              Link
            </a>
          </p>
        </div>
      ))}
    </div>
  );
}
