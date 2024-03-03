from tkinter import Tk, Label, Button, filedialog
from rembg import remove

class BackgroundRemoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Background Removing Tool")
        self.master.geometry("500x300")
        self.master.resizable(0, 0)
        self.master.configure(bg="light blue")
        self.text_font = ("Boulder", 18, 'bold')
        self.background = "light blue"
        self.foreground = "black"

        self.label_description = Label(self.master, text="Image", font=self.text_font, bg=self.background, fg=self.foreground)
        self.label_description.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.select_button = Button(self.master, text="Browse", font=self.text_font, bg="green", fg=self.foreground, command=self.select_file)
        self.select_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="W")

        self.run_button = Button(self.master, text="Run Now!", font=self.text_font, bg="light cyan", fg=self.foreground, command=self.background_remover)
        self.run_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="EW")

        self.processing_label = Label(self.master, text="Processing...", font=self.text_font, bg=self.background, fg="black", justify="center")
        self.processing_label.grid_forget()

        self.info_label = Label(self.master, text="", font=self.text_font, bg=self.background, fg=self.foreground, wraplength=400)
        self.info_label.grid(row=2, column=0, columnspan=2, pady=20)


        self.file_path = None
        self.file_path_new = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        
        
    def select_last(self):
        self.file_path_new = filedialog.asksaveasfilename(defaultextension=".png")

    def save_file(self, content):
        if self.file_path_new:
            with open(self.file_path_new, "wb") as file:
                file.write(content)
                self.info_label.config(text=f"File saved to: {self.file_path_new}")
    

    def background_remover(self):
        if self.file_path: 
            self.processing_label.grid()
            input_path = self.file_path
            if not self.file_path_new:
                self.select_last()
            output_path = self.file_path_new
            print("in:   ",self.file_path)
            print("out:    ",self.file_path_new)

            

            with open(input_path, "rb") as i:
                with open(output_path, "wb") as o:
                    input_value = i.read()
                    output_value = remove(input_value)
                    o.write(output_value)
            
 
            print("İşlem tamam.")
            try:
                self.processing_label.grid_forget()
                self.info_label.config(text="Background removed.")
            except Exception as e:
                self.info_label.config(text=f"Hata: {str(e)}")

            
            self.save_file(output_value)

if __name__ == "__main__":
    bg_remover = Tk()
    app = BackgroundRemoverApp(bg_remover)
    bg_remover.mainloop()
