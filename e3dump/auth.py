# -*- coding: utf-8 -*-

from lxml import etree

from e3dump.utils import E3_LOGIN_URL


async def login(client, username, password):
    data = {'username': username, 'password': password}
    async with client.post(E3_LOGIN_URL, data=data) as resp:
        assert resp.status == 200
        text = await resp.text()
        root = etree.HTML(text)
        return ':' not in root.xpath('//title/text()')[0], root
