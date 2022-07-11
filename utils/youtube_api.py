from .youtube_config import youtube


def get_search_result(
    q,
    part="snippet",
    type="video",
    order="relevance",
    maxResults=50,
    fields="nextPageToken,items(snippet(channelId))",
    nextToken=None,
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


def get_channels_by_search_result(search_result):
    channels = []
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
        channels.append(channel)
    return channels
