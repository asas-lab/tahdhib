# Tahdhib
## files

**wiki_arabic_scripts:** a python file for scrabing web data.

**scraped_data:** a text file of raw scrippd data.

**scraped_data_result:** a text file result of running the pipeline on the raw data.

**normalize_arabic:** a python file of data cleaning pipeline.

## Documentation of the pipeline
Replace Alif variants (ٱ،إ،أ،آ) with bare Alif (ا)
Replace Yaa variants (ى) with bare Yaa (ي)
Replace Ha (ه) with Taa Marbuta (ة)
Replace (ؤ) with (و)
Replace (ئ) with (ي)
Delete (ء)
Delete (ال)
Delete Tatweel
Delete Harakat
Delete HTML tags
Delete URLs
Delete letters repetition (هههههه، مرررحبا)
Standrize numbers from western to Arabic
Remove empty lines
Remove extra whitespace between words

### Reasons
1 - Reduce the complexity of the text because the model has fewer variations of the same word to learn.
2 - To help the model to generalize better, as it may not need to understand the nuances of each character variant to make accurate predictions.
3 - Mostly it carries grammatical or phonetic significance but not semantic. 
4 - Fix spelling mistakes since most of dectation errors are in these areas, especially social media data.  

**Problem:** an issue will rise using this deep normalization, a model trained on it might not correctly generate text with the appropriate use of variations.

**Solution:** do multiple model training phases, initially training a model on highly normalized data and then introducing less normalized or unnormalized data in a later phase. 

## Methodology: 
### Phase one:
Training on highly normalized data initially can help the model focus on learning the core patterns and relationships in the data without the complexity introduced by variations in spelling, grammar, and formatting.

The goal here is to reach a satisfactory level of accuracy where the model has a solid understanding of the fundamental aspects of the language or task.

### Phase two:
Start introducing less normalized data gradually. This could be done in batches or phases to avoid overwhelming the model with too much complexity at once.

Use this less normalized data to fine-tune the model. The idea is that the model will learn to handle the variability and complexity in the language that was initially abstracted out.

Monitor for overfitting as the model might start to learn the noise instead of the signal. Regular validation of a diverse set of data is crucial.

## Conclusion
By doing this practice I am hoping that the model may become more robust and flexible, able to handle a wider range of inputs. However, we should be careful that the model might get confused by the introduction of new patterns, so regular evaluation and adjustments are necessary.