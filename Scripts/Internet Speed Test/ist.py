import speedtest

st = speedtest.Speedtest()

download = st.download()

upload = st.upload()

print(f'Download Speed: {download}')
print(f'Upload Speed: {upload}')

st.get_servers([])

ping = st.results.ping

print(f'Ping: {ping}')