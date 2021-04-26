# -*- coding: utf8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:42:13
# @Last Modified by:   test
# @Last Modified time: 2021-04-23 22:37:16


from app.lab import blueprint
from flask import jsonify
def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1
    if (n < 0):
       return -1
    elif (n == 0 or n == 1):
       return n
    else:
       for i in range(2, n):
        f0 = f1
        f1 = fn
        fn = f0 + f1
    return fn


@blueprint.route('/', methods=['GET'], strict_slashes=False)
def index():
    return jsonify({
                   'status': True,
                   'message': 'Lab!'
                   })
@blueprint.route('/phamvana', methods=['GET'], strict_slashes=False)
def phamvana():
    sb=""
    for i in range(0, 20):
        sb = sb + str(fibonacci(i)) + ", "
        print(sb)
    return jsonify({
                    'Status': True,
                    'fibonacci': sb
                  })