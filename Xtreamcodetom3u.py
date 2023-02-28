server_url = input("enter server urlwithout port and user password\n")
port_id = input("enter port id \n")
username = input("enter user \n")
password = input("enter password \n")

m3u_url = f"{server_url}:{port_id}/get.php?username={username}&password={password}&type=m3u&output=mpegts"

print("M3U Playlist URL: ", m3u_url)
