import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data produk
data_produk = {
    'Produk ID': [1, 2, 3, 4, 5],
    'Nama produk': ['Laptop', 'Meja', 'Buku', 'Kamera', 'Kursi'],
    'Harga(IDR)': [10000000, 500000, 100000, 8000000, 700000],
    'Kategori': ['Elektronik', 'Perabotan', 'Perlengkapan', 'Elektronik', 'Perabotan']
}

# Data stok
data_stok = {
    'Produk ID': [1, 2, 3, 4, 5],
    'Jumlah Stok': [50, 100, 75, 30, 80]
}

# Data transaksi
data_transaksi = {
    'Transaksi ID': [1, 2, 3, 4, 5],
    'Produk ID': [1, 3, 2, 4, 5],
    'Pelanggan ID': [1, 2, 3, 4, 5],
    'Tanggal': ['5/1/2024', '5/2/2024', '5/3/2024', '5/4/2024', '5/5/2024'],
    'Jumlah': [2, 5, 1, 1, 3],
    'Total (IDR)': ["20,000,000", "500,000", "500,000", "8,000,000", "2,100,000"]
}

# Membuat DataFrame
df_produk = pd.DataFrame(data_produk)
df_stok = pd.DataFrame(data_stok)
df_transaksi = pd.DataFrame(data_transaksi)

# Mengubah kolom 'Total (IDR)' ke format numerik
df_transaksi['Total (IDR)'] = df_transaksi['Total (IDR)'].str.replace(',', '').astype(int)

# Menggabungkan DataFrame
df_merged = pd.merge(df_transaksi, df_produk, on='Produk ID')
df_merged = pd.merge(df_merged, df_stok, on='Produk ID')

# Menambahkan kolom 'Harga per Satuan'
df_merged['Harga per Satuan'] = df_merged['Harga(IDR)'] / df_merged['Jumlah Stok']

# Membuat scatter plot untuk korelasi antara 'Jumlah Stok' dan 'Harga per Satuan'
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='Jumlah Stok', y='Harga per Satuan', data=df_merged, ax=ax)
ax.set_title('Korelasi antara Jumlah Stok dan Harga per Satuan')
ax.set_xlabel('Jumlah Stok')
ax.set_ylabel('Harga per Satuan (IDR)')
plt.show()

# Menghitung dan menampilkan korelasi antara 'Jumlah Stok' dan 'Harga per Satuan'
correlation = df_merged['Jumlah Stok'].corr(df_merged['Harga per Satuan'])
print("Korelasi antara Jumlah Stok dan Harga per Satuan:", correlation)
