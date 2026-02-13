import sys
import os
import yt_dlp
from pydub import AudioSegment
import imageio_ffmpeg

# 🔥 Force ffmpeg usage from imageio
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
AudioSegment.converter = ffmpeg_path

def download_audios(singer, num_videos):
    os.makedirs("audios", exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audios/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def trim_and_merge(duration, output_file):
    final_audio = AudioSegment.empty()

    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            audio = AudioSegment.from_mp3(os.path.join("audios", file))
            trimmed = audio[:duration * 1000]
            final_audio += trimmed

    final_audio.export(output_file, format="mp3")


def main():
    if len(sys.argv) != 5:
        print("Usage: python <rollnumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit()

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except:
        print("NumberOfVideos and AudioDuration must be integers")
        sys.exit()

    output_file = sys.argv[4]

    if num_videos <= 0:
        print("Number of videos must be positive")
        sys.exit()

    if duration <= 20:
        print("Audio duration must be greater than 20 seconds")
        sys.exit()

    try:
        print("Downloading audios...")
        download_audios(singer, num_videos)

        print("Trimming and merging...")
        trim_and_merge(duration, output_file)

        print("Mashup created successfully:", output_file)

    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    main()
