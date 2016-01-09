from random import choice

from errbot import BotPlugin, botcmd


class MakiBot(BotPlugin):
    """docstring for MakiBot"""
    @botcmd
    def hello(self, msg, args):
        return choice([
            '何それイミワカンナイ!',
            'ヴェェ!?',
            'お断りします!',
            '从廿_廿从'
        ])
