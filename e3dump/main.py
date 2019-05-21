# -*- coding: utf-8 -*-

import asyncio
import aiohttp

from e3dump.auth import login
from e3dump.fetcher import get_current_courses_list
from e3dump.fetcher import get_course_materials
from e3dump.fetcher import download_materials
from e3dump.utils import logger


async def main(username, password, base_path):
    async with aiohttp.ClientSession() as client:
        success, root = await login(client, username, password)
        if not success:
            logger.critical('Please check your username or password again')
            return

        logger.info('NCTU e3 login successfully')
        student, ta = get_current_courses_list(root)

        for course_id in student + ta:
            course_name, materials = await get_course_materials(client, course_id)
            logger.info(f'Start: {course_name}')
            await download_materials(client, materials, base_path, course_name)

        logger.info('Done!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    root = loop.run_until_complete(main())
