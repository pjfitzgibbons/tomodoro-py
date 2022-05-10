import sys
from datetime import datetime

import reactivex as rx



argv = rx.of(*['ehllo', 'woerkl', '!'])


argv.subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed"))

timer = rx.timer(0.0, 1.0)

timer.subscribe(
    on_next=lambda i: print("on_next: {}".format(datetime.now().timestamp())),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)

input("Press Enter key to exit\n")