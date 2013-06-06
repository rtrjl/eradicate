#/bin/sh
grep -r -l "jstoredirect" site-verole/ | python eradicate.py
