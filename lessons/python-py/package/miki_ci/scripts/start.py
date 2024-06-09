
#!/root/.venv/bin/python

import os, sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "..")             )

import build_support as bs


print(bs.Jenkins.jenkins_test())
