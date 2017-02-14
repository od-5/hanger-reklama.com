# coding=utf-8
from os import path as op
import uuid

__author__ = 'aser'


def upload_to(instance, filename, prefix=None):
        """
        Auto generate name for File and Image fields.
        :param instance: Instance of Model
        :param filename: Name of uploaded file
        :param prefix: Add to path
        :return:
        """
        name, ext = op.splitext(filename)
        filename = "%s%s" % (uuid.uuid4(), ext or '.jpg')
        basedir = op.join(instance._meta.app_label, instance._meta.model_name)
        if prefix:
            basedir = op.join(basedir, prefix)
        return op.join(basedir, filename[:2], filename[2:4], filename)
