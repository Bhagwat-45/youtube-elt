def _batch_list(video_id_list: list, batch_size: int):
    for video_id in range(0, len(video_id_list), batch_size):
        yield video_id_list[video_id: video_id + batch_size]