import streamlit as st
from keras.preprocessing.sequence import pad_sequences
import pickle
import time
import numpy as np
import torch
from torch import optim
import torch.nn.functional as F
from transformers import BertForSequenceClassification, BertTokenizer, BertConfig


# Load trained tokenizer with pickle
with open('../tuned_model/tokenizer.pkl', 'rb') as handle:
	tokenizer = pickle.load(handle)


# Instantiate trained model
config = BertConfig.from_pretrained('../tuned_model/config.json')
model = BertForSequenceClassification.from_pretrained('../tuned_model/', config=config)

def labelling(result):

	if result == 1:
		return 'Mirip'
	else: 
		return 'Berbeda'	

def run():
	first_question = []
	second_question = []

	st.title('Identifikasi Duplikat Pertanyaan dan Kesamaan Kata')
	st.text('')
	st.subheader('Kenapa ini dikembangkan?')
	st.markdown('''Dilatarbelakangi dengan lebih dari 100 juta orang mengunjungi Quora setiap bulan, banyak orang mengajukan pertanyaan serupa. Memanfaatkan **BERT** sebagai *Deep Learning*, identifikasi pertanyaan-pertanyaan ini dapat dilakukan secara akurat dan akan membantu pengguna menemukan jawaban dengan lebih efektif dan efisien.
  \nTerlebih lagi, anda juga bisa memeriksa kesamaan kata melalui Web App sederhana ini :sunglasses:
  \nThis web App use **IndoBERT** as the language model. **Big thanks and hats off to IndoNLU Team** :tada:''')
	st.text('')

	question_1 = st.text_input('Masukkan Teks/Pertanyaan Pertama Anda')
	question_2 = st.text_input('Masukkan Teks/Pertanyaan Kedua Anda')

	first_question.append(question_1)
	second_question.append(question_2)

	if st.button('Predict'):
		with st.spinner('Sedang mengidentifikasi...'):
			if question_1 is not '' and question_2 is not '':
				encoded_inputs = tokenizer.encode_plus(question_1, question_2, add_special_tokens=True, return_token_type_ids=True)
				subwords, token_type_ids = encoded_inputs["input_ids"], encoded_inputs["token_type_ids"]
				
				subwords = torch.LongTensor(subwords).view(1, -1).to(model.device)
				token_type_ids = torch.LongTensor(token_type_ids).view(1, -1).to(model.device)
				
				logits = model(subwords, token_type_ids=token_type_ids)[0]
				label = torch.topk(logits, k=1, dim=-1)[1].squeeze().item()

				hasil = labelling(label)
			else:
				st.write('[INFO] Tidak ada teks.. Silahkan tulis teks terlebih dahulu')


			st.success(f"Dua teks tersebut hasilnya: **{hasil}** dengan **{F.softmax(logits, dim=-1).squeeze()[label] * 100:.3f}%** probability")
	
	st.text('')
	st.text('')
	st.text('')
	st.markdown('''Also thanks to _@anjasopo_ as my learning partner :v:
	\nAaaand special credit for **Alde Satriayu Putri Nadeak**, my sweetheart :yellow_heart:''')



if __name__ == '__main__':

	run()



