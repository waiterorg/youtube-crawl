import pandas as pd

from .youtube_api import get_channels_by_search_result, get_search_result


def get_channels_info(channels):
    channel_info = {
        "title": [],
        "customUrl": [],
        "subscriberCount": [],
    }
    for channel in channels:
        title = channel["items"][0]["snippet"]["title"]
        get_subscriberCount = channel["items"][0]["statistics"].get(
            "subscriberCount"
        )

        if get_subscriberCount:
            channel_info["subscriberCount"].append(get_subscriberCount)
        else:
            channel_info["subscriberCount"].append("none")

        get_customUrl = channel["items"][0]["snippet"].get("customUrl")

        if get_customUrl:
            channel_info["customUrl"].append(get_customUrl)
        else:
            channel_info["customUrl"].append("none")

        channel_info["title"].append(title)
    return channel_info


def get_channels_info_by_search_as_csv():
    search_query = input("please search :")
    next_page_token = None
    result = []
    for i in range(2):
        search_result = get_search_result(
            q=search_query, nextToken=next_page_token
        )
        channel = get_channels_by_search_result(search_result)
        channels_info = get_channels_info(channel)
        result.append(channels_info)
        next_page_token = search_result["nextPageToken"]

    pd.DataFrame(data=result).to_csv("khazande_result.csv", index=False)
