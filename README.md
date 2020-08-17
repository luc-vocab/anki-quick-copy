 # Anki Quick Clipboard Copy
 
Allow quickly copying a particular field to the keyboard from within the card browser.
When organizing my Anki flashcards, I frequently need to copy a particular field from my notes to the clipboard, for example to look it up in a dictionary. The normal way of selecting the note, then going to the right field, selecting all and hitting Ctrl+C, is tedious. With this add-on, as soon as you select the note in the Anki browser, the relevant field is automatically copied to the clipboard.

## Installation
Install from https://ankiweb.net/shared/info/1297559139

## Configuration

You do need to configure the addon to tell it which field in your note type needs to be copied to the clipboard. After installing the addon, select it in the Anki addon manager, then click **Config**

in my case, I have a note-type called **Chinese-Words**. In that note type, the field of interest for me is **Chinese**. So my configuration looks like this:

`{
    "Chinese-Words": "Chinese"
}`

You could add multiple note types, like this:

`{
    "Chinese-Words": "Chinese",
    "Italian": "Word",
}`

After configuration, restart Anki, and as soon as you select a note in the card browser, the relevant field will be copied to the clipboard.