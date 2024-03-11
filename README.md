# Title Case

> Need to write a title? → Use the title case to capitalize it to highlight crucial words

## Background

The purpose of capitalization guidelines is to provide a standard approach to title capitalization within academic writing, helping to ensure that titles are presented in a clear and uniform manner across publications. Following these rules helps to highlight the key elements of a work's title, making it easier for readers to understand and remember.

Title case in APA style is a capitalization style used for the titles of articles, books, chapters, and other works. It involves capitalizing major words in a title or heading. The American Psychological Association (APA) provides specific guidelines for using title case to ensure consistency and clarity across scholarly works. 

## Usage Guidelines (APA Style)
1. Capitalize the First Word of the Title and Subtitle: The first word of the title and any subtitle (after a colon or em dash) should be capitalized, regardless of its part of speech.
2. Capitalize Major Words: Capitalize all major words in the title, including nouns, pronouns, verbs, adjectives, adverbs, and some conjunctions. This includes words of four letters or more.
3. Lowercase Articles, Conjunctions, and Prepositions: Articles (a, an, the), coordinating conjunctions (and, but, for, nor, or, so, yet), and prepositions of three letters or fewer should be lowercase unless they are the first or last word of the title or subtitle.
4. Capitalize Both Words in a Hyphenated Compound: In a hyphenated compound word, capitalize both words, such as "Self-Report" and "Follow-Up".
5. Use Consistent Capitalization in Reference Lists: Ensure that the capitalization of titles in reference lists follows these same rules for consistency and professionalism.
6. Exception for Names and Places: Always capitalize proper nouns, including names and places, regardless of their position in the title.
7. Special Terms and Titles: Capitalize terms that are always capitalized, such as brand names, trademarks, and words that have special meanings or are derived from proper nouns.

## Use Cases and Docs
### **Capitalize a Single Title**
#### **Online**
    
You can use the website [Capitalize my Title](https://capitalizemytitle.com/#APAStyle) to capitalize a single title without any prep work. However, if you need to capitalize text repeatedly, it is more efficient to do it locally. 

#### **Offline/Local**
##### Setup 
1. If you have Apple Darwin x86_64, you can download the precompiled version 2.2.1 [here](https://github.com/lgiesen/title-case/blob/main/titlecase-v221-x86_64-apple-darwin). You can determine your system with the commands
    `uname -a` (resulting in "Darwin [...] x86_64" here).
    <!-- Alternatively, you can download it from the original repository for [version 1.1.0 for Apple Darwin](https://releases.wezm.net/titlecase/1.1.0/titlecase-1.1.0-x86_64-apple-darwin.tar.gz) file.  -->
    If you have another system, you need to compile the project using the following steps. Note: The commands are for MacOS

    1. Install rust to compile the project coded in rust: 

        `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
    
    2. Set the path for rust/cargo: 
        
        `source "$HOME/.cargo/env"`
        
        You can check the versions with `rustc --version && cargo --version`

    3. Download the project: 
        
        `git clone https://github.com/wezm/titlecase.git && cd titlecase`

    4. Run the bash script to build and strip the project: 
        
        `chmod +x ../titlecase-build-binary-macos && ../titlecase-build-binary-macos 2.2.1 x86_64-apple-darwin` 
        
        In this example, the repository release version is 
        "[2.2.1](https://github.com/wezm/titlecase/releases/tag/v2.2.1)"
        and the system is "x86_64-apple-darwin".

    5. Open the zip file (here: "target/titlecase-2.2.1-x86_64-apple-darwin.tar.gz")

    6. Move the "titlecase" bash file to the desired location

    7. Remove the titlecase project `cd .. && rm -r titlecase` and confirm the overrides with `y`

    8. Uninstall rust with `rustup self uninstall` and confirm with `y`



2. Add a shortcut for executing the capitalization (e.g., [iCanHazShortcut](https://github.com/deseven/iCanHazShortcut/releases/download/1.3.0/ichs.dmg) for MacOS) by running the following bash script with a keystroke of your choice. Adjust the path to the titlecase file:

    `pbpaste | /Path/to/titlecase | pbcopy && pbpaste`
##### Usage
1. Copy the text
2. Apply your keystroke shortcut
3. Paste the capitalized text

##### Credits: [Wesley Moore and Rin Arakaki](https://github.com/wezm/titlecase)

### **Capitalize a Bibliography**
#### Setup

Download the [bib-titlecase.py](https://github.com/lgiesen/title-case/blob/main/bib-titlecase.py). You also need to have [Python 3](https://www.python.org/downloads/) installed.

#### Usage
Execute the Python script and pass the BibTeX file as a parameter like this:

`python3 "/Path/to/bib-titlecase.py" "/Path/to/library.bib"`

Then the capitalized output is saved in the new file `/Path/to/library-capitalized.bib`. 

##### Credits: [Garrett Dash Nelson](https://gist.github.com/garrettdashnelson/af0f8307393da37c6f94eda8c4613a4f)

## Bibliography

American Psychological Association. (2020). Publication Manual of the American Psychological Association (7th ed.). https://doi.org/10.1037/0000165-000