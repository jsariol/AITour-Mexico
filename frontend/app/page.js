"use client";

import { useMemo, useState } from "react";

const DEFAULT_API_BASE = "http://localhost:8000";

export default function Home() {
  const apiBase = useMemo(
    () => process.env.NEXT_PUBLIC_API_BASE || DEFAULT_API_BASE,
    []
  );
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState("");
  const [history, setHistory] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const trimmed = message.trim();
    if (!trimmed) {
      setStatus("Type a message to continue.");
      return;
    }

    setHistory((prev) => [...prev, { role: "user", text: trimmed }]);
    setMessage("");
    setStatus("Sending...");

    try {
      const response = await fetch(`${apiBase}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: trimmed })
      });

      if (!response.ok) {
        const errorBody = await response.json();
        throw new Error(errorBody.detail || "Request failed");
      }

      const data = await response.json();
      setHistory((prev) => [...prev, { role: "assistant", text: data.reply }]);
      setStatus("");
    } catch (error) {
      setStatus(`Error: ${error.message}`);
    }
  };

  return (
    <section className="card">
      <header className="header">
        <p className="eyebrow">Azure OpenAI + FastAPI</p>
        <h1>Conversation Studio</h1>
        <p className="subtitle">
          A clean, professional interface for guided chat experiences.
        </p>
      </header>

      <div className="panel">
        <div className="chat" role="log" aria-live="polite">
          {history.length === 0 ? (
            <div className="empty">Start by sending your first message.</div>
          ) : (
            history.map((item, index) => (
              <div key={index} className={`bubble ${item.role}`}>
                <span className="role">{item.role}</span>
                <p>{item.text}</p>
              </div>
            ))
          )}
        </div>

        <form className="composer" onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              rows={3}
              value={message}
              onChange={(event) => setMessage(event.target.value)}
              placeholder="Ask about itinerary ideas, recommendations, or details..."
            />
          </div>
          <button type="submit">Send</button>
        </form>

        <p className="status" role="status">
          {status}
        </p>
      </div>
    </section>
  );
}
