import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

old_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256882166.html'
with open(old_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract the objects in const Q = [...]
# Each object is {id: "...", cat: "...", d: ..., q: "...", opts: [...], a: [...], ex: "..."}
# We can evaluate or parse it via regex or node/js
import subprocess

# Let's write a small node script or js to dump Q as json
js_code = """
const fs = require('fs');
const content = fs.readFileSync('""" + old_path.replace('\\', '/') + """', 'utf8');
const match = content.match(/const Q = (\\[[\\s\\S]*?\\]);\\s*let/);
if (match) {
    const qArray = eval(match[1]);
    fs.writeFileSync('data/old_trainer_parsed.json', JSON.stringify(qArray, null, 2), 'utf8');
    console.log('Successfully dumped ' + qArray.length + ' questions from old trainer!');
} else {
    console.log('Failed to match Q array');
}
"""

with open('tools/dump_old_q.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Created tools/dump_old_q.js")
