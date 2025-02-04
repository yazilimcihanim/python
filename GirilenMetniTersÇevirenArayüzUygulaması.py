
# Mini bir Tkinter arayüzü

import tkinter as tk
def translate_text():
    input_text = input_entry.get()  # Kullanıcıdan alınan metni al
    output_label.config(text=f"Çeviri: {input_text[::-1]}")  # Metni ters çevirerek "çeviri" yap

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Mini Çeviri Uygulaması")
root.geometry("400x300")

# Kullanıcıdan metin girişi
input_label = tk.Label(root, text="Metin Giriniz:", font=("Arial", 12))
input_label.pack(pady=10)

input_entry = tk.Entry(root, font=("Arial", 14), width=30)
input_entry.pack(pady=5)

# Çeviri düğmesi
translate_button = tk.Button(root, text="Çevir", font=("Arial", 12), bg="blue", fg="white", command=translate_text)
translate_button.pack(pady=10)

# Çeviri sonucunu göstermek için etiket
output_label = tk.Label(root, text="Çeviri: ", font=("Arial", 14), fg="green")
output_label.pack(pady=20)

# Uygulamayı çalıştır
root.mainloop()