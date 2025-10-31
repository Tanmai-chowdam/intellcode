import ast
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein

def tokenize_code(code):
    """Tokenize code into identifiers and keywords."""
    tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', code)
    return ' '.join(tokens)

def compute_cosine_similarity(code1, code2):
    """Cosine similarity based on token frequency."""
    vectorizer = CountVectorizer().fit_transform([code1, code2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0][1]

def compute_levenshtein(code1, code2):
    """Levenshtein-based structural similarity."""
    distance = Levenshtein.distance(code1, code2)
    max_len = max(len(code1), len(code2))
    return 1 - distance / max_len

def compute_ast_similarity(code1, code2):
    """Compare AST node structures."""
    try:
        tree1 = ast.dump(ast.parse(code1))
        tree2 = ast.dump(ast.parse(code2))
        return compute_cosine_similarity(tree1, tree2)
    except Exception:
        return 0.0

def combined_similarity(code1, code2):
    """Combine multiple similarity metrics."""
    t1, t2 = tokenize_code(code1), tokenize_code(code2)

    cosine = compute_cosine_similarity(t1, t2)
    lev = compute_levenshtein(t1, t2)
    ast_sim = compute_ast_similarity(code1, code2)

    final_score = (0.4 * cosine) + (0.3 * lev) + (0.3 * ast_sim)
    return round(final_score * 100, 2)
