#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi el3arbi_@email.com
# created       : 26-June-2022
#
# description   : a simple reminder for prompt toolkit
#
# --blue        : #007bff;
# --indigo      : #6610f2;
# --purple      : #6f42c1;
# --pink        : #e83e8c;
# --red         : #dc3545;
# --orange      : #fd7e14;
# --yellow      : #ffc107;
# --green       : #28a745;
# --teal        : #20c997;
# --gray        : #6c757d;
# --gray-dark   : #343a40;
# --primary     : #007bff;
# --secondary   : #6c757d;
# --success     : #28a745;
# --info        : #17a2b8;
# --warning     : #ffc107;
# --danger      : #dc3545;
# --light       : #f6f7f9;
# --dark        : #343a40;
# ----------------------------------------------------------------------------

from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText


def danger_msg(msg):
    print_formatted_text(HTML('<b>[<style fg="#dc3545">error</style>] {}</b>'.format(msg)))


danger_msg('DB with name <style fg="#20c997">{}</style> does not exits.'.format('false.db'))

print_formatted_text(HTML('<b>This is Bold</b>'))
print_formatted_text(HTML('<i>This is Italic</i>'))
print_formatted_text(HTML('<u>This is Underline</u>'))

print()
print_formatted_text(HTML('<ansired>This is red</ansired>'))
print_formatted_text(HTML('<ansigreen>This is green</ansigreen>'))

print()
print_formatted_text(HTML('<skyblue>This is sky blue</skyblue>'))
print_formatted_text(HTML('<seagreen>This is sea green</seagreen>'))
print_formatted_text(HTML('<violet>This is violet</violet>'))

print()
print_formatted_text(HTML('<skyblue>This is sky blue</skyblue>'))

style = Style.from_dict({'aaa': '#17a2b8', 'bbb': '#fd7e14 underline'})
print_formatted_text(HTML('<aaa>Using Stile with</aaa> <bbb>Style.from_dict()</bbb>'), style=style)
print()

text = FormattedText([('#ff0066', 'Hello From'), ('', ' '), ('#44ff00 italic', 'Prompt Toolkit')])
print_formatted_text(text)
print()

from prompt_toolkit import prompt
text = prompt('Give me some input: ')
print(type(text), 'You said: {}'.format(text))
print()

from prompt_toolkit import PromptSession
# advantage: the input history will be kept
p_session = PromptSession()
text1 = p_session.prompt('Input with prompt session: ')
text2 = p_session.prompt('Input with prompt session: ')
print(text1)
print(text2)

# SYNTAX HIGHLIGHTING
from pygments.lexers.html import HtmlLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer

text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer))
print('You said: {}'.format(text))

from pygments.styles import get_style_by_name
from prompt_toolkit.styles.pygments import style_from_pygments_cls
style = style_from_pygments_cls(get_style_by_name('monokai'))
text = prompt('Enter Html: ', lexer=PygmentsLexer(HtmlLexer), style=style, include_default_pygments_style=False)
print('You said: {}'.format(text))

# coloring the prompt itself
style = Style.from_dict({
    # user input (default text)
    '': '#ff0066',

    # prompt
    'username': '#884444',
    'at': '#00aa00',
    'colon': '#0000aa',
    'pound': '#00aa00',
    'host': '#00ffff bg:#444400',
    'path': 'ansicyan underline',
})
message = [('class:username', 'john'), ('class:at', '@'), ('class:host', 'localhost'), ('class:colon', ':'),
           ('class:path', '/user/john'), ('class:pound', '#')]
text = prompt(message, style=style)
print('You said: {}'.format(text))
print()

# AUTOCOMPLETION
from prompt_toolkit.completion import WordCompleter
html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
text = prompt('Enter Html(completer): ', completer=html_completer, complete_while_typing=True)
print('You said: {}'.format(text))
print()

from prompt_toolkit.completion import NestedCompleter
completer = NestedCompleter.from_nested_dict({
    'show': {'version': None, 'clock': None, 'ip': {'interface': {'brief'}}},
    'exit': None,
})
text = prompt('# ', completer=completer)
print('You said: {}'.format(text))
print()

# Cursor shapes
# from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig
# prompt('>', cursor=CursorShape.BLOCK)
# prompt('>', cursor=CursorShape.UNDERLINE)
# prompt('>', cursor=CursorShape.BEAM)
# prompt('>', cursor=CursorShape.BLINKING_BLOCK)
# prompt('>', cursor=CursorShape.BLINKING_UNDERLINE)
# prompt('>', cursor=CursorShape.BLINKING_BEAM)
# prompt('>', cursor=ModalCursorShapeConfig())

# Message Box
from prompt_toolkit.shortcuts import message_dialog
message_dialog(
    title='Example dialog window',
    text='Do you want to continue?\nPress Enter to quit.'
).run()

from prompt_toolkit.shortcuts import radiolist_dialog
result = radiolist_dialog(
    title='RadioList dialog',
    text='Which breakfast would you like?',
    values=[('breakfast1', 'Eggs and beacon'), ('breakfast2', 'French breakfast'), ('breakfast3', 'Equestrian breakfast')]
).run()
print(result)

from prompt_toolkit.shortcuts import checkboxlist_dialog
results_array = checkboxlist_dialog(
    title="CheckboxList dialog",
    text="What would you like in your breakfast ?",
    values=[("eggs", "Eggs"), ("bacon", "Bacon"), ("croissants", "20 Croissants"), ("daily", "The breakfast of the day")]
).run()
print(results_array)

# example with style
results = checkboxlist_dialog(
    title="CheckboxList dialog",
    text="What would you like in your breakfast ?",
    values=[("eggs", "Eggs"), ("bacon", "Bacon"), ("croissants", "20 Croissants"), ("daily", "The breakfast of the day")],
    style=Style.from_dict({
        'dialog': 'bg:#cdbbb3',
        'button': 'bg:#bf99a4',
        'checkbox': '#e8612c',
        'dialog.body': 'bg:#a9cfd0',
        'dialog shadow': 'bg:#c98982',
        'frame.label': '#fcaca3',
        'dialog.body label': '#fd8bb6',
    })
).run()
print(results)

from prompt_toolkit.shortcuts import ProgressBar
import time
with ProgressBar() as pb:
    for i in pb(range(800)):
        time.sleep(.01)
