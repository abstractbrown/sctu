#!c:\users\aaron\projects\sctu_common\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'yolk3k==0.9','console_scripts','yolk'
__requires__ = 'yolk3k==0.9'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('yolk3k==0.9', 'console_scripts', 'yolk')()
    )
