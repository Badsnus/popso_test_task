import asyncio
import json
import os

from dotenv import load_dotenv
from pyrogram import Client


def load_env(env_file_path: str = '../news_site/.env') -> tuple:
    load_dotenv(env_file_path)

    api_id = int(os.getenv('TELEGRAM_API_ID', 0))
    api_hash = os.getenv('TELEGRAM_API_HASH', 'NO_API_HASH')
    channels_for_parse = list(map(int, os.getenv('CHANNELS_FOR_PARSE', '').split(',')))
    parse_channel_limit = int(os.getenv('TELEGRAM_PARSE_CHANNEL_LIMIT', 10))

    return api_id, api_hash, channels_for_parse, parse_channel_limit


def upload_fixture(fixture_name: str) -> None:
    os.chdir('../news_site')
    os.system('python manage.py makemigrations')
    os.system(f'python manage.py loaddata {fixture_name}')


def dump_data_to_json(data: list[dict], upload, fixture_name='fixture.json') -> None:
    with open(f'../news_site/{fixture_name}', 'w') as file:
        file.write(json.dumps(data))
        if upload:
            upload_fixture(fixture_name)


def get_fixture(channels_pk: dict[str], data: dict[str]) -> list[dict]:
    fixture = []

    for channel, pk in channels_pk.items():
        fixture.append({'model': 'news.channel', 'pk': pk, 'fields': {'name': channel}})

    image_index = post_pk = 1
    for name, data_items in data.items():
        for item in data_items:
            fixture.append({
                'model': 'news.post', 'pk': post_pk,
                'fields': {'text': item['text'], 'channel': channels_pk[name], 'date': str(item['date'])},
            })
            for image in item['images']:
                fixture.append({
                    'model': 'news.image', 'pk': image_index,
                    'fields': {'post': post_pk, 'photo': image},
                })
                image_index += 1
            post_pk += 1
    return fixture


async def main(api_id: int, api_hash: str, channels_for_parse: list[int], parse_channel_limit: int, *,
               upload=True) -> None:
    async with Client('my_account', api_id, api_hash) as app:
        data = {}
        media_groups = {}
        channels_pk = {}

        for pk, channel_id in enumerate(channels_for_parse, 1):
            count = 0
            name = (await app.get_chat(channel_id)).title

            channels_pk[name] = pk
            data[name] = []

            async for message in app.get_chat_history(channel_id):
                media_group_id = message.media_group_id
                if str(message.media) == 'MessageMediaType.PHOTO':
                    file_name = f'/media/{message.photo.file_id}.jpg'

                    if media_group_id not in media_groups:
                        media_groups[media_group_id] = [file_name]
                    else:
                        media_groups[media_group_id].append(file_name)

                    await app.download_media(
                        message.photo.file_id,
                        file_name=f'../news_site' + file_name
                    )

                if message.caption or message.text:

                    data[name].append({
                        'text': message.caption if message.caption else message.text,
                        'date': message.date,
                        'images': media_groups.pop(media_group_id) if media_group_id in media_groups else [],
                    })

                    count += 1
                    print(f'ADD {count} posts for {name}')

                    if count == parse_channel_limit:
                        break

        fixture = get_fixture(channels_pk, data)
        dump_data_to_json(fixture, upload=upload)


if __name__ == '__main__':
    asyncio.run(main(*load_env()))
