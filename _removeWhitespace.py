#!/usr/bin/env python
import re, fnmatch, os

def removeWhitespace(file_path):
    #read file content
    with open(file_path) as f:
        content = f.read()

    #replace whitespace
    openingTag = re.compile('<pre>\s*<code', re.DOTALL)
    closingTag = re.compile('</code>\s*</pre>', re.DOTALL)
    if re.findall(openingTag, content):
        content = re.sub(openingTag, '<pre><code', content)
        content = re.sub(closingTag, '</code></pre>', content)

    #write without whitespace
    with open(file_path,'w') as f:
        f.write(content)

# Get all HTML files
files = []
for root, dirnames, filenames in os.walk('.'):
  for filename in fnmatch.filter(filenames, '*.html'):
      files.append(os.path.join(root, filename))

for filename in files:
    removeWhitespace(filename)
