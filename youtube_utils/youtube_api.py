from search_videos_api import youtube


def get_search_result(
    part, type, order, q, maxResults, fields, nextToken=None
):
    search_result = (
        youtube.search()
        .list(
            part=part,
            type=type,
            order=order,
            q=q,
            maxResults=maxResults,
            fields=fields,
            pageToken=nextToken,
        )
        .execute()
    )
    return search_result


def get_channel_by_search_result(search_result):

    for item in search_result["items"]:
        # Getting the id
        channelId = item["snippet"]["channelId"]
        # Getting stats of the channel
        channel = (
            youtube.channels()
            .list(
                part="snippet,statistics",
                id=channelId,
                fields="items(snippet(title,customUrl),statistics(subscriberCount))",
            )
            .execute()
        )
    return channel


def get_channel_info(channel):
    channel_info = {
        "title": [],
        "customUrl": [],
        "subscriberCount": [],
    }
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
