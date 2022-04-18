from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 500, 1000))
hunians.append(Rumah("Gustavo Fring", 5, 2, 600, 2000))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 100, 500))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 700, 2100))


root = Tk()
root.title("Praktikum DPBO Python")


def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    opt = LabelFrame(top, padx=10, pady=10)
    opt.pack(padx=10, pady=10)

    d_exit = Button(opt, text="Exit", command=top.quit)
    d_exit.grid(row=0, column=0)

    d_summary = Label(d_frame, text="Summary: ", anchor="w").grid(
        row=0, column=0, sticky="w")

    labelpemilik = Label(d_frame, text="Nama Pemilik", width=15,
                         borderwidth=1, relief="solid")
    labelpemilik.grid(row=1, column=0)

    pemilik = Label(d_frame, text=hunians[index].get_nama_pemilik(), width=60,
                    borderwidth=1, relief="solid")
    pemilik.grid(row=1, column=1)

    if hunians[index].get_jenis() == "Indekos":

        labelpenghuni = Label(d_frame, text="Nama Penghuni", width=15,
                              borderwidth=1, relief="solid")
        labelpenghuni.grid(row=2, column=0)

        penghuni = Label(d_frame, text=hunians[index].get_nama_penghuni(), width=60,
                         borderwidth=1, relief="solid")
        penghuni.grid(row=2, column=1)

    labeljmlPenghuni = Label(d_frame, text="Jumlah Penghuni", width=15,
                             borderwidth=1, relief="solid")
    labeljmlPenghuni.grid(row=3, column=0)

    jmlPenghuni = Label(d_frame, text=hunians[index].get_jml_penghuni(), width=60,
                        borderwidth=1, relief="solid")
    jmlPenghuni.grid(row=3, column=1)

    labeljmlKamar = Label(d_frame, text="Jumlah Kamar", width=15,
                          borderwidth=1, relief="solid")
    labeljmlKamar.grid(row=4, column=0)

    jmlKamar = Label(d_frame, text=hunians[index].get_jml_kamar(), width=60,
                     borderwidth=1, relief="solid")
    jmlKamar.grid(row=4, column=1)

    labelluas = Label(d_frame, text="Luas Tanah", width=15,
                      borderwidth=1, relief="solid")
    labelluas.grid(row=5, column=0)

    luas = Label(d_frame, text=hunians[index].get_luas_tanah(), width=60,
                 borderwidth=1, relief="solid")
    luas.grid(row=5, column=1)

    labellistrik = Label(d_frame, text="Kapasitas Listrik", width=15,
                         borderwidth=1, relief="solid")
    labellistrik.grid(row=6, column=0)

    listrik = Label(d_frame, text=hunians[index].get_kapasitas_listrik(), width=60,
                    borderwidth=1, relief="solid")
    listrik.grid(row=6, column=1)

    labeldoc = Label(d_frame, text="document", width=15,
                     borderwidth=1, relief="solid")
    labeldoc.grid(row=7, column=0)

    doc = Label(d_frame, text=hunians[index].get_dokumen(), width=60,
                borderwidth=1, relief="solid")
    doc.grid(row=7, column=1)


frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5,
                borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15,
                 borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos":
        name = Label(frame, text=" " + h.get_nama_pemilik(),
                     width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(),
                     width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ",
                      command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)


root.mainloop()
