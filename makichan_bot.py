from random import choice

from errbot import BotPlugin, botcmd


class MakiBot(BotPlugin):
    """docstring for MakiBot"""
    @botcmd
    def hello(self, msg, args):
        return choice([
            'nanisore, imiwakannai.',
            'mendonahito.',
            'okotowarishimasu.',
            'vuee.'
        ])
