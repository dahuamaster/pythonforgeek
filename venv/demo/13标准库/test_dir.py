import os
print(os.path.abspath('.'))
print(os.path.exists('/Users'))
print(os.path.isdir('/Users'))
print(os.path.join('tmp/a/b','c/d/e/f'))

from pathlib import Path
p = Path('.')
print(p.resolve)
p.is_dir()

q=Path('/tmp/a')
Path.mkdir(q,parents=True)