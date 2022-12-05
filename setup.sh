mkdir -p ~/.streamlit/
echo "
[server]
headless = true
port = 8000
enableCORS = false

[browser]

# Internet address of the server server that the browser should connect to. Can be IP address or DNS name.
# Default: 'localhost'
serverAddress = '0.0.0.0'

# Whether to send usage statistics to Streamlit.
# Default: true
gatherUsageStats = true

# Port that the browser should use to connect to the server when in liveSave mode.
# Default: whatever value is set in server.port.
serverPort = 8000
" > ~/.streamlit/config.toml
stramlit run app.py
