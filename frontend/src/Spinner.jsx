// Spinner.js
const Spinner = () => (
  <div style={styles.container}>
    <div style={styles.spinner}></div>
    <p style={styles.text}>Thinking... Finding the best treks for you.</p>
  </div>
);

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    marginTop: "20px",
  },
  spinner: {
    width: "40px",
    height: "40px",
    border: "4px solid #ccc",
    borderTop: "4px solid #4CAF50",
    borderRadius: "50%",
    animation: "spin 1s linear infinite"
  },
  text: {
    marginTop: "10px",
    color: "#FFF",
  },
};

export default Spinner;
