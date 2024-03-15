[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-390/) 
[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/learn/get-started)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/mit) 
![GitHub version](https://img.shields.io/github/v/release/lgiesen/title-case?color=green&include_prereleases)
<img align="right" height="72px" src="https://raw.githubusercontent.com/lgiesen/title-case/main/logo.png" />

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

If you only need to capitalize a single title, an online solution is the way to go. You can use [Capitalize my Title](https://capitalizemytitle.com/#APAStyle) to capitalize a single title without any preparation. However, if you need to capitalize text repeatedly, it is more efficient to do it locally. 

## Docs
### 1. Capitalize Text

If you have Apple Darwin x86_64, you can download the precompiled version 2.2.1 [here](https://github.com/lgiesen/title-case/blob/main/titlecase-v221-x86_64-apple-darwin). You can determine your system with the commands `uname -a` (resulting in "Darwin [...] x86_64" here).
If you have another system, you need to compile the project using the following steps. 

Note: 
(1) The commands are for MacOS. (2) I have adjusted the [src/lib.rs](https://github.com/lgiesen/title-case/blob/main/lib.rs) file to account for german words that should not be capitalized. 

**1. Preparation**

```
# Install rust to compile the project coded in rust and confirm with enter
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Set the path for rust/cargo
source "$HOME/.cargo/env"

# You can check the versions with
rustc --version && cargo --version

# Download the project
git clone https://github.com/wezm/titlecase.git
```

**2. Development**

In this example, the repository release version is 
"[2.2.1](https://github.com/wezm/titlecase/releases/tag/v2.2.1)"
and the system is "x86_64-apple-darwin".
Open the zip file (here: "target/titlecase-2.2.1-x86_64-apple-darwin.tar.gz") and move the "titlecase" bash file to the desired location


```
# Give permission to execute the script
chmod +x ../titlecase-build-binary-macos 

# Run the bash script to build and strip the project
../titlecase-build-binary-macos 2.2.1 x86_64-apple-darwin

# Find the .tar.gz file
first_tar_gz=$(find target -maxdepth 1 -name '*.tar.gz' | head -n 1)

# Unzip it into the current directory
tar -xzvf "$first_tar_gz" -C .

# Cleanup: Uninstall rust and confirm with "y"
rustup self uninstall
# Cleanup: Remove the titlecase project and confirm the overrides with "y"
rm -r titlecase
```

Make sure to open the file once, so that your system trusts the file. For MacOs, just use "Open with" > "Terminal"

**3. Application**

Add a shortcut for executing the capitalization with [Shortcuts](https://www.icloud.com/shortcuts/48acb8b78c1f4e46b55d64e29cc6b378). Of course, you need to adjust the path to your titlecase file in the shell script. 
Alternatively, you can use [iCanHazShortcut](https://github.com/deseven/iCanHazShortcut/releases/download/1.3.0/ichs.dmg) for MacOS) by running the following bash script with a keystroke of your choice. Adjust the path to the titlecase file:
```
pbpaste | /Path/to/titlecase | pbcopy && pbpaste
```

### Usage
1. Copy the text
2. Apply your keystroke shortcut
3. Paste the capitalized text

Credits: [Wesley Moore and Rin Arakaki](https://github.com/wezm/titlecase)

### 2. Capitalize a Bibliography
#### Setup

Download the [bib-titlecase.py](https://github.com/lgiesen/title-case/blob/main/bib-titlecase.py). You also need to have [Python 3](https://www.python.org/downloads/) installed.

#### Usage
Execute the Python script and pass the BibTeX filepath as a parameter like this:

```
python3 "/Path/to/bib-titlecase.py" "/Path/to/library.bib"
```

Then the capitalized output is saved in the new file `/Path/to/library-capitalized.bib`. 

Credits: [Garrett Dash Nelson](https://gist.github.com/garrettdashnelson/af0f8307393da37c6f94eda8c4613a4f)

## Bibliography

American Psychological Association. (2020). Publication Manual of the American Psychological Association (7th ed.). https://doi.org/10.1037/0000165-000