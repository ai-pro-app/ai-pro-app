import { useState } from "react";

function ChatInterface() {
  const [text, setText] = useState("");

  return (
    <div>
      <h2>AI Chat</h2>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Ketik pesan..."
      />

      <button onClick={() => alert(text)}>
        Kirim
      </button>
    </div>
  );
}

export default ChatInterface;
