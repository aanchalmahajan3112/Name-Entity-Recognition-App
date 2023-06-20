import streamlit as st
import spacy_streamlit as spt
import spacy

nlp = spacy.load('en_core_web_sm')


def main():

	st.title('Name Entity Recognition(NER) APP')

	menu=['HOME','NER']
	choice = st.sidebar.selectbox('menu',menu)
	if choice == 'HOME':
		st.subheader('Word Tokenization')
		raw_text=st.text_area('Text to Tokenize ','Enter Text Here')
		docs=nlp(raw_text)
		if st.button('Tokenize'):
			spt.visualize_tokens(docs)
			
	elif choice == 'NER':
		st.subheader('Name Entity Recognition')
		raw_text=st.text_area('Text to Tokenize ','Enter Text Here')
		docs = nlp(raw_text)
		spt.visualize_ner(docs)



if __name__== '__main__':
		main()