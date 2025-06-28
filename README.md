# text_summarization_tool (backend + GUI)

Description:-
This project is a Python-based application designed to summarize lengthy articles or text passages using Natural Language Processing (NLP) techniques.<br>
The tool implements an extractive summarization approach by identifying and ranking the most informative sentences from a given input. <br>
To enhance accessibility and ease of use, the project includes a simple Graphical User Interface (GUI) created with `tkinter`. The GUI consists of an input text area where users can paste or type content, a "Summarize" button to trigger the summarization process, and an output text area to display the generated summary. The interface is minimal, clean, and beginner-friendly, making it suitable for students, researchers, and content editors alike.<br>
This tool serves as a demonstration of how fundamental NLP techniques can be combined to build efficient, offline-capable text processing applications without requiring any deep learning models or external APIs. It is especially useful for summarizing articles, academic content, reports, or any long-form writing where quick overviews are needed. The project is open for future enhancements such as abstractive summarization, file input/output options, and multilingual support.<br>

Requirements:-
  Python 3.7 or higher<br>
  nltk (Natural Language Toolkit)<br>
  scikit-learn (for TF-IDF vectorization)<br>
  networkx (for PageRank algorithm)<br>
  tkinter (usually comes pre-installed with Python)<br>

Features:-
  Extractive summarization using classic NLP techniques<br>
  TF-IDF + Cosine Similarity to measure sentence importance<br>
  PageRank algorithm to rank and select top sentences<br>
  Interactive GUI using tkinter for input/output<br>
  Offline functionality — No internet or API needed after setup<br>
  Fast and efficient — runs on basic hardware<br>
