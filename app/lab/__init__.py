# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-26 08:42:13
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-26 21:02:43


from flask import Blueprint


blueprint = Blueprint(
    'lab_blueprint',
    __name__,
    url_prefix='/lab'
)
