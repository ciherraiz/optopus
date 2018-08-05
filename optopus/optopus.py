#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:30:25 2018

@author: ilia
"""
from account import Account, AccountItem


class Optopus():
    """Class implementing automated trading system"""

    def __init__(self, broker) -> None:
        self._broker = broker
        self._account = Account()
        # Events
        self._broker.emit_account_item_event = self._change_account_item
        
    def start(self) -> None:
        self._broker.connect()
        
    def stop(self) -> None:
        self._broker.disconnect()
        
    def pause(self, time: float) -> None:
        self._broker.sleep(time)
        
    def _change_account_item(self, item: AccountItem) -> None:
        if item.tag == 'id':
            self._account.id = item.value







