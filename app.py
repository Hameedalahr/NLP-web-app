from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.corpus import stopwords, wordnet, names
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('names')

app = Flask(__name__)
CORS(app)

@app.route('/remove_stopwords', methods=['POST'])
def remove_stopwords():
    data = request.json
    text = data.get("text", "")
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_text = " ".join([word for word in words if word.lower() not in stop_words])
    return jsonify({"filtered_text": filtered_text})

@app.route('/tokenize_text', methods=['POST'])
def tokenize_text():
    data = request.json
    text = data.get("text", "")
    tokens = word_tokenize(text)
    return jsonify({"tokens": tokens})

@app.route('/split_sentences', methods=['POST'])
def split_sentences():
    data = request.json
    text = data.get("text", "")
    sentences = sent_tokenize(text)
    return jsonify({"sentences": sentences})

@app.route('/wordnet_definition', methods=['POST'])
def wordnet_definition():
    data = request.json
    word = data.get("word", "")
    synsets = wordnet.synsets(word)
    definitions = [syn.definition() for syn in synsets]
    return jsonify({"definitions": definitions})

@app.route('/synonyms_antonyms', methods=['POST'])
def synonyms_antonyms():
    data = request.json
    word = data.get("word", "")
    synonyms, antonyms = set(), set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    return jsonify({"synonyms": list(synonyms), "antonyms": list(antonyms)})

@app.route('/pos_tagging', methods=['POST'])
def pos_tagging():
    data = request.json
    text = data.get("text", "")
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    return jsonify({"pos_tags": pos_tags})

@app.route('/lemmatize', methods=['POST'])
def lemmatize():
    data = request.json
    text = data.get("text", "")
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return jsonify({"lemmatized": lemmatized_words})

@app.route('/stemming', methods=['POST'])
def stemming():
    data = request.json
    text = data.get("text", "")
    stemmer = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return jsonify({"stemmed": stemmed_words})

@app.route('/restaurant_review_analysis', methods=['POST'])
def restaurant_review_analysis():
    data = request.json
    text = data.get("text", "")
    analysis = TextBlob(text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)
    