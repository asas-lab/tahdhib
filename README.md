# Tahdhib
## files

**wiki_arabic_scripts:** a Python file for scraping web data.

**scraped_data:** a text file of raw scraped data.

**scraped_data_result:** a text file result of running the pipeline on the raw data.

**normalize_arabic:** a Python file of data cleaning pipeline.

## Documentation of the pipeline
- Replace Alif variants (ٱ،إ،أ،آ) with bare Alif (ا)
- Replace Yaa variants (ى) with bare Yaa (ي)
- Replace Ha (ه) with Taa Marbuta (ة)
- Replace (ؤ) with (و)
- Replace (ئ) with (ي)
- Delete (ء)
- Delete (ال)
- Delete Tatweel
- Delete Harakat
- Delete HTML tags
- Delete URLs
- Delete letter repetition (هههههه، مرررحبا)
- Standardize numbers from Western to Arabic
- Remove empty lines
- Remove extra whitespace between words
