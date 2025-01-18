import yt_dlp
import os

def download_yt_video(url):
    # Construct the FFmpeg path correctly
    ffmpeg_base_path = r"C:\Users\Joseph N Nimyel\OneDrive\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"
    ffmpeg_exe = os.path.join(ffmpeg_base_path, "ffmpeg.exe")
    
    # Verify FFmpeg exists
    if not os.path.exists(ffmpeg_exe):
        print(f"Error: FFmpeg not found at {ffmpeg_exe}")
        return

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'ffmpeg_location': ffmpeg_exe,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True,
    }

    try:
        print(f"Using FFmpeg from: {ffmpeg_exe}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    print("YouTube Video Downloader")
    print("-----------------------")
    
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

        # Download video
        download_yt_video(video_url)