import os
from subprocess import check_output


check_output(
    ["waitress-serve", "--listen", "https://gw.app.8gears.com", os.environ["WSGI_APP"]],
    cwd="/home/app/function",
)
