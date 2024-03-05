import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Fungsi untuk menampilkan visualisasi pertama
def visualisasi_pertama(true_df):
    # Mengelompokkan data berdasarkan musim 
    seasonal_usage = true_df.groupby('musim')[['terdaftar', 'tdk_daftar']].sum().reset_index()
    
    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(
        seasonal_usage['musim'],
        seasonal_usage['terdaftar'],
        label='Terdaftar',
        color='tab:blue'
    )
    plt.bar(
        seasonal_usage['musim'],
        seasonal_usage['tdk_daftar'],
        label='Tidak Terdaftar',
        color='tab:orange'
    )
    plt.xlabel(None)
    plt.ylabel(None)
    plt.title('Jumlah penyewaan sepeda berdasarkan musim')
    plt.legend()
    plt.show()
    st.pyplot(plt)

# Fungsi untuk menampilkan visualisasi kedua
def visualisasi_kedua(true_df):
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15,10))
    sns.lineplot(
        x='hr_krj',
        y='jumlah',
        data=true_df,
        ax=axes[0])
    axes[0].set_title('Jumlah Pengguna Sepeda berdasarkan Hari Kerja')
    axes[0].set_xlabel('Hari Kerja')
    axes[0].set_ylabel('Jumlah Pengguna Sepeda')

    sns.lineplot(
        x='hr_lbr',
        y='jumlah',
        data=true_df,
        ax=axes[1])
    axes[1].set_title('Jumlah Pengguna Sepeda berdasarkan Hari Libur')
    axes[1].set_xlabel('Hari Libur')
    axes[1].set_ylabel('Jumlah Pengguna Sepeda')

    sns.lineplot(
        x='hr_biasa',
        y='jumlah',
        data=true_df,
        ax=axes[2])
    axes[2].set_title('Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu')
    axes[2].set_xlabel('Hari dalam Seminggu')
    axes[2].set_ylabel('Jumlah Pengguna Sepeda')

    plt.tight_layout()
    plt.show()
    st.pyplot(plt)

# Fungsi untuk menampilkan visualisasi ketiga
def visualisasi_ketiga(true_df):
    plt.figure(figsize=(10,6))
    sns.stripplot(
        x='kondisi_cuaca',
        y='jumlah',
        data=true_df,
        alpha=0.5)

    plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.show()
    st.pyplot(plt)

# Load data
true_df = pd.read_csv("dashboard/true.csv")

# Judul halaman
st.title("Selamat Datang di Dashboard Sepedamu!🚴🏽‍♀️✨")

# Sidebar
menu = st.sidebar.radio("Menu", ("Data Diri", "Visualisasi 1", "Visualisasi 2", "Visualisasi 3"))

# Main content
if menu == "Data Diri":
    st.title(f"Proyek analisis data")
    st.subheader("About Me:")
    st.text("Nama: Fitria Amanda Pratiwi")
    st.text("Email: fitriaamanda13@gmail.com")
    st.text("ID Dicoding: fitriaamanda")
    st.subheader("Project Overview")
    st.text("Membuat analisis data terhadap dataset Bike Sharing Dataset")
    st.subheader("Pertanyaan bisnis:")
    st.text("1. Apakah musim berpengaruh terhadap preferensi penyewa sepeda, baik penyewa tidak terdaftar maupun yang terdaftar?")
    st.text("2. Bagaimana kondisi ketika sepeda digunakan pada hari kerja(hr_krj), hari libur(hr_lbr), dan hari biasa(hr_biasa)?")
    st.text("3. Apakah cuaca memiliki peran dalam jumlah penyewa sepeda?")
    st.caption('Fitria Amanda Pratiwi - MACHINE LEARNING - BANGKIT 2024')
elif menu == "Visualisasi 1":
    st.header("Visualisasi Jumlah Penyewaan Sepeda berdasarkan Musim")
    visualisasi_pertama(true_df)
elif menu == "Visualisasi 2":
    st.header("Visualisasi Jumlah Penyewaan Sepeda berdasarkan Hari")
    visualisasi_kedua(true_df)
elif menu == "Visualisasi 3":
    st.header("Visualisasi Jumlah Penyewaan Sepeda berdasarkan Kondisi Cuaca")
    visualisasi_ketiga(true_df)
