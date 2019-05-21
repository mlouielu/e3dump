# -*- coding: utf-8 -*-

import colorlog


E3_LOGIN_URL = 'https://e3new.nctu.edu.tw/login/index.php'
E3_MATERIAL_URL = 'https://e3new.nctu.edu.tw/local/courseextension/index.php?courseid={course_id}'


# Logger
handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)
handler.setFormatter(formatter)

logger = colorlog.getLogger('e3dump')
logger.addHandler(handler)
logger.setLevel('INFO')
