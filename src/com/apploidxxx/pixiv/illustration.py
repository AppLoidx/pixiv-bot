class Illustration:
    _artist = None
    _image_url = None
    _artist_url = None
    _title = None

    def __init__(self, title, artist, image_url, artist_url):
        self._title = title
        self._artist = artist
        self._image_url = image_url
        self._artist_url = artist_url

    def get_artist(self):
        return self._artist

    def get_image_url(self):
        return self._image_url

    def get_artist_url(self):
        return self._artist_url

    def get_title(self):
        return self._title
