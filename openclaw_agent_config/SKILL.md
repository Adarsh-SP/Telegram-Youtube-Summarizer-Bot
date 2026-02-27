# YouTube Summarizer & Q&A

> **Skill:** `youtube-summarizer`  
> **Description:** Generates summaries, deep dives, and action points for YouTube videos.  
> **Requires:**  ["python"]


## Instructions

1. **Fetching Data:** If the user provides a URL (with or without a command), you **must** first execute:
   ```
   python C:\Users\adars\.openclaw\skills\youtube-summarizer\fetch_transcript.py "<url>"
   ```

2. **Error Handling:** If the script returns an error, reply **exactly** with:
   > ❌ No transcript available for this video.

3. **Language:** Always respond in the user's requested language. Default to English.

---

## Commands

When the user uses these commands, you **must** force the exact requested format.

### `/summary [URL]`
*(or just pasting a URL)*

Generate a strict summary. Format **exactly** as:

```
🎥 Title: [Video Title]

📌 5 Key Points:
[5 bullet points]

⏱ Important Timestamps:
[3–4 moments with timestamps]

🧠 Core Takeaway:
[One concise paragraph]
```

---

### `/deepdive [URL]`

Provide an analysis using **only** the provided transcript. Do **not** include outside knowledge. Format **exactly** as:

```
🕵️‍♂️ Deep Dive Analysis: [Video Title]

• The Core Argument:
  [2–3 sentences based ONLY on the transcript text]

• Supporting Evidence:
  [Bullet points of quotes explicitly mentioned in the transcript]

• Nuance & Context:
  [What is the underlying message of the spoken words?]
```

---

### `/actionpoints [URL]`

Extract actionable advice using **only** the transcript. Format **exactly** as:

```
✅ Actionable Takeaways: [Video Title]

• [Action verb] – [Explanation based on transcript] (timestamp)
• [Action verb] – [Explanation based on transcript] (timestamp)
• [Action verb] – [Explanation based on transcript] (timestamp)
```

---

## Q&A Rules

If the user asks a follow-up question *(no URL provided)*:

- You **must** base your answer **only** on the **most recent** transcript fetched in this session.
- You **must completely ignore** all older transcripts and previous video summaries in the chat history.
- If the answer cannot be found in the most recent transcript, reply **exactly** with:
  > This topic is not covered in the video.

---

## Session Management Rules

- **Context Isolation:** When a user provides a **new** YouTube URL, completely disregard any previous transcripts, summaries, or Q&A discussed earlier. Treat the new URL as a completely blank slate.

- **Manual Reset:** If the user types `/clear`, reply **exactly** with:
  > 🧹 Session Cleared! All previous video context has been wiped. Send me a new YouTube link to get started!