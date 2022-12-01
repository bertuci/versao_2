
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

hashed_passwords = stauth.Hasher(['123', '456']).generate()

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    df = pd.read_excel('resultado.xlsx')
    st.title('Melhores Resultados da Bolsa')

    # df = pd.read_excel('resultado.xlsx')

    df['% entrada'] = df['% entrada'] * 100
    df['% entrada'] = df['% entrada'].astype(str)
    df['% entrada'] = df['% entrada'].str[:5]
    df['% entrada'] = df['% entrada'].astype(str) + '%'

    df['RESULTADO'] = df['RESULTADO'] * 100
    df['RESULTADO'] = df['RESULTADO'].astype(str)
    df['RESULTADO'] = df['RESULTADO'].str[:5]
    df['RESULTADO'] = df['RESULTADO'].astype(str) + '%'

    df['MEDIA'] = df['MEDIA'] * 100
    df['MEDIA'] = df['MEDIA'].astype(str)
    df['MEDIA'] = df['MEDIA'].str[:5]
    df['MEDIA'] = df['MEDIA'].astype(str) + '%'

    df['GAIN %'] = df['GAIN %'] * 100
    df['GAIN %'] = df['GAIN %'].astype(str)
    df['GAIN %'] = df['GAIN %'].str[:5]
    df['GAIN %'] = df['GAIN %'].astype(str) + '%'

    df['LOSS %'] = df['LOSS %'] * 100
    df['LOSS %'] = df['LOSS %'].astype(str)
    df['LOSS %'] = df['LOSS %'].str[:5]
    df['LOSS %'] = df['LOSS %'].astype(str) + '%'

    df['MAIOR LOSS'] = df['MAIOR LOSS'] * 100
    df['MAIOR LOSS'] = df['MAIOR LOSS'].astype(str)
    df['MAIOR LOSS'] = df['MAIOR LOSS'].str[:5]
    df['MAIOR LOSS'] = df['MAIOR LOSS'].astype(str) + '%'

    df['MAIOR GAIN'] = df['MAIOR GAIN'] * 100
    df['MAIOR GAIN'] = df['MAIOR GAIN'].astype(str)
    df['MAIOR GAIN'] = df['MAIOR GAIN'].str[:5]
    df['MAIOR GAIN'] = df['MAIOR GAIN'].astype(str) + '%'

    # st.dataframe(df)

    with st.sidebar:
        option = st.selectbox(
            'Filtro de Gain',
            ('Maior que 70%', 'Menor que 70%'))

    if option == 'Maior que 70%':
        df = df[df['GAIN %'] >= '70%']
        st.dataframe(df)

    if option == 'Menor que 70%':
        df = df[df['GAIN %'] <= '70%']
        st.dataframe(df)


    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')


    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='resultado.xlsx',
        mime='text/csv',
    )





elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')





with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)


    






#if st.checkbox('WordCloud'):


#    st.dataframe(df_teste)


#col1, col2, col3 = st.columns([1,2,1])

#with col2:
#    with st.form("login"):
#        st.markdown("### Painel de login")
#        st.text_input('Email', placeholder = 'Digite aqui seu email')
#        st.text_input('Senha', placeholder='Digite aqui sua senha', type="password")
#        st.form_submit_button('Login')
