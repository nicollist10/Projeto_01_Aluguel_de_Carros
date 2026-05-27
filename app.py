import streamlit as st
st.title('top multimarcas')
st.subheader('“Mais do que dirigir um carro de luxo, aqui você vive uma experiência exclusiva, onde elegância, potência e sofisticação se encontram para transformar cada trajeto em um momento inesquecível.”')
st.subheader('“Cada detalhe foi pensado para quem não aceita o comum. Descubra uma nova forma de dirigir, com carros que unem luxo, tecnologia, conforto e desempenho em uma experiência criada para impressionar em todos os momentos.”')
st.sidebar.title('Seu próximo carro de luxo está aqui.')
st.sidebar.image('logo.png')
carros = ['bmw', 'audi', 'ferrari', 'mercedes', 'lamborghini', 'bugatti','mclaren']
opcao = st.sidebar.selectbox('escolha o carro que foi alugado ou comprado', carros)

st.image(f'{opcao}.png')
st.markdown(f'##Você acaba de escolher excelência sobre rodas c: {opcao}')
st.markdown('---')