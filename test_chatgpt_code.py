import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.scrolledtext as scrolledtext


class App:
    def __init__(self, root):
        # Create a menu
        menu = tk.Menu(root)
        root.config(menu=menu)
        # Create a text widget
        self.text = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, highlightthickness=0)
        self.text.pack()
        # Create a file menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        # Create a tag for red text
        self.text.tag_configure("red", foreground="red")
        # Create a tag for indented text
        self.text.tag_configure("indent", lmargin1=20, lmargin2=20)
        # Create a button
        self.save_button = tk.Button(root, text="Save", command=self.save_file)
        self.save_button.pack()

    def new_file(self):
        print("Creating a new file...")

    def open_file(self):
        # Open a file dialog to select a file
        filepath = filedialog.askopenfilename()
        # Check if the user selected a file
        if filepath:
            # Open the file
            with open(filepath, "r") as f:
                # Read the contents of the file
                contents = f.read()
            # Clear the text widget
            self.text.delete("1.0", tk.END)
            # Insert the contents of the file into the text widget
            self.text.insert("1.0", contents)
            # Set the syntax highlighting for the file
            if filepath.endswith(".py"):
                self.text.config(highlightbackground="black", highlightcolor="white", highlightthickness=1, font=(
                    "Consolas", 12), bg="black", fg="white", insertbackground="white")
            elif filepath.endswith(".txt"):
                self.text.config(highlightbackground="black", highlightcolor="white", highlightthickness=1, font=(
                    "Consolas", 12), bg="black", fg="white", insertbackground="white")

    def save_file(self):
        # Open a save dialog to select a file
        filepath = filedialog.asksaveasfilename()
        # Check if the user selected a file
        if filepath:
            # Get the contents of the text widget
            contents = self.text.get("1.0", tk.END)
            # Write the contents to the file
            with open(filepath, "w") as f:
                f.write(contents)
        else:
            print("No file was selected.")


# Create the root window
root = tk.Tk()
# Create an instance of the App class
app = App(root)
# Run the main loop
root.mainloop()

