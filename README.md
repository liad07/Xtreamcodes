# Xtreamcodes IPTV Project
This project allows you to access and parse an IPTV M3U playlist provided by a server running Xtreamcodes. It also includes a simple HTML/JavaScript video player that allows you to select and play IPTV channels from the playlist.

# Stage 1: Retrieving M3U Playlist URL
To use this project, you first need to enter the URL of your Xtreamcodes server, as well as your port ID, username, and password. This can be done by running the script get_m3u_url.py:

```python
get_m3u_url.py
```
This will prompt you to enter the server URL, port ID, username, and password. Once you have entered these details, the script will generate an M3U playlist URL for you to use.

# Stage 2: Parsing M3U Playlist
Once you have the M3U playlist URL, you can use it to retrieve the list of channels in the playlist. To do this, you need to run the script parse_m3u.py:

``` python parse_m3u.py```
This will prompt you to enter the path to the M3U file you want to parse. Once you have entered this, the script will parse the file and generate individual M3U files for each channel in the playlist. These files will be named after the channel name, with all spaces replaced with underscores.

# Stage 3: Playing IPTV Channels
To play IPTV channels from the playlist, you can use the HTML/JavaScript player included in this project. To use it, open the file index.html in your web browser. This will display a list of channels in a dropdown menu.

To play a channel, simply select it from the dropdown menu. The player will automatically load the corresponding M3U file and start playing the channel.

# Conclusion
This project provides a simple way to access and play IPTV channels from a server running Xtreamcodes. It includes scripts for retrieving and parsing M3U playlists, as well as an HTML/JavaScript player for selecting and playing channels. By following the steps outlined in this README, you can easily set up and use this project to access your IPTV channels.
