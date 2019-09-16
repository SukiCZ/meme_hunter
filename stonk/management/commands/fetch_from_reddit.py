import requests
from django.core.management import BaseCommand

from stonk.models import Meme

URL = 'https://api.reddit.com/r/dankmemes/hot.json'


class Command(BaseCommand):
    help = 'Download hot memes from reddit/dankmemes'

    def handle(self, *args, **options):
        created_count = 0
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json().get("data", {})
            for child in data.get('children', [0, 0])[2:]:  # skip first 2 posts
                if child.get('kind') == 't3':
                    data = child.get('data', {})
                    _, created = Meme.objects.get_or_create(
                        author=data.get('author'),
                        title=data.get('title'),
                        thumbnail=data.get('thumbnail'),
                        url=data.get('url'),
                        defaults={
                            'post_id': data.get('id')
                        }
                    )
                    if created:
                        created_count += 1
            print("Imported %s memes" % created_count)
        else:
            print("Wrong Reddit status %s" % response.status_code)
