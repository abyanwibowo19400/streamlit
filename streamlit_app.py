import streamlit as st


st.title("Kalkulator Sederhana")

#HINT : INPUT
angka1 = st.number_input("Masukkan angka pertama", format="%.2f")
angka2 = st.number_input("Masukkan angka kedua", format="%.2f")

satuan_asal = st.selectbox("Pilih operasi", ["Tambah", "Kurang", "Kali", "Bagi"])

if st.button("Hitung"):
    if satuan_asal == "Tambah":
        hasil = angka1 + angka2
        st.success(f"Hasil : {hasil}")
    elif satuan_asal == "Kurang":
        hasil = angka1 - angka2
        st.success(f"Hasil : {hasil}")
    elif satuan_asal == "Kali":
        hasil = angka1 * angka2
        st.success(f"Hasil : {hasil}")
    elif satuan_asal == "Bagi":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil : {hasil}")
        else:
            st.error("Tidak bisa membagi dengan nol!")
        