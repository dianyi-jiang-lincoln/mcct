###############################
### MCCT                    ###
###############################


def get_news():
    return (
        f"SELECT "
        f"is_sticky, "
        f"thumbnail_url, "
        f"title, "
        f"type, "
        f"preview, "
        f"content, "
        f"address, "
        f"phone_number, "
        f"updated_at "
        f"FROM `posts` "
        f"WHERE visible_start < NOW() AND type = 'news'"
        f"LIMIT 50 "
    )


def get_events():
    return (
        f"SELECT "
        f"is_sticky, "
        f"thumbnail_url, "
        f"title, "
        f"type, "
        f"preview, "
        f"content, "
        f"address, "
        f"phone_number, "
        f"updated_at "
        f"FROM `posts` "
        f"WHERE visible_start < NOW() AND type = 'event'"
        f"LIMIT 50 "
    )
