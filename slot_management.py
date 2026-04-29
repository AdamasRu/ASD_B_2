from datetime import datetime

class Slot:

    def __init__(self, id_slot: int):

        self.id_slot = id_slot

        self.mobil = None

        self.waktu_mulai = None

        self.status = "KOSONG"


    def isi_slot(self, mobil):

        self.mobil = mobil

        self.waktu_mulai = datetime.now()

        self.status = "TERPAKAI"

        mobil.status = "DICUCI"


    def kosongkan_slot(self):

        mobil_selesai = self.mobil

        if mobil_selesai:
            mobil_selesai.status = "SELESAI"

        self.mobil = None

        self.waktu_mulai = None

        self.status = "KOSONG"

        return mobil_selesai

class SlotManager:

    def __init__(self):

        self.slots = [

            Slot(1),
            Slot(2)

        ]


    def assign_mobil(self, queue):

        for slot in self.slots:

            if slot.status == "KOSONG":

                if not queue.is_empty():

                    mobil = queue.dequeue()

                    slot.isi_slot(mobil)

                    print(
                        f"Mobil {mobil.plat_nomor} "
                        f"masuk ke Slot {slot.id_slot}"
                    )

    def selesai_cuci(self, id_slot: int):

        for slot in self.slots:

            if slot.id_slot == id_slot:

                if slot.status == "TERPAKAI":

                    mobil = slot.mobil

                    waktu_mulai = slot.waktu_mulai

                    slot.kosongkan_slot()

                    print(
                        f"Mobil {mobil.plat_nomor} "
                        f"selesai dari Slot {id_slot}"
                    )

                    return mobil, waktu_mulai

                else:

                    print("Slot sudah kosong.")

                    return None, None

        print("Slot tidak ditemukan.")

        return None, None


    def display_slots(self):

        print("\n=== STATUS SLOT ===")

        for slot in self.slots:

            if slot.status == "KOSONG":

                print(
                    f"Slot {slot.id_slot} : KOSONG"
                )

            else:

                mobil = slot.mobil

                print(
                    f"Slot {slot.id_slot} : "
                    f"{mobil.plat_nomor} "
                    f"({mobil.status})"
                )