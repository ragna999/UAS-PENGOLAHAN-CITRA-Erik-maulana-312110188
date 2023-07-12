import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import math


def calculate_mse(original, processed):
    mse = np.mean((original - processed) ** 2)
    return mse


def calculate_psnr(mse, max_pixel=255.0):
    if mse == 0:
        return float('inf')
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr


def median_filter(image_array, filter_size):
    filtered_image = np.zeros_like(image_array)
    padding = filter_size // 2
    padded_image = np.pad(image_array, ((padding, padding), (padding, padding)), mode='edge')

    for i in range(padding, image_array.shape[0] + padding):
        for j in range(padding, image_array.shape[1] + padding):
            neighborhood = padded_image[i - padding:i + padding + 1, j - padding:j + padding + 1]
            median_value = np.median(neighborhood)
            filtered_image[i - padding, j - padding] = median_value

    return filtered_image


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Raihan Tantowi - 312110229 - UAS Pengolahan Citra")
        self.geometry("600x350")
        self.configure(bg="#708090")  # Warna latar belakang
        self.original_image = None
        self.processed_image = None

        self.label_title = tk.Label(self, text="Program perbaikan citra dengan menggunakan metode median filter",
                                    font=("Arial", 14), bg="#708090", fg="white")
        self.label_title.pack(pady=10)

        self.frame_images = tk.Frame(self, bg="#708090")
        self.frame_images.pack()

        self.frame_left = tk.Frame(self.frame_images, bg="#708090")
        self.frame_left.pack(side=tk.LEFT, padx=10)

        self.label_original = tk.Label(self.frame_left, text="Original Image", bg="#708090", fg="white")
        self.label_original.pack()

        self.canvas_original = tk.Canvas(self.frame_left, width=250, height=250)
        self.canvas_original.pack()

        self.frame_right = tk.Frame(self.frame_images, bg="#708090")
        self.frame_right.pack(side=tk.LEFT, padx=10)

        self.label_processed = tk.Label(self.frame_right, text="Processed Image", bg="#708090", fg="white")
        self.label_processed.pack()

        self.canvas_processed = tk.Canvas(self.frame_right, width=250, height=250)
        self.canvas_processed.pack()

        self.frame_buttons = tk.Frame(self, bg="#708090")
        self.frame_buttons.pack(side=tk.TOP, pady=10)

        self.button_upload = tk.Button(self.frame_buttons, text="Upload Image", command=self.upload_image)
        self.button_upload.pack(side=tk.LEFT, padx=5)

        self.button_process = tk.Button(self.frame_buttons, text="Process Image", command=self.process_image)
        self.button_process.pack(side=tk.LEFT, padx=5)

        self.label_mse = tk.Label(self, text="MSE: ", bg="#708090", fg="white")
        self.label_mse.pack()

        self.label_psnr = tk.Label(self, text="PSNR: ", bg="#708090", fg="white")
        self.label_psnr.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.canvas_original, self.original_image)

    def process_image(self):
        if self.original_image:
            image_array = np.array(self.original_image)
            filtered_image = median_filter(image_array, 3)  # Adjust the filter size if needed
            self.processed_image = Image.fromarray(filtered_image.astype(np.uint8))
            self.display_image(self.canvas_processed, self.processed_image)

            mse = calculate_mse(image_array, filtered_image)
            psnr = calculate_psnr(mse)
            self.label_mse.config(text="MSE: {:.2f}".format(mse))
            self.label_psnr.config(text="PSNR: {:.2f}".format(psnr))

    def display_image(self, canvas, image):
        image = image.resize((250, 250))
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)


if __name__ == "__main__":
    app = Application()
    app.mainloop()