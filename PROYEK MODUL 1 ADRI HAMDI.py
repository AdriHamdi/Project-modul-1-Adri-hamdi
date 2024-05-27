
data_karyawan = [
    {'nama': 'Andi', 'nomor_ktp': '111', 'jenis_kelamin': 'Laki-laki', 'status_nikah': 'Belum Menikah', 'gaji': '5000', 'promosi': 'Layak'},
    {'nama': 'Budi', 'nomor_ktp': '222', 'jenis_kelamin': 'Laki-laki', 'status_nikah': 'Menikah', 'gaji': '7000', 'promosi': 'Tidak Layak'},
    {'nama': 'Citra', 'nomor_ktp': '333', 'jenis_kelamin': 'Perempuan', 'status_nikah': 'Belum Menikah', 'gaji': '6000', 'promosi': 'Layak'}
]

def read_data():
    while True:
        print("\nMenu:")
        print("1. Tampilkan semua data karyawan")
        print("2. Tampilkan data karyawan berdasarkan nomor KTP")
        print("3. Tampilkan data karyawan berdasarkan nama")
        print("4. Tampilkan data karyawan berdasarkan gaji")
        print("5. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            print("\nTampilkan semua data karyawan:")
            print("=" * 110)
            print("| {:<10} | {:<10} | {:<12} | {:<15} | {:<8} | {:<10} |".format('Nama', 'Nomor KTP', 'Jenis Kelamin', 'Status Nikah', 'Gaji', 'Promosi'))
            print("=" * 110)
            for karyawan in data_karyawan:
                print("| {:<10} | {:<10} | {:<12} | {:<15} | {:>8} | {:<10} |".format(karyawan['nama'], karyawan['nomor_ktp'], karyawan['jenis_kelamin'], karyawan['status_nikah'], karyawan['gaji'], karyawan['promosi']))
            print("=" * 110)
        elif pilihan == '2':
            nomor_ktp = input("\nMasukkan nomor KTP karyawan yang ingin ditampilkan (atau ketik 'exit' untuk kembali): ")
            if nomor_ktp.lower() == 'exit':
                return
            found = False
            print("\nTampilkan data karyawan berdasarkan nomor KTP:")
            print("=" * 110)
            print("| {:<10} | {:<10} | {:<12} | {:<15} | {:<8} | {:<10} |".format('Nama', 'Nomor KTP', 'Jenis Kelamin', 'Status Nikah', 'Gaji', 'Promosi'))
            print("=" * 110)
            for karyawan in data_karyawan:
                if karyawan['nomor_ktp'] == nomor_ktp:
                    found = True
                    print("| {:<10} | {:<10} | {:<12} | {:<15} | {:>8} | {:<10} |".format(karyawan['nama'], karyawan['nomor_ktp'], karyawan['jenis_kelamin'], karyawan['status_nikah'], karyawan['gaji'], karyawan['promosi']))
            print("=" * 110)
            if not found:
                print("Nomor KTP tidak ditemukan.")
        elif pilihan == '3':
            nama = input("\nMasukkan nama karyawan yang ingin ditampilkan (atau ketik 'exit' untuk kembali): ")
            if nama.lower() == 'exit':
                return
            found = False
            print("\nTampilkan data karyawan berdasarkan nama:")
            print("=" * 110)
            print("| {:<10} | {:<10} | {:<12} | {:<15} | {:<8} | {:<10} |".format('Nama', 'Nomor KTP', 'Jenis Kelamin', 'Status Nikah', 'Gaji', 'Promosi'))
            print("=" * 110)
            for karyawan in data_karyawan:
                if karyawan['nama'].lower() == nama.lower():
                    found = True
                    print("| {:<10} | {:<10} | {:<12} | {:<15} | {:>8} | {:<10} |".format(karyawan['nama'], karyawan['nomor_ktp'], karyawan['jenis_kelamin'], karyawan['status_nikah'], karyawan['gaji'], karyawan['promosi']))
            print("=" * 110)
            if not found:
                print("Nama karyawan tidak ditemukan.")
        elif pilihan == '4':
            gaji = input("\nMasukkan gaji karyawan yang ingin ditampilkan (atau ketik 'exit' untuk kembali): ")
            if gaji.lower() == 'exit':
                return
            found = False
            print("\nTampilkan data karyawan berdasarkan gaji:")
            print("=" * 110)
            print("| {:<10} | {:<10} | {:<12} | {:<15} | {:<8} | {:<10} |".format('Nama', 'Nomor KTP', 'Jenis Kelamin', 'Status Nikah', 'Gaji', 'Promosi'))
            print("=" * 110)
            for karyawan in data_karyawan:
                if karyawan['gaji'] == gaji:
                    found = True
                    print("| {:<10} | {:<10} | {:<12} | {:<15} | {:>8} | {:<10} |".format(karyawan['nama'], karyawan['nomor_ktp'], karyawan['jenis_kelamin'], karyawan['status_nikah'], karyawan['gaji'], karyawan['promosi']))
            print("=" * 110)
            if not found:
                print("Gaji karyawan tidak ditemukan.")
        elif pilihan == '5':
            return
        else:
            print("Pilihan tidak valid.")

def create_data():
    while True:
        print("\nTambah Data Karyawan (ketik 'exit' untuk kembali ke menu utama):")
        nama = input("Masukkan nama: ")
        if nama.lower() == 'exit':
            return
        nomor_ktp = input("Masukkan nomor KTP (3 digit): ")
        if nomor_ktp.lower() == 'exit':
            return
        jenis_kelamin = input("Masukkan jenis kelamin (L/P): ").upper()
        if jenis_kelamin == 'EXIT':
            return
        status_nikah = input("Masukkan status nikah (M/B): ").upper()
        if status_nikah == 'EXIT':
            return
        gaji = input("Masukkan gaji (4 digit): ")
        if gaji.lower() == 'exit':
            return
        promosi = input("Masukkan status promosi (L/T): ").upper()
        if promosi.lower() == 'exit':
            return

        if not nomor_ktp.isdigit() or len(nomor_ktp) != 3:
            print("Nomor KTP harus berupa 3 digit angka.")
            continue

        if jenis_kelamin not in ['L', 'P']:
            print("Jenis kelamin tidak valid.")
            continue
        else:
            jenis_kelamin = 'Laki-laki' if jenis_kelamin == 'L' else 'Perempuan'

        if status_nikah not in ['M', 'B']:
            print("Status nikah tidak valid.")
            continue
        else:
            status_nikah = 'Menikah' if status_nikah == 'M' else 'Belum Menikah'

        if not gaji.isdigit() or len(gaji) != 4:
            print("Gaji harus berupa 4 digit angka.")
            continue

        if promosi not in ['L', 'T']:
            print("Status promosi tidak valid.")
            continue
        else:
            promosi = 'Layak' if promosi == 'L' else 'Tidak Layak'

        if any(karyawan['nomor_ktp'] == nomor_ktp for karyawan in data_karyawan):
            print("Karyawan dengan nomor KTP ini sudah ada.")
            continue

        confirm = input("Apakah Anda ingin menyimpan data ini? (ya/tidak): ").lower()
        if confirm == 'ya':
            data_karyawan.append({
                'nama': nama,
                'nomor_ktp': nomor_ktp,
                'jenis_kelamin': jenis_kelamin,
                'status_nikah': status_nikah,
                'gaji': gaji,
                'promosi': promosi
            })
            print("Data berhasil disimpan.")
        else:
            print("Penyimpanan data dibatalkan.")
        break

def delete_data():
    while True:
        nomor_ktp = input("Masukkan nomor KTP karyawan yang ingin dihapus (atau ketik 'exit' untuk kembali): ")
        if nomor_ktp.lower() == 'exit':
            return
        if not nomor_ktp.isdigit() or len(nomor_ktp) != 3:
            print("Nomor KTP harus berupa 3 digit angka.")
            continue
        for karyawan in data_karyawan:
            if karyawan['nomor_ktp'] == nomor_ktp:
                confirm = input(f"Apakah Anda yakin ingin menghapus data karyawan {karyawan['nama']}? (ya/tidak): ")
                if confirm.lower() == 'ya':
                    data_karyawan.remove(karyawan)
                    print("Data karyawan berhasil dihapus.")
                else:
                    print("Penghapusan data dibatalkan.")
                return
        print("Nomor KTP tidak ditemukan.")

def replace_data():
    while True:
        nomor_ktp = input("Masukkan nomor KTP karyawan yang ingin diganti (atau ketik 'exit' untuk kembali): ")
        if nomor_ktp.lower() == 'exit':
            return
        if not nomor_ktp.isdigit() or len(nomor_ktp) != 3:
            print("Nomor KTP harus berupa 3 digit angka.")
            continue
        
        # Cari karyawan dengan nomor KTP yang sesuai
        found = False
        for karyawan in data_karyawan:
            if karyawan['nomor_ktp'] == nomor_ktp:
                found = True
                # Meminta input untuk data baru
                nama_baru = input("Masukkan nama baru: ")
                if nama_baru.lower() == 'exit':
                    return
                nomor_ktp_baru = input("Masukkan nomor KTP baru (3 digit): ")
                if nomor_ktp_baru.lower() == 'exit':
                    return
                jenis_kelamin_baru = input("Masukkan jenis kelamin baru (L/P): ").upper()
                if jenis_kelamin_baru == 'EXIT':
                    return
                status_nikah_baru = input("Masukkan status nikah baru (M/B): ").upper()
                if status_nikah_baru == 'EXIT':
                    return
                gaji_baru = input("Masukkan gaji baru (4 digit): ")
                if gaji_baru.lower() == 'exit':
                    return
                promosi_baru = input("Masukkan status promosi baru (L/T): ").upper()
                if promosi_baru.lower() == 'exit':
                    return

                if not nomor_ktp_baru.isdigit() or len(nomor_ktp_baru) != 3:
                    print("Nomor KTP harus berupa 3 digit angka.")
                    continue

                if jenis_kelamin_baru not in ['L', 'P']:
                    print("Jenis kelamin tidak valid.")
                    continue

                if status_nikah_baru not in ['M', 'B']:
                    print("Status nikah tidak valid.")
                    continue
                else:
                    status_nikah_baru = 'Menikah' if status_nikah_baru == 'M' else 'Belum Menikah'

                if not gaji_baru.isdigit() or len(gaji_baru) != 4:
                    print("Gaji harus berupa 4 digit angka.")
                    continue

                if promosi_baru not in ['L', 'T']:
                    print("Status promosi tidak valid.")
                    continue
                else:
                    promosi_baru = 'Layak' if promosi_baru == 'L' else 'Tidak Layak'

                confirm = input("Apakah Anda ingin mengganti data ini? (ya/tidak): ")
                if confirm.lower() == 'ya':
                    # Mengganti data karyawan
                    karyawan['nama'] = nama_baru
                    karyawan['nomor_ktp'] = nomor_ktp_baru
                    karyawan['jenis_kelamin'] = 'Laki-laki' if jenis_kelamin_baru == 'L' else 'Perempuan'
                    karyawan['status_nikah'] = status_nikah_baru
                    karyawan['gaji'] = gaji_baru
                    karyawan['promosi'] = promosi_baru
                    print("Data berhasil diganti.")
                else:
                    print("Penggantian data dibatalkan.")
                return
        if not found:
            print("Nomor KTP tidak ditemukan.")

def main():
    while True:
        print("\nMenu Utama:")
        print("1. Baca Data Karyawan")
        print("2. Tambah Data Karyawan")
        print("3. Hapus Data Karyawan")
        print("4. Ganti Data Karyawan")
        print("5. Mengurut Data Karyawan")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '1':
            read_data()
        elif pilihan == '2':
            create_data()
        elif pilihan == '3':
            delete_data()
        elif pilihan == '4':
            replace_data()
        elif pilihan == '5':
            sort_data()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

def sort_data():
    while True:
        print("\nMenu Pengurutan:")
        print("1. Urutkan karyawan berdasarkan nama")
        print("2. Urutkan karyawan berdasarkan gaji")
        print("3. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            sorted_by_name = sorted(data_karyawan, key=lambda x: x['nama'])
            print("\nKaryawan diurutkan berdasarkan nama:")
            print("=" * 110)
            print("| {:<10} | {:<10} | {:<12} | {:<15} | {:<8} | {:<10} |".format('Nama', 'Nomor KTP', 'Jenis Kelamin', 'Status Nikah', 'Gaji', 'Promosi'))
            print("=" * 110)
            for karyawan in sorted_by_name:
                print("| {:<10} | {:<10} | {:<12} | {:<15} | {:>8} | {:<10} |".format(karyawan['nama'], karyawan['nomor_ktp'], karyawan['jenis_kelamin'], karyawan['status_nikah'], karyawan['gaji'], karyawan['promosi']))
            print("=" * 110)
        elif pilihan == '2':
            sorted_by_salary = sorted(data_karyawan, key=lambda x: int(x['gaji']))
            print("\nKaryawan diurutkan berdasarkan gaji:")
            print("=" * 110)
            print("| {:<10} | {:<10} | {:<12} | {:<15} | {:<8} | {:<10} |".format('Nama', 'Nomor KTP', 'Jenis Kelamin', 'Status Nikah', 'Gaji', 'Promosi'))
            print("=" * 110)
            for karyawan in sorted_by_salary:
                print("| {:<10} | {:<10} | {:<12} | {:<15} | {:>8} | {:<10} |".format(karyawan['nama'], karyawan['nomor_ktp'], karyawan['jenis_kelamin'], karyawan['status_nikah'], karyawan['gaji'], karyawan['promosi']))
            print("=" * 110)
        elif pilihan == '3':
            return
        else:
            print("Pilihan tidak valid.")

main()
