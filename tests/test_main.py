import pafy


def main():
    url = 'https://www.youtube.com/watch?v=n5wm3fY5pCY'
    video = pafy.new(url)
    print(video.viewcount)
    best = video.getbest()
    print(best)
    best.download(filepath='C:\\Users\\zhouwei_vendor\\Videos')
    # video.audiostreams[2].download('C:\\Users\\zhouwei_vendor\\Music')


if __name__ == '__main__':
    main()
