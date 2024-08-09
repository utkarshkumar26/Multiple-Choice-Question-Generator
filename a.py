import streamlit as st
import spacy
import random
from collections import Counter
from PyPDF2 import PdfReader
import io

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def generate_mcqs(text, num_questions=5):
    if text is None:
        return []

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    num_questions = min(num_questions, len(sentences))
    selected_sentences = random.sample(sentences, num_questions)
    mcqs = []

    for sentence in selected_sentences:
        sent_doc = nlp(sentence)
        nouns = [token.text for token in sent_doc if token.pos_ == "NOUN"]
        if len(nouns) < 2:
            continue
        noun_counts = Counter(nouns)
        if noun_counts:
            subject = noun_counts.most_common(1)[0][0]
            question_stem = sentence.replace(subject, "______")
            answer_choices = [subject]
            distractors = list(set(nouns) - {subject})
            while len(distractors) < 3:
                distractors.append("[Distractor]")
            random.shuffle(distractors)
            for distractor in distractors[:3]:
                answer_choices.append(distractor)
            random.shuffle(answer_choices)
            correct_answer = chr(64 + answer_choices.index(subject) + 1)
            mcqs.append((question_stem, answer_choices, correct_answer))

    return mcqs

def process_pdf(file):
    text = ""
    pdf_reader = PdfReader(file)
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        text += page_text
    return text

st.title("Generate MCQs")
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = process_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")
    
    num_questions = st.slider("Number of Questions", min_value=5, max_value=20, value=5)
    if st.button("Generate MCQs"):
        mcqs = generate_mcqs(text, num_questions=num_questions)
        for i, (question_stem, answer_choices, correct_answer) in enumerate(mcqs, 1):
            st.write(f"**Q{i}:** {question_stem}")
            for idx, choice in enumerate(answer_choices, 1):
                st.write(f"  {chr(64 + idx)}. {choice}")
            st.write(f"  **Answer:** {chr(64 + answer_choices.index(correct_answer) + 1)}")
