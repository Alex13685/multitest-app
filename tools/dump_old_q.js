
const fs = require('fs');
const content = fs.readFileSync('C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256882166.html', 'utf8');
const match = content.match(/const Q = (\[[\s\S]*?\]);\s*let/);
if (match) {
    const qArray = eval(match[1]);
    fs.writeFileSync('data/old_trainer_parsed.json', JSON.stringify(qArray, null, 2), 'utf8');
    console.log('Successfully dumped ' + qArray.length + ' questions from old trainer!');
} else {
    console.log('Failed to match Q array');
}
