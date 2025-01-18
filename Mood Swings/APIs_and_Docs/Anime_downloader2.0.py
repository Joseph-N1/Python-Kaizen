import yt_dlp
import os
from datetime import datetime

# Define constant paths
DOWNLOAD_DIR = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Mood Swings\Downloads\Anime Downloads"
FFMPEG_PATH = r"C:\Users\Joseph N Nimyel\OneDrive\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

def download_anime(url):
    # Create downloads directory if it doesn't exist
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        print(f"Created directory: {DOWNLOAD_DIR}")
    
    # Verify FFmpeg exists
    if not os.path.exists(FFMPEG_PATH):
        print(f"Error: FFmpeg not found at {FFMPEG_PATH}")
        return

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'ffmpeg_location': FFMPEG_PATH,
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
        },
        'verbose': True,
    }

    try:
        print(f"\nDownloading to: {DOWNLOAD_DIR}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Preparing to download: {info.get('title', 'Unknown Title')}")
            print(f"Duration: {int(info.get('duration', 0)/60)} minutes")
            ydl.download([url])
        print("Download completed successfully!")
        log_download(url, "Success")
    except Exception as e:
        error_msg = str(e)
        print(f"An error occurred: {error_msg}")
        log_download(url, "Failed", error_msg)

def log_download(url, status, error=None):
    """Log download attempts and their status"""
    log_file = os.path.join(DOWNLOAD_DIR, "download_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | URL: {url} | Status: {status}"
    if error:
        log_entry += f" | Error: {error}"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")

if __name__ == '__main__':
    print("Anime Episode Downloader")
    print("----------------------")
    print(f"Downloads will be saved to: {DOWNLOAD_DIR}")
    print("Note: Please only use this with legal streaming sources\n")
    
    while True:
        url = input('Enter anime episode URL (or "exit" to quit): ').strip()
        
        if url.lower() == "exit":
            print("Exiting the program.")
            break
            
        if not url:
            print("Error: No URL entered. Please try again.")
            continue
            
        if not url.startswith(("http://", "https://")):
            print("Error: Invalid URL. Please enter a valid URL.")
            continue
        
        download_anime(url)