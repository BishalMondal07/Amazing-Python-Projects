from pytube import YouTube

link = input("Enter the video link: ")
youtube = YouTube(link)

print(youtube.title)

videos = youtube.streams.filter(only_video=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter the stream number: "))
videos[strm].download()
print('Successfully downloaded.')
