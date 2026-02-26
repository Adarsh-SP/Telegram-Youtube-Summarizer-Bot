# 🎥 Agentic YouTube Summarizer \& Q\&A Telegram Bot

# 

# \[ 📺 CLICK HERE TO WATCH THE 3-5 MINUTE DEMO VIDEO ]

# 

# (Insert your YouTube/Loom link here)

# 

# 📌 Project Objective

# 

# A production-ready Telegram assistant built to revolutionize video research. Unlike traditional bots, this system utilizes an Agentic AI Architecture to autonomously fetch transcripts, generate structured summaries, and provide grounded Q\&A. It is engineered for high token efficiency, zero hallucinations, and multi-lingual support.

# 

# 🏗️ Architecture Explanation

# 

# The project is built on a decoupled, three-tier architecture:

# 

# Orchestration Layer (OpenClaw): Acting as the "Brain," this layer handles the Telegram webhook polling and maintains session state. It routes user intent (like /deepdive or /summary) to the appropriate tools.

# 

# Logic Layer (Python Skill): A custom-built execution engine (fetch\_transcript.py) that handles data extraction. It converts YouTube URLs into searchable text and applies Token Optimization before passing data back to the LLM.

# 

# Intelligence Layer (Minimax 2.5): A high-reasoning LLM that interprets the transcript. Through strict Persona Engineering (SOUL.md), the model is constrained to only provide info from the transcript, preventing general-knowledge hallucinations.

# 

# Key Architectural Win: By using an agentic framework, I eliminated the need for complex, thread-blocking Python dictionaries to manage user sessions. OpenClaw provides native, isolated session memory per user.

# 

# 🚀 Setup Steps

# 

# 1\. Backend Environment

# 

# \# Clone and enter the repo

# cd Eywa-YouTube-Bot

# \# Create virtual environment

# python -m venv venv

# source venv/bin/activate # or venv\\Scripts\\activate on Windows

# \# Install dependencies

# pip install -r requirements.txt

# 

# 

# 2\. OpenClaw Configuration

# 

# Install OpenClaw: pip install openclaw

# 

# Initialize and link your Telegram Bot Token: openclaw onboard

# 

# Copy the contents of the openclaw\_agent/ folder in this repo to your active OpenClaw workspace.

# 

# 3\. Run the Bot

# 

# openclaw gateway start

# 

# 

# ⚖️ Design Trade-offs \& Engineering Decisions

# 

# 1\. Agentic vs. Monolithic (The "Why")

# 

# Decision: I chose an agentic framework (OpenClaw) over a standard python-telegram-bot script.

# 

# Trade-off: While a standard script is easier to write initially, an agentic structure allows for "Tool Calling." If I wanted to add a "Web Search" or "Stock Price" tool later, I could do so without rewriting the core bot logic.

# 

# 2\. Local Caching vs. Fresh Fetching

# 

# Decision: Implemented a local JSON-based caching layer.

# 

# Trade-off: This consumes a small amount of disk space but provides near-instant responses for popular videos and prevents the bot's IP from being rate-limited by YouTube's API.

# 

# 3\. Handling API Breaking Changes

# 

# During development, the youtube-transcript-api library moved toward an object-oriented fetch model. I updated the backend logic to handle the new Transcript objects rather than legacy dictionaries, ensuring the system is resilient to future upstream changes.

# 

# 🌟 Bonus Features Implemented

# 

# Smart Caching: Avoids redundant API calls by storing transcripts locally by Video ID.

# 

# Token Efficiency: Implemented a 15,000-character hard truncation limit to ensure the LLM never exceeds context window limits or wastes API costs.

# 

# Context Isolation: Explicit rules in SOUL.md force the AI to "forget" previous video context when a new URL is provided, preventing cross-video hallucinations.

# 

# Multi-Command Support: Supports /summary, /deepdive, and /actionpoints with strict, distinct formatting for each.

# 

# 📸 Screenshots

# 

# 1\. Multi-Lingual Summary

# 

# \[ INSERT SCREENSHOT OF KANNADA SUMMARY HERE ]

# Description: Demonstrates the bot's ability to maintain strict formatting while translating technical content into regional Indian languages.

# 

# 2\. Grounded Q\&A (No Hallucinations)

# 

# \[ INSERT SCREENSHOT OF THE "HEAVY WINDS" Q\&A HERE ]

# Description: Showcases the bot pulling exact quotes and explaining metaphors based strictly on the transcript context.

# 

# 3\. Strict Persona Rejection

# 

# \[ INSERT SCREENSHOT OF BOT REJECTING "WHO IS OBAMA" HERE ]

# Description: Proves the success of the Persona Engineering (SOUL.md), where the bot refuses to answer general knowledge questions outside its defined scope.

# 

# 🛠️ Tech Stack

# 

# Language: Python 3.10+

# 

# Framework: OpenClaw (Agentic Orchestration)

# 

# LLM: Minimax 2.5

# 

# Libraries: yt-dlp, youtube-transcript-api

# 

# Channel: Telegram API

