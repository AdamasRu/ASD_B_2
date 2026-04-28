# main.py

from queue_LL import QueueLinkedList
from slot_management import SlotManager


def main():

    queue = QueueLinkedList()

    slot_manager = SlotManager()

    # Tambah mobil
    queue.enqueue(
        "Andi",
        "08123456789",
        "B1234CD",
        "Cuci Biasa",
        50000
    )

    queue.enqueue(
        "Budi",
        "08987654321",
        "B5678EF",
        "Cuci Premium",
        75000
    )

    queue.enqueue(
        "Cici",
        "08222222222",
        "B9999GH",
        "Cuci Biasa",
        50000
    )

    # Tampilkan queue
    queue.display_queue()

    # Assign ke slot
    slot_manager.assign_mobil(queue)

    slot_manager.display_slots()

    # Assign lagi (untuk slot kedua)
    slot_manager.assign_mobil(queue)

    slot_manager.display_slots()

    # Selesaikan slot 1
    slot_manager.selesai_cuci(1)

    slot_manager.display_slots()

    # Assign lagi
    slot_manager.assign_mobil(queue)

    slot_manager.display_slots()


if __name__ == "__main__":
    main()