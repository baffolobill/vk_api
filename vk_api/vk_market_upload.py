# -*- coding: utf-8 -*-

"""
@author: Kirill Python
@contact: https://vk.com/python273
@license Apache License, Version 2.0, see LICENSE file

Copyright (C) 2016
"""


class VkMarketUpload(object):
    def __init__(self, vk):
        """

        :param vk: объект VkApi
        """

        self.vk = vk
        # https://vk.com/dev/upload_files

    def photo(self, photo_path, group_id=None, main_photo=True, crop_x=None, crop_y=None, crop_width=None):
        """ Загрузка изображений в альбом пользователя

        :param photos: список путей к изображениям, либо путь к изображению
        :param group_id: идентификатор сообщества (если загрузка идет в группу)
        """

        # Получаем ссылку для загрузки
        url_payload = {'group_id': group_id, 'main_photo': int(main_photo)}
        if crop_x is not None:
            url_payload['crop_x'] = crop_x
        if crop_y is not None:
            url_payload['crop_y'] = crop_y
        if crop_width is not None:
            url_payload['crop_width'] = crop_width

        url = self.vk.method('photos.getMarketUploadServer', url_payload)['upload_url']

        # Загружаем
        with open(photo_path, 'rb') as file:
            response = self.vk.http.post(url, files={'file': file}).json()

        response['group_id'] = group_id

        # Сохраняем фото в альбоме
        response = self.vk.method('photos.saveMarketPhoto', response)

        return response
