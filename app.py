# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Model Regression </h1>", unsafe_allow_html=True)
st.markdown('---'*10)


# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

# Ini merupakan fungsi utama
def main():
    
    # Nilai awal
    rd = 250000
    adm = 400000
    mkt = 65000
    akp = 100000
    fn = 500000
    pr2 = 150000
    
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            rd = st.number_input('R&D', value=rd)
        with col2:
            adm = st.number_input('Administrasi', value=adm)
        with col3:
           mkt = st.number_input('Marketing', value=mkt)
        with col4:
           akp = st.number_input('Numbers', value=akp)
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fn = st.number_input('Finance', value= fn)
        with col2:
            pr2 = st.number_input('Profit2', value= pr2)
            
    st.markdown('---'*10)
    
    wly = st.selectbox('Lokasi', ('New York', 'California', 'Florida', 'Oklahoma'))
    
    data = {
        'R&D': rd,
        'Administrasi': adm,
        'Marketing': mkt,
        'Wilayah': wly,
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # load model
    my_model = pickle.load(open('model_regresi_terbaik.pkl', 'rb'))
    
    # Predict
    result = round(float(final_prediction(df_final, my_model)),2)
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Predicted Profit= ', result,'</b></h3>', unsafe_allow_html=True)
           
if __name__ == '__main__':
	main() 
