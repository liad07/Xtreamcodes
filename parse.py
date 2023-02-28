m3u_file = input("enter path of m3u file to parse\n")

with open(m3u_file) as f:
    lines = f.readlines()

channels = []
name = ''
for line in lines:
    line = line.strip()
    if line.startswith('#EXTINF:'):
        name = line.split(',')[1]
    elif line.startswith('http'):
        url = line
        channels.append((name, url))

for name, url in channels:
    file_name = name.lower().replace(' ', '_') + '.m3u'
    with open(file_name, 'w') as f:
        f.write('#EXTM3U\n')
        f.write(f'#EXTINF:-1,{name}\n')
        f.write(f'{url}\n')
