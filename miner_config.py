# -*- coding: utf-8 -*-

"""Этот файл нужно изменять до того, как вы запустите майнер. Для лучшего понимания смотрите в
wallet.py.
"""

# Тут указываем сгенерированный адрес. Все монеты пойдут сюда.
MINER_ADDRESS = "03277499e99e4db944d4b02b5694e9993cc565b435a28c725822fa792d4aeb2693"

# Тут укажите URL-адрес ноды или ее ip. Если все запущено на localhost, то пишем так:
MINER_NODE_URL = "http://localhost:5000"

# А здесь храним URL-адреса каждого узла в сети, чтобы можно было общаться с ними.
PEER_NODES = []