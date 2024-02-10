import sqlite3

def create_m3u8_playlist(urls, output_file):
    with open(output_file, 'w') as f:
        f.write("#EXTM3U\n")
        for url in urls:
            f.write("#EXTINF:-1, {}\n".format(url))  # Assume each URL is a separate stream, hence -1 duration
            f.write("{}\n".format(url))

def main():
    # Connect to SQLite database
    conn = sqlite3.connect('stream_channels.db')
    c = conn.cursor()

    # Fetch URLs from the database
    c.execute("SELECT url FROM filtered_urls")
    urls = c.fetchall()

    # Close connection to the database
    conn.close()

    # Extract URLs from fetched data
    urls = [url[0] for url in urls]

    # Create m3u8 playlist
    create_m3u8_playlist(urls, 'playlist.m3u8')

if __name__ == "__main__":
    main()

