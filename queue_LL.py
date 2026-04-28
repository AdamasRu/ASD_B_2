from node import NodeMobil
from datetime import datetime


class QueueLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # Auto increment id
        self.next_id = 1


    # =========================
    # CEK APAKAH KOSONG
    # =========================
    def is_empty(self):
        return self.size == 0


    # =========================
    # ENQUEUE (Tambah Mobil)
    # =========================
    def enqueue(
        self,
        nama_pelanggan,
        no_hp,
        plat_nomor,
        jenis_layanan,
        harga
    ):

        waktu_masuk = datetime.now()

        new_node = NodeMobil(
            id_antrian=self.next_id,
            nama_pelanggan=nama_pelanggan,
            no_hp=no_hp,
            plat_nomor=plat_nomor,
            jenis_layanan=jenis_layanan,
            harga=harga,
            waktu_masuk=waktu_masuk
        )

        self.next_id += 1

        if self.is_empty():

            self.head = new_node
            self.tail = new_node

        else:

            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

        print("Mobil berhasil ditambahkan ke antrian.")


    # =========================
    # DEQUEUE (Ambil Mobil Depan)
    # =========================
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong.")
            return None

        removed_node = self.head

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1

        removed_node.next = None

        return removed_node


    # =========================
    # PEEK (Lihat Depan)
    # =========================
    def peek(self):

        if self.is_empty():
            return None

        return self.head


    # =========================
    # DISPLAY ANTRIAN
    # =========================
    def display_queue(self):

        if self.is_empty():
            print("Antrian kosong.")
            return

        current = self.head

        print("\n=== DAFTAR ANTRIAN ===")

        while current:

            print(current)

            current = current.next

        print(f"Total antrian: {self.size}")


    # =========================
    # GET SIZE
    # =========================
    def get_size(self):
        return self.size