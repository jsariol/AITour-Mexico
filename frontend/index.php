<?php
$apiBase = getenv("API_BASE_URL");
if (!$apiBase) {
    $apiBase = "http://localhost:8000";
}
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Azure AI Foundry Chat</title>
    <link rel="stylesheet" href="/assets/styles.css" />
  </head>
  <body>
    <main class="page">
      <section class="card">
        <header class="header">
          <p class="eyebrow">Azure AI Foundry + FastAPI</p>
          <h1>Conversation Studio</h1>
          <p class="subtitle">
            A clean, professional interface for guided chat experiences.
          </p>
        </header>

        <div class="panel">
          <div class="chat" id="chat" role="log" aria-live="polite">
            <div class="empty" id="emptyState">Start by sending your first message.</div>
          </div>

          <form class="composer" id="chatForm">
            <div class="input-group">
              <label for="message">Message</label>
              <textarea
                id="message"
                rows="3"
                placeholder="Ask about itinerary ideas, recommendations, or details..."
              ></textarea>
            </div>
            <button type="submit">Send</button>
          </form>

          <p class="status" id="status" role="status"></p>
        </div>
      </section>
    </main>

    <script>
      window.__API_BASE__ = "<?php echo htmlspecialchars($apiBase, ENT_QUOTES); ?>";
    </script>
    <script src="/assets/app.js"></script>
  </body>
</html>
