#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse
import logging
import os
import sys

from weixin.wechat.common.textutil import ensure_unicode
from weixin.wechat.parser import WeChatDBParser
from weixin.wechat.render import HTMLRender
from weixin.wechat.res import Resource

logger = logging.getLogger("wechat")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='name of contact')
    parser.add_argument('--output', help='output html file', default='output.html')
    parser.add_argument('--db', default='decrypted.db', help='path to decrypted database')
    parser.add_argument('--avt', default='avatar.index',
                        help='path to avatar.index file that only exists in old version of wechat')
    parser.add_argument('--res', default='resource', help='reseource directory')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()

    name = ensure_unicode(args.name)
    output_file = args.output

    parser = WeChatDBParser(args.db)

    try:
        chatid = parser.get_chat_id(args.name)
    except KeyError:
        sys.stderr.write(u"Valid Contacts: {}\n".format(
            u'\n'.join(parser.all_chat_nicknames)))
        sys.stderr.write(u"Couldn't find the chat {}.".format(name))
        sys.exit(1)

    res = Resource(parser, args.res, args.avt)
    msgs = parser.msgs_by_chat[chatid]
    logger.info(f"Number of Messages for chatid {chatid}: {len(msgs)}")
    assert len(msgs) > 0

    render = HTMLRender(parser, res)
    htmls = render.render_msgs(msgs)

    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    if len(htmls) == 1:
        with open(output_file, 'w', encoding='utf8') as f:
            f.write(htmls[0])
    else:
        assert output_file.endswith(".html")
        basename = output_file[:-5]
        for idx, html in enumerate(htmls):
            with open(basename+f'{idx:02d}.html', 'w') as f:
                f.write(html)
    res.emoji_reader.flush_cache()
