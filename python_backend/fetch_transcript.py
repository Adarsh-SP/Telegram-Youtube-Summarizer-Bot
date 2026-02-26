import sys
import re
import os
import json
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp

# Define where caches will be stored
CACHE_DIR = "transcript_cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def extract_video_id(url: str):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_video_info(url: str):
    ydl_opts = {'quiet': True, 'skip_download': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('title', 'Unknown Title')
    except Exception:
        return "Unknown Title"

def get_transcript(video_id: str):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id, languages=['en', 'en-IN'])
        formatted = []
        for item in transcript_list:
            minutes = int(item.start // 60)
            seconds = int(item.start % 60)
            formatted.append(f"[{minutes:02d}:{seconds:02d}] {item.text}")
        return "\n".join(formatted)
    except Exception:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No URL provided.")
        sys.exit(1)
        
    url = sys.argv[1]
    vid_id = extract_video_id(url)
    
    if not vid_id:
        print("Error: Invalid YouTube URL.")
        sys.exit(1)

    # --- SMART CACHING LOGIC ---
    cache_file_path = os.path.join(CACHE_DIR, f"{vid_id}.json")
    
    # Check if we already have this video saved
    if os.path.exists(cache_file_path):
        # Print to stderr so it shows in your terminal but OpenClaw ignores it
        sys.stderr.write(f"\n🟢 CACHE HIT: Loading {vid_id} from local storage...\n")
        
        with open(cache_file_path, "r", encoding="utf-8") as f:
            cached_data = json.load(f)
            title = cached_data.get("title")
            transcript = cached_data.get("transcript")
            
    else:
        sys.stderr.write(f"\n🟡 CACHE MISS: Fetching {vid_id} from YouTube...\n")
        
        title = get_video_info(url)
        transcript = get_transcript(vid_id)
        
        # Save to cache if fetch was successful
        if transcript:
            with open(cache_file_path, "w", encoding="utf-8") as f:
                json.dump({"title": title, "transcript": transcript}, f)
                sys.stderr.write(f"💾 Saved {vid_id} to cache.\n")

   # --- OUTPUT TO OPENCLAW ---
    if transcript:
        # Limit to roughly ~15,000 characters (approx. 3000-4000 tokens) for token optimization
        MAX_CHARS = 15000 
        
        if len(transcript) > MAX_CHARS:
            optimized_transcript = transcript[:MAX_CHARS] + "\n\n...[TRANSCRIPT TRUNCATED FOR TOKEN EFFICIENCY]..."
            sys.stderr.write("✂️ Transcript truncated to save token costs.\n")
        else:
            optimized_transcript = transcript

        print(f"TITLE: {title}\n")
        print(f"TRANSCRIPT:\n{optimized_transcript}")
    else:
        print("Error: No transcript available.")