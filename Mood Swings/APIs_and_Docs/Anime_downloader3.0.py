import yt_dlp
import os
from datetime import datetime
import random

# Define constant paths
DOWNLOAD_DIR = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Mood Swings\Downloads\Anime Downloads"
FFMPEG_PATH = r"C:\Users\Joseph N Nimyel\OneDrive\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/120.0.0.0'
    ]
    return random.choice(user_agents)

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
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        },
        'nocheckcertificate': True,
        'no_warnings': False,
        'quiet': False,
        'verbose': True,
        'extractor_retries': 3,
        'socket_timeout': 30,
        'cookiefile': os.path.join(DOWNLOAD_DIR, 'cookies.txt'),
        'cookiesfrombrowser': ('chrome',),  # Try to use Chrome cookies
    }

    try:
        print(f"\nDownloading to: {DOWNLOAD_DIR}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Extracting video information...")
            info = ydl.extract_info(url, download=False)
            print(f"Preparing to download: {info.get('title', 'Unknown Title')}")
            if info.get('duration'):
                print(f"Duration: {int(info.get('duration', 0)/60)} minutes")
            
            print("\nStarting download...")
            ydl.download([url])
        print("Download completed successfully!")
        log_download(url, "Success")
    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        print(f"\nDownload Error: {error_msg}")
        if "403" in error_msg:
            print("\nTips for 403 Forbidden error:")
            print("1. Make sure you're logged in to the website in your browser")
            print("2. Try copying the direct video URL instead of the page URL")
            print("3. Some websites require premium membership for downloads")
            print("4. Consider using a different source website")
        log_download(url, "Failed", error_msg)
    except Exception as e:
        error_msg = str(e)
        print(f"\nAn unexpected error occurred: {error_msg}")
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

def suggest_alternative_sources():
    print("\nRecommended legal streaming sources:")
    print("1. Crunchyroll")
    print("2. Funimation")
    print("3. HIDIVE")
    print("4. Netflix Anime")
    print("5. Amazon Prime Video")

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
        
        retry = input("\nWould you like to see alternative sources? (y/n): ").lower()
        if retry == 'y':
            suggest_alternative_sources()