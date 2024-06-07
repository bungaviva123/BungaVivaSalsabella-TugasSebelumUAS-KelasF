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

# Menampilkan DataFrame hasil gabungan
print(df_merged)

# Membuat subplots
fig = plt.figure(figsize=(14, 18))
gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1], hspace=0.4, wspace=0.3)

# Diagram batang 1: Total penjualan per kategori
ax1 = fig.add_subplot(gs[0, 0])
sns.barplot(x='Kategori', y='Total (IDR)', data=df_merged, estimator=sum, ax=ax1)
ax1.set_title('Total Penjualan per Kategori')
ax1.set_ylabel('Total Penjualan (IDR)')
ax1.set_xlabel('Kategori')

# Diagram batang 2: Jumlah stok per kategori
ax2 = fig.add_subplot(gs[1, 0])
sns.barplot(x='Kategori', y='Jumlah Stok', data=df_merged, estimator=sum, ax=ax2)
ax2.set_title('Jumlah Stok per Kategori')
ax2.set_ylabel('Jumlah Stok')
ax2.set_xlabel('Kategori')

# Diagram batang 3: Penjualan per produk
ax3 = fig.add_subplot(gs[2, 0])
sns.barplot(x='Nama produk', y='Total (IDR)', data=df_merged, estimator=sum, ax=ax3)
ax3.set_title('Penjualan per Produk')
ax3.set_ylabel('Total Penjualan (IDR)')
ax3.set_xlabel('Nama Produk')

# Dotplot 1: Total penjualan per kategori
ax4 = fig.add_subplot(gs[0, 1])
sns.stripplot(x='Kategori', y='Total (IDR)', data=df_merged, jitter=True, ax=ax4)
ax4.set_title('Dotplot Total Penjualan per Kategori')
ax4.set_ylabel('Total Penjualan (IDR)')
ax4.set_xlabel('Kategori')

# Dotplot 2: Jumlah stok per kategori
ax5 = fig.add_subplot(gs[1, 1])
sns.stripplot(x='Kategori', y='Jumlah Stok', data=df_merged, jitter=True, ax=ax5)
ax5.set_title('Dotplot Jumlah Stok per Kategori')
ax5.set_ylabel('Jumlah Stok')
ax5.set_xlabel('Kategori')

# Dotplot 3: Penjualan per produk
ax6 = fig.add_subplot(gs[2, 1])
sns.stripplot(x='Nama produk', y='Total (IDR)', data=df_merged, jitter=True, ax=ax6)
ax6.set_title('Dotplot Penjualan per Produk')
ax6.set_ylabel('Total Penjualan (IDR)')
ax6.set_xlabel('Nama Produk')

# Menampilkan plot
plt.tight_layout()
plt.show()
