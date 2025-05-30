{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "8473390e-6676-42ae-8ef2-4070accee63f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def reversePerKata(kalimat):\n",
    "    kata = kalimat.split() # untuk memisahkan kalimat jadi kata\n",
    "    hasil = []\n",
    "    for k in kata :\n",
    "        hasil.append(k[::-1]) #untuk membalik tiap kata\n",
    "    return hasil  #untuk menggabungkan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "a363599f-58d1-437a-8ac2-c3f3f26d7e1c",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1712393944.py, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[89], line 6\u001b[1;36m\u001b[0m\n\u001b[1;33m    return ' ' hasil\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def urutanKalimat(kalimat, urutan):\n",
    "    kata = kalimat.split() # untuk memisahkan kalimat jadi kata\n",
    "    hasil = []\n",
    "    for i in urutan :\n",
    "        hasil.append(kata[i - 1]) #karena urtan dimulai dari 1, dikurangi 1\n",
    "    return ' ' hasil\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a48948e1-b2f5-43ae-b15a-0d4025670530",
   "metadata": {},
   "outputs": [],
   "source": [
    "def gantiVocal(kalimat, pilihan):\n",
    "    hasil = ''\n",
    "    vocalKecil = {'a':'4', 'i':'1', 'u': '|_|', 'e':'3', 'o':'0'} # dictionary\n",
    "    vocalBesar = {'A':'4', 'I':'1', 'U': '|_|', 'E':'3', 'O':'0'}\n",
    "    for huruf in kalimat:\n",
    "        if pilihan==1 and huruf in vocalKecil:  #pilihan untuk vocal kecil\n",
    "            hasil += vocalKecil[huruf]\n",
    "        elif pilihan==2 and huruf in vocalBesar: #[ilihan untuk vocal besar\n",
    "            hasil += vocalBesar[huruf]\n",
    "        else:\n",
    "            hasil += huruf\n",
    "    return hasil\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "df0c07b9-da51-4b31-9658-00426d24bb90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['UKA', 'ATNIC', 'UMAK']\n",
      "PYTHON HARI BELAJAR SEDANG INI\n",
      "Ak|_| C1nt4 K4m|_|\n",
      "4ku Cinta Kamu\n"
     ]
    }
   ],
   "source": [
    "print(reversePerKata(\"AKU CINTA KAMU\"))\n",
    "print(urutanKalimat(\"HARI INI SEDANG BELAJAR PYTHON\", [5, 1, 4, 3, 2]))\n",
    "print(gantiVocal(\"Aku Cinta Kamu\", 1))\n",
    "print(gantiVocal(\"Aku Cinta Kamu\" , 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "92d51124-8bf5-4ee4-b644-018eaabaf1a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Masukkan Kalimat :  SAHLA NURUL\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hasil : ALHAS LURUN\n"
     ]
    }
   ],
   "source": [
    "#Coba Input\n",
    "#Balik kata\n",
    "kalimat1 = input(\"Masukkan Kalimat : \")\n",
    "print(\"Hasil :\", reversePerKata(kalimat1)) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "554de75c-ffdf-4954-b253-526de294d13a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Masukkan Kalimat :  HARI INI SEDANG MEMBUAT KUE\n",
      "Masukkan urutan :  2,5,3,1,4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hasil :  INI KUE SEDANG HARI MEMBUAT\n"
     ]
    }
   ],
   "source": [
    "#mengurutkan kata \n",
    "kalimat2 = input(\"\\nMasukkan Kalimat : \")\n",
    "urutan = input(\"Masukkan urutan : \")\n",
    "urutanList = [int(i) for i in urutan.split(',')]\n",
    "print(\"Hasil : \", urutanKalimat(kalimat2, urutanList))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "e1006fdd-fec1-4cda-8854-3c4ee8a845b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Masukkan Kalimat :  Aku Rindu Kamu\n",
      "Masukkan pilihan :  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hasil : Ak|_| R1nd|_| K4m|_|\n"
     ]
    }
   ],
   "source": [
    "#Menggnti huruf vocal dengan simbol tertentu\n",
    "kalimat3 = input(\"\\nMasukkan Kalimat : \")\n",
    "pilihan = int(input(\"Masukkan pilihan : \" )) \n",
    "print(\"Hasil :\" , gantiVocal(kalimat3, pilihan))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
