def added_avatar(avatar):
    with open(avatar, "rb") as f:
        bin_file = f.read()
        return bin_file
