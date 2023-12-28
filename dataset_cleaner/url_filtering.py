

def url_filtering(text):
    with open('blocklist.txt'"r") as url:
        blocklist = url.readlines()

    if text['meta']['url'] in blocklist:
        text['meta']['blocklist'] = True
    else:
        text['meta']['blocklist'] = False

    return text
