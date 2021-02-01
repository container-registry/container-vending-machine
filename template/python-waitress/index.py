import os
from subprocess import check_output


check_output(
    ["waitress-serve", "--listen", "0.0.0.0:5000", os.environ["WSGI_APP"]],
    cwd="/home/app/function",
)
