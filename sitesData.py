
class SiteData:
    def __init__(self, name, bytes, duration):
        self.site_name = name
        self.site_downloaded_bytes = bytes
        self.site_downloaded_duration = duration

    def get_bandwith(self):
        return self.site_downloaded_bytes / self.site_downloaded_duration

    def add_bytes_to_site(self,bytes_to_add):
        self.site_downloaded_bytes = self.site_downloaded_bytes + bytes_to_add
