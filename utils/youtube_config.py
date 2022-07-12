# API client library
import googleapiclient.discovery

# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "YOUR_API_KEY"
# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY
)
