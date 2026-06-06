import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graph_logic import SocialGraph

sg = SocialGraph()

st.title('DSS Relasi Sosial Media')

menu = st.sidebar.selectbox('Menu', [
    'Tambah User',
    'Tambah Relasi',
    'Visualisasi Graph',
    'Cari Jalur Pertemanan',
    'Rekomendasi Teman',
    'Analisis User Populer'
])

if menu == 'Tambah User':
    user = st.text_input('Nama User Baru')
    if st.button('Tambah'):
        if user:
            sg.add_user(user)
            st.success(f'User {user} ditambahkan!')
        else:
            st.warning('Nama user tidak boleh kosong.')

elif menu == 'Tambah Relasi':
    users = sg.get_users()
    user = st.selectbox('User', users)
    friend = st.selectbox('Teman', users)
    if st.button('Tambah Relasi'):
        if user != friend:
            sg.add_relation(user, friend)
            st.success(f'Relasi {user} → {friend} ditambahkan!')
        else:
            st.warning('User dan Teman tidak boleh sama.')

elif menu == 'Visualisasi Graph':
    G = sg.graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12, arrows=True)
    st.pyplot(plt)
    st.write('Nodes:', sg.get_users())
    st.write('Edges:', sg.get_relations())

elif menu == 'Cari Jalur Pertemanan':
    st.header('Hasil Pencarian')
    users = sg.get_users()
    
    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox('Dari', users, key='source')
    with col2:
        target = st.selectbox('Ke', users, key='target')
    
    if st.button('Cari Jalur', key='search_button'):
        if source == target:
            st.warning('Pilih user yang berbeda untuk mencari jalur.')
        else:
            result = sg.bfs_path_detailed(source, target)
            
            if result:
                # Display path found message
                st.success(f'Jalur ditemukan dari {source} ke {target}.')
                
                # Display the path
                path_str = ' → '.join(result['path'])
                st.info(f'**Jalur BFS:** {path_str}')
                
                # Display path metrics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric('Panjang jalur', f"{result['path_length']} hop")
                with col2:
                    st.metric('Jumlah node dikunjungi', len(result['visited']))
                
                # Display visited nodes
                st.subheader('Node yang dikunjungi:')
                visited_list = result['visited']
                node_display = '[\n'
                for i, node in enumerate(visited_list):
                    node_display += f'  {i} : "{node}"\n'
                node_display += ']'
                st.code(node_display, language='python')
                
                # Display BFS steps detail
                with st.expander('Detail Langkah BFS'):
                    for step in result['steps']:
                        st.write(f"• Kunjungi: **{step['from']}** → Masukkan: **{step['to']}**")
                
            else:
                st.error('Tidak ada jalur pertemanan.')

elif menu == 'Rekomendasi Teman':
    users = sg.get_users()
    user = st.selectbox('Pilih User', users)
    if st.button('Rekomendasikan'):
        recs = sg.recommend_friends(user)
        if recs:
            st.info('Rekomendasi teman: ' + ', '.join(recs))
        else:
            st.warning('Tidak ada rekomendasi teman.')

elif menu == 'Analisis User Populer':
    top_n = st.slider('Top N', 1, 10, 3)
    popular = sg.most_popular_users(top_n)
    st.write('User paling populer:')
    for user, deg in popular:
        st.write(f'{user} ({deg} koneksi masuk)')
