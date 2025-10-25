#!/usr/bin/env python
import os, sys, subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

cmds = {
    "runserver": "python manage.py runserver",
    "test": "python manage.py test",
    "test-v": "python manage.py test -v 2",
    "migrate": "python manage.py migrate",
}

if len(sys.argv) < 2:
    print("Use: python dev.py [" + "|".join(cmds.keys()) + "]")
    sys.exit(1)

cmd = sys.argv[1]
if cmd in cmds:
    sys.exit(subprocess.run(cmds[cmd], shell=True).returncode)
else:
    print(f"Unknown: {cmd}")
    sys.exit(1)
