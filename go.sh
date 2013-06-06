#/bin/sh
grep -r -l "jstoredirect" /home/web/ | python eradicate.py
