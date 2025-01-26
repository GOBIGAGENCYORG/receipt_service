#!/usr/bin/env python

import sys
import os

from check_machine.callbacks import message_callback
from queue_manager.queue_manager import QueueManager
from settings import settings

if __name__ == "__main__":
    try:
        QueueManager().start_consume(
            queue=settings.receipts_rabbit_queue, callback=message_callback
        )
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
