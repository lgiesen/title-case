# title-case

> Need to write a title? → Use the title case to capitalize it to highlight crucial words

### Background

The purpose of capitalization guidelines is to provide a standard approach to title capitalization within academic writing, helping to ensure that titles are presented in a clear and uniform manner across publications. Following these rules helps to highlight the key elements of a work's title, making it easier for readers to understand and remember.

Title case in APA style is a capitalization style used for the titles of articles, books, chapters, and other works. It involves capitalizing major words in a title or heading. The American Psychological Association (APA) provides specific guidelines for using title case to ensure consistency and clarity across scholarly works. 

### Usage Guidelines (APA Style)
1. Capitalize the First Word of the Title and Subtitle: The first word of the title and any subtitle (after a colon or em dash) should be capitalized, regardless of its part of speech.
2. Capitalize Major Words: Capitalize all major words in the title, including nouns, pronouns, verbs, adjectives, adverbs, and some conjunctions. This includes words of four letters or more.
3. Lowercase Articles, Conjunctions, and Prepositions: Articles (a, an, the), coordinating conjunctions (and, but, for, nor, or, so, yet), and prepositions of three letters or fewer should be lowercase unless they are the first or last word of the title or subtitle.
4. Capitalize Both Words in a Hyphenated Compound: In a hyphenated compound word, capitalize both words, such as "Self-Report" and "Follow-Up".
5. Use Consistent Capitalization in Reference Lists: Ensure that the capitalization of titles in reference lists follows these same rules for consistency and professionalism.
6. Exception for Names and Places: Always capitalize proper nouns, including names and places, regardless of their position in the title.
7. Special Terms and Titles: Capitalize terms that are always capitalized, such as brand names, trademarks, and words that have special meanings or are derived from proper nouns.

### Use Cases and Docs
1. **Capitalize a Single Title**
    1. **Online**: You can use the website [Capitalize my Title](https://capitalizemytitle.com/#APAStyle) to capitalize a single title without any prep work. However, if you need to capitalize text repeatedly, it is more efficient to do it locally. 
    2. **Offline/Local**: 
        - Setup 
            1. Download the [titlecase](https://releases.wezm.net/titlecase/1.1.0/titlecase-1.1.0-x86_64-apple-darwin.tar.gz) file. One [copy]() of it is also in this repository.
            2. Add a shortcut for executing the capitalization (e.g., [iCanHazShortcut](https://github.com/deseven/iCanHazShortcut/releases/download/1.3.0/ichs.dmg) for MacOS) by running the following bash script with a keystroke of your choice. Adjust the path to the titlecase file:

                `pbpaste | /Path/to/titlecase | pbcopy && pbpaste`
        - Usage
            1. Copy the text
            2. Apply your keystroke shortcut
            3. Paste the capitalized text
        - Credits: [Wesley Moore](https://github.com/wezm/titlecase?tab=readme-ov-file)
2. **Capitalize a Bibliography**
    - Setup: Download the [bib-titlecase.py]().
    - Usage: Execute the Python script and pass the BibTeX file as a parameter like this:

        `/Path/to/bib-titlecase.py /Path/to/library.bib`
        
        Then the capitalized output is saved in the new file `/Path/to/library-capitalized.bib`.

### Bibliography

American Psychological Association. (2020). Publication Manual of the American Psychological Association (7th ed.). https://doi.org/10.1037/0000165-000