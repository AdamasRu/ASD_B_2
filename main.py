# main.py

from queue_LL import QueueLinkedList
from slot_management import SlotManager
from transaksi import TransaksiManager


def tampilkan_menu():

    print("\n=== SISTEM CARWASH CLI ===")

    print("1. Tambah Mobil ke Antrian")
    print("2. Tampilkan Antrian")
    print("3. Proses Slot (Assign Mobil)")
    print("4. Selesaikan Cuci")
    print("5. Tampilkan Slot")
    print("6. Lihat Transaksi")
    print("7. Total Pendapatan")
    print("0. Keluar")


def main():

    queue = QueueLinkedList()

    slot_manager = SlotManager()

    transaksi_manager = TransaksiManager()

    while True:

        tampilkan_menu()

        pilihan = input("Pilih menu: ")

        # TAMBAH MOBIL
        if pilihan == "1":

            print("\n=== TAMBAH MOBIL ===")

            nama = input("Nama pelanggan: ")

            no_hp = input("No HP: ")

            plat = input("Plat nomor: ")

            jenis = input("Jenis layanan: ")

            try:

                harga = int(
                    input("Harga layanan: ")
                )

            except ValueError:

                print("Harga harus angka!")

                continue

            queue.enqueue(
                nama,
                no_hp,
                plat,
                jenis,
                harga
            )

        elif pilihan == "2":

            queue.display_queue()

        elif pilihan == "3":

            slot_manager.assign_mobil(queue)

        elif pilihan == "4":

            try:

                id_slot = int(
                    input("Masukkan ID Slot: ")
                )

            except ValueError:

                print("ID Slot harus angka!")

                continue

            mobil, waktu_mulai = \
                slot_manager.selesai_cuci(id_slot)

            if mobil:

                metode = input(
                    "Metode pembayaran: "
                )

                transaksi_manager.buat_transaksi(
                    mobil=mobil,
                    waktu_mulai=waktu_mulai,
                    metode_pembayaran=metode
                )

        elif pilihan == "5":

            slot_manager.display_slots()

        elif pilihan == "6":

            transaksi_manager.display_transaksi()

        elif pilihan == "7":

            total = \
                transaksi_manager.hitung_total_pendapatan()

            print(
                f"Total pendapatan: Rp {total}"
            )

        elif pilihan == "0":

            print("Keluar dari program.")

            break

        else:

            print("Pilihan tidak valid!")


if __name__ == "__main__":

    main()