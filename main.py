import logging

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

import findip

logger = logging.getLogger(__name__)


class IpCopyExtension(Extension):

    def __init__(self):
        super(IpCopyExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        ext_ip = findip.get_external_ip()
        int_ip = findip.get_local_ip()

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Local IP',
                                         description='IP:  %s' % int_ip,
                                         on_enter=CopyToClipboardAction(int_ip)))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='External IP',
                                         description='IP: %s' % ext_ip,
                                         on_enter=CopyToClipboardAction(ext_ip)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    IpCopyExtension().run()
