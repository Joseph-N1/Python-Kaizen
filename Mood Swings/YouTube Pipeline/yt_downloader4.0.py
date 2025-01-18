import yt_dlp
import os

# Define constant paths
DOWNLOAD_DIR = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Mood Swings\Downloads\Youtube Downloads"
FFMPEG_PATH = r"C:\Users\Joseph N Nimyel\OneDrive\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

def download_yt_video(url):
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
        'noplaylist': True,
        'ffmpeg_location': FFMPEG_PATH,
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'verbose': True,
    }

    try:
        print(f"\nDownloading to: {DOWNLOAD_DIR}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Preparing to download: {info.get('title', 'Unknown Title')}")
            ydl.download([url])
        print("Download completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    print("YouTube Video Downloader")
    print("-----------------------")
    print(f"Downloads will be saved to: {DOWNLOAD_DIR}\n")
    
    while True:
        video_url = input('Enter YouTube video URL (or "exit" to quit): ').strip()
        if video_url.lower() == "exit":
            print("Exiting the program.")
            break
        if not video_url:
            print("Error: No URL entered. Please try again.")
            continue
        if not video_url.startswith(("https://www.youtube.com/", "https://youtu.be/")):
            print("Error: Invalid URL. Please enter a valid YouTube video URL.")
            continue

        download_yt_video(video_url)