# The data will be stored using pandas
from genericpath import exists
import pandas as pd
# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyA4MXaU7iQwrjj7PYrvXw-UZJNAlGD-nlU'
# API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

search_query = input('please search :')

# search result query
search_result_channel_ids = youtube.search().list(
    part="snippet",
    type='video',
    order="relevance",
    q=search_query,
    maxResults=50,
    fields="nextPageToken,items(snippet(channelId))"
).execute()

nextToken = search_result_channel_ids['nextPageToken']

# second page search result query
second_search_result_channel_ids = youtube.search().list(
        part="snippet",
        type='video',
        order="relevance",
        q=search_query,
        maxResults=50,
        fields="items(snippet(channelId))",
        pageToken=nextToken
).execute()
# Dictionary to store chanel data
channel_info = {
    'title':[],
    'customUrl':[],
    'subscriberCount':[],
}
# For loop to obtain the information of each channel info
for item in search_result_channel_ids['items']:
    # Getting the id
    channelId = item['snippet']['channelId']
    # Getting stats of the channel
    r = youtube.channels().list(
        part="snippet,statistics",
        id=channelId,
        fields="items(snippet(title,customUrl),statistics(subscriberCount))"
    ).execute()
    title = r['items'][0]['snippet']['title']
    get_subscriberCount = r['items'][0]['statistics'].get('subscriberCount')
    
    if get_subscriberCount:
        channel_info['subscriberCount'].append(get_subscriberCount)
    else:
        channel_info['subscriberCount'].append('none')
    
    get_customUrl = r['items'][0]['snippet'].get('customUrl')
    
    if get_customUrl:
        channel_info['customUrl'].append(get_customUrl)
    else:
        channel_info['customUrl'].append('none')
    
    channel_info['title'].append(title)

# For loop to obtain the information for next page result
for item in second_search_result_channel_ids['items']:
    # Getting the id
    channelId = item['snippet']['channelId']
    # Getting stats of the channel
    r = youtube.channels().list(
        part="snippet,statistics",
        id=channelId,
        fields="items(snippet(title,customUrl),statistics(subscriberCount))"
    ).execute()
    title = r['items'][0]['snippet']['title']
    get_subscriberCount = r['items'][0]['statistics'].get('subscriberCount')
    
    if get_subscriberCount:
        channel_info['subscriberCount'].append(get_subscriberCount)
    else:
        channel_info['subscriberCount'].append('none')
    
    get_customUrl = r['items'][0]['snippet'].get('customUrl')
    
    if get_customUrl:
        channel_info['customUrl'].append(get_customUrl)
    else:
        channel_info['customUrl'].append('none')
    
    channel_info['title'].append(title)

pd.DataFrame(data=channel_info).to_csv("khazande_result.csv", index=False)
