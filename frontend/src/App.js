import React, { useState } from "react";
import axios from "axios";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";
import "./App.css";

function App() {
  const [code1, setCode1] = useState("");
  const [code2, setCode2] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCompare = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:5000/compare", { code1, code2 });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error comparing code");
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>IntelliCode: Code Similarity Detector ⚡</h1>

      <div className="code-inputs">
        <textarea
          placeholder="Paste first code here..."
          value={code1}
          onChange={(e) => setCode1(e.target.value)}
        />
        <textarea
          placeholder="Paste second code here..."
          value={code2}
          onChange={(e) => setCode2(e.target.value)}
        />
      </div>

      <button onClick={handleCompare} disabled={loading}>
        {loading ? "Comparing..." : "Compare Code"}
      </button>

      {result && (
        <div className="result-box">
          <h2>Similarity Score: {result.similarity}%</h2>
          <div className="highlighted">
            <div>
              <h3>Code 1</h3>
              <SyntaxHighlighter language="python" style={vscDarkPlus}>
                {code1}
              </SyntaxHighlighter>
            </div>
            <div>
              <h3>Code 2</h3>
              <SyntaxHighlighter language="python" style={vscDarkPlus}>
                {code2}
              </SyntaxHighlighter>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
