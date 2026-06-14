<<<<<<< HEAD
import requests

TOKEN = "" #Ganti dengan token Fonnte

def kirim_whatsapp(
    nomor,
    pesan,
    file_url
):

    try:

        nomor = nomor.replace("+", "")

        if nomor.startswith("08"):
            nomor = "62" + nomor[1:]

        url = "https://api.fonnte.com/send"

        headers = {
            "Authorization": TOKEN
        }

        data = {
            "target": nomor,
            "message": pesan,
            "file": file_url
        }

        response = requests.post(
            url,
            headers=headers,
            data=data
        )

        print(response.text)

    except Exception as e:

=======
import requests

TOKEN = "" #Ganti dengan token Fonnte

def kirim_whatsapp(
    nomor,
    pesan,
    file_url
):

    try:

        nomor = nomor.replace("+", "")

        if nomor.startswith("08"):
            nomor = "62" + nomor[1:]

        url = "https://api.fonnte.com/send"

        headers = {
            "Authorization": TOKEN
        }

        data = {
            "target": nomor,
            "message": pesan,
            "file": file_url
        }

        response = requests.post(
            url,
            headers=headers,
            data=data
        )

        print(response.text)

    except Exception as e:

>>>>>>> 5fceec73727726b3ef910424eff48b115e568ffc
        print(e)