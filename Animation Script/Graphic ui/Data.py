#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Data:
    """
    It provides collecting and performing all data, which comes from Serial port
    """

    def __init__(self):
        self.data_store = None

        self.x_data = []
        self.y_data = []
        self.t_data = []

        # data = x_data, y_data
