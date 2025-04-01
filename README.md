# Question-MCQS-Generator-Using-Machine-learning-NLP

# Introduction:

Our project aims to generate multiple-choice questions (MCQs) using machine learning and natural language processing (NLP) techniques. MCQs are widely used in educational assessments to evaluate students' understanding of a given topic. By automating the generation of MCQs, educators can save time and effort while ensuring the quality and relevance of the questions.



# Explanation of the Code:

# Loading Modules:

The code begins by importing necessary modules, including spacy for NLP processing and random for random selection of sentences.

# Loading English Language Model:

It loads the English language model from spaCy (en_core_web_sm) for tokenization, tagging, parsing, named entity recognition (NER), and word vectors.


# Input Text:

The input text contains information about the Nile River, its significance, and characteristics.

# Processing the Text:

The input text is processed using spaCy, which tokenizes the text into words, identifies parts of speech, parses the structure, recognizes named entities, and generates word vectors.

# Extracting Sentences:

The processed text is split into sentences, and each sentence is stored in a list named sentences.
Randomly Selecting Sentences:
Randomly selects a subset of sentences from the list of sentences to form questions. The number of questions to generate is specified by num_questions.


#  Result:
The selected sentences are stored in the selected_sentences list, which will be used to generate MCQs.
















This code can to be a useful tool for automatically generating multiple-choice questions from text data, which could be helpful for educational purposes or generating practice quizzes. You can discuss how this functionality can save time for educators or content creators and how it leverages natural language processing techniques to automate the process. Additionally, you can mention potential improvements or customization options, such as adjusting the number of distractors or incorporating more sophisticated language processing techniques.


