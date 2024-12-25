# Written by Lena Weissman
# Program to download three YouTube videos and extract, display, and analyze key metadata from the videos.

from pytubefix import YouTube  # Import pytube
import pandas as pd  # Import pandas

def download_video(url, path):  # Download each video
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading: {url}")  # Indicates video is downloading
    stream.download(output_path=path)
    print(f"Downloaded: {url}")  # Indicates video is downloaded

def extract_metadata(video):
    print(f"Extracting metadata for: {video.title}")  # Print a message indicating which video's metadata is being extracted
    # Create a dictionary containing the video's metadata
    return {
        'title': video.title,
        'description': video.description,
        'author': video.author,
        'upload_date': video.publish_date.strftime('%Y-%m-%d'),
        'views': video.views,
        'length': video.length
    }

# Video URLs
urls = [
    'https://www.youtube.com/watch?v=rfscVS0vtbw',  # Python for Beginners
    'https://www.youtube.com/watch?v=ua-CiDNNj30',  # Data Science Introduction
    'https://www.youtube.com/watch?v=GwIo3gDZCVQ'   # Machine Learning Tutorial
]

path = '/Users/lenaweissman/Desktop/Youtube Downloads'  # My path for where the videos are

# Download the videos and extract metadata
metadata_list = []
for url in urls:
    download_video(url, path)
    yt = YouTube(url)
    metadata = extract_metadata(yt)
    metadata_list.append(metadata)

# Print the metadata for all videos
print("\n--- Video Metadata ---\n")
for metadata in metadata_list:
    print(f"Title: {metadata['title']}")
    print(f"Author: {metadata['author']}")
    print(f"Description: {metadata['description'][:150]}...")  # Truncate description for brevity
    print(f"Upload Date: {metadata['upload_date']}")
    print(f"Views: {metadata['views']}")
    print(f"Length: {metadata['length']} seconds")
    print("-" * 40)

# Create and display a DataFrame with Pandas
df = pd.DataFrame(metadata_list)

# Display video summary with selected columns
print("\n--- Video Summary ---\n")
print(df[['title', 'views', 'length']])

# Pose four questions about the metadata and print the answers
print("\n--- Questions ---\n")

# Question 1: Which video has the most views?
most_views_video = df.loc[df['views'].idxmax()]['title']
print(f"1. Video with the most views: {most_views_video}")

# Question 2: Which video is the longest?
longest_video = df.loc[df['length'].idxmax()]['title']
print(f"2. Longest video: {longest_video}")

# Question 3: Which video is the shortest?
shortest_video = df.loc[df['length'].idxmin()]['title']
print(f"3. Shortest video: {shortest_video}")

# Question 4: Which video was uploaded the earliest?
earliest_video = df.loc[df['upload_date'].idxmin()]['title']
print(f"4. Earliest uploaded video: {earliest_video}")
