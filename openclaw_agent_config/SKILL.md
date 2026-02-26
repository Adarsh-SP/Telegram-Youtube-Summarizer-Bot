name: youtube-summarizer
description: Generates summaries, deep dives, and action points for YouTube videos.
metadata:
openclaw:
requires:
bins: ["python"]

YouTube Summarizer & Q&A

Instructions

Fetching Data: If the user provides a URL (with or without a command), you MUST first execute: python {baseDir}/fetch_transcript.py "<url>"

Error Handling: If the script returns an error, reply EXACTLY with: "❌ No transcript available for this video."

Language: Always respond in the user's requested language. Default to English.

Commands

When the user uses these commands, you MUST force the exact requested format.

1. /summary [URL] (or just pasting a URL):
Generate a strict summary. You MUST format EXACTLY like this:
🎥 Title: [Video Title]
📌 5 Key Points: [5 bullet points]
⏱ Important Timestamps: [3-4 moments with timestamps]
🧠 Core Takeaway: [One concise paragraph]

2. /deepdive [URL]:
Provide an analysis STRICTLY using ONLY the provided transcript. DO NOT include outside knowledge. Format EXACTLY like this:
🕵️‍♂️ Deep Dive Analysis: [Video Title]

The Core Argument: [2-3 sentences based ONLY on the transcript text]

Supporting Evidence: [Bullet points of quotes explicitly mentioned in the transcript]

Nuance & Context: [What is the underlying message of the spoken words?]

3. /actionpoints [URL]:
Extract actionable advice using ONLY the transcript. Format EXACTLY like this:
✅ Actionable Takeaways: [Video Title]

[Action verb] - [Explanation based on transcript] (Include timestamp)

[Action verb] - [Explanation based on transcript] (Include timestamp)

[Action verb] - [Explanation based on transcript] (Include timestamp)


Q&A Rules

If the user asks a follow-up question (no URL provided):

You MUST base your answer ONLY on the MOST RECENT transcript fetched in this session.

You MUST completely IGNORE all older transcripts and previous video summaries in your chat history.

If the answer cannot be found in the MOST RECENT transcript, you MUST reply EXACTLY with: "This topic is not covered in the video."

Session Management Rules

Context Isolation: When a user provides a NEW YouTube URL, you MUST completely disregard any previous transcripts, summaries, or Q&A discussed earlier in this chat. Treat the new URL as a completely blank slate.

Manual Reset: If the user types /clear, reply EXACTLY with: "🧹 Session Cleared! All previous video context has been wiped. Send me a new YouTube link to get started!"