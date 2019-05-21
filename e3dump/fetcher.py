# -*- coding: utf-8 -*-

import asyncio
import pathlib

from lxml import etree

from e3dump.utils import E3_MATERIAL_URL
from e3dump.utils import logger


CHUNK_SIZE = 4 * 1024


def get_course_id(url):
    return url.split('=')[-1]


def get_current_courses_list(root):
    student = list(map(get_course_id, root.xpath(
        'id("layer2_right_current_course_stu")//a[@class="course-link"]/@href')))
    ta = list(map(get_course_id, root.xpath(
        'id("layer2_right_current_course_tea")//a[@class="course-link"]/@href')))

    return student, ta


async def get_course_materials(client, course_id):
    async with client.get(E3_MATERIAL_URL.format(course_id=course_id)) as resp:
        assert resp.status == 200
        text = await resp.text()
        root = etree.HTML(text)

        course_name = root.xpath(
            '//h1[1]/text()')[0].replace('/', '-').replace('\\', '-')
        materials = []
        for row in root.xpath('//tr'):
            if not row.xpath('td'):
                continue
            title = ''.join(row.xpath('td[1]')[0].itertext()).strip(
                '\n ').replace('/', '-').replace('\\', '-')
            material = [(i.text.strip('\n ').replace('/', '-').replace('\\', '-'), i.get('href'))
                        for i in row.xpath('td[2]//a')]
            materials.append((title, material))
        return course_name, materials


async def download_file(client, url, path):
    async with client.get(url) as resp:
        assert resp.status == 200
        with open(path, 'wb') as f:
            while True:
                chunk = await resp.content.read(CHUNK_SIZE)
                if not chunk:
                    break
                f.write(chunk)

        return path.name, url


async def download_materials(client, materials, base_path, course_name):
    futures = []
    base_path = pathlib.Path(base_path)
    for index, value in enumerate(materials):
        folder, material = value
        folder = base_path / course_name / f'{index:02d} - {folder}'
        folder.mkdir(parents=True, exist_ok=True)
        for filename, url in material:
            path = folder / filename
            futures.append(download_file(client, url, path))
    for f in asyncio.as_completed(futures):
        filename, url = await f
        logger.info(f'Download finished: {filename}, {url}')
