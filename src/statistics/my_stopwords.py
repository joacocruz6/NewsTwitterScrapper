from stop_words import get_stop_words
STOPWORDS = get_stop_words("es")
# Appending some useless and non informatic words to the stopwords
STOPWORDS.append("twitter")
STOPWORDS.append("http")
STOPWORDS.append("https")
STOPWORDS.append("bit")
STOPWORDS.append("ly")
STOPWORDS.append("com")
STOPWORDS.append("cl")
STOPWORDS.append("www")
STOPWORDS.append("tinyurl")
STOPWORDS.append("Señal")
STOPWORDS.append("pic")
STOPWORDS.append("AHORA")
STOPWORDS.append("meganoticias")
STOPWORDS.append("Sigue")
STOPWORDS.append("t13")
STOPWORDS.append("lacuarta")
STOPWORDS.append("YouTube")
STOPWORDS.append("mega")
STOPWORDS.append("vivo")
STOPWORDS.append("AHORA24H")
STOPWORDS.append("cronica")
STOPWORDS.append("noticia")
STOPWORDS.append("ÚLTIMO")
STOPWORDS.append("24Play")