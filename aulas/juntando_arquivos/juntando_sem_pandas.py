import os


filefull = ['ID,A,B\n']

for filetest in sorted(os.listdir()):
    if filetest.endswith('txt') and not filetest == 'file_full.txt':
        with open(filetest) as f:
            lines = f.readlines()
        start = lines.index('TESTE\n')
        filetext = lines[start + 2:]
        filefull.extend(filetext)

with open('file_full.txt', 'w') as w:
    w.write(''.join(filefull))
