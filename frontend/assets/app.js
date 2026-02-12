const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("message");
const chat = document.getElementById("chat");
const statusText = document.getElementById("status");
const emptyState = document.getElementById("emptyState");

const apiBase = window.__API_BASE__ || "http://localhost:8000";

const appendMessage = (role, text) => {
  if (emptyState) {
    emptyState.remove();
  }

  const bubble = document.createElement("div");
  bubble.className = `bubble ${role}`;

  const roleTag = document.createElement("span");
  roleTag.className = "role";
  roleTag.textContent = role;

  const body = document.createElement("p");
  body.textContent = text;

  bubble.append(roleTag, body);
  chat.appendChild(bubble);
  chat.scrollTop = chat.scrollHeight;
};

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = messageInput.value.trim();

  if (!message) {
    statusText.textContent = "Type a message to continue.";
    return;
  }

  appendMessage("user", message);
  messageInput.value = "";
  statusText.textContent = "Sending...";

  try {
    const response = await fetch(`${apiBase}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    if (!response.ok) {
      const errorBody = await response.json();
      throw new Error(errorBody.detail || "Request failed");
    }

    const data = await response.json();
    appendMessage("assistant", data.reply);
    statusText.textContent = "";
  } catch (error) {
    statusText.textContent = `Error: ${error.message}`;
  }
});
