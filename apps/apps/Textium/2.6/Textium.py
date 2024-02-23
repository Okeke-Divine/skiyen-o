import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Menubar:

	def __init__(self, parent):

		menubar = tk.Menu(parent.master)
		parent.master.config(menu=menubar)

		file_dropdown = tk.Menu(menubar, tearoff=0)
		file_dropdown.add_command(label="New File",
								accelerator="Ctrl+N",
								command=parent.new_file)
		file_dropdown.add_command(label="Open File",
								accelerator="Ctrl+O",
								command=parent.open_file)
		file_dropdown.add_command(label="Save",
								accelerator="Ctrl+S",
								command=parent.save)
		file_dropdown.add_command(label="Save As",
								accelerator="Ctrl+Shift+S",
								command=parent.save_as)
		file_dropdown.add_separator()
		file_dropdown.add_command(label="Exit",
								command=parent.master.destroy)

		about_dropdown = tk.Menu(menubar, tearoff=0)
		about_dropdown.add_command(label="Release Notes",
									 command=parent.release)
		about_dropdown.add_separator()
		about_dropdown.add_command(label="About",
									 command=parent.about)


		menubar.add_cascade(label="File",menu=file_dropdown)
		menubar.add_cascade(label="About",menu=about_dropdown)


class Statusbar:

	def __init__(self, parent):

		self.status = tk.StringVar()
		self.status.set("Textium - V2.6")

		label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
						bg="lightgrey", anchor='sw')
		label.pack(side=tk.BOTTOM, fill=tk.BOTH)


	def update_status(self, *args):
		if isinstance(args[0], bool):
			self.status.set("Your File Has Been Saved!")
		else:
			self.status.set("Textium - V2.6")

 
class PyText:

	def __init__(self, master):
		master.title("Untitled - Textium")
		master.geometry("900x400")

		self.master = master
		self.filename = None

		self.textarea = tk.Text(master, bg="white", fg="black",font=("conoslola",15))
		self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
		self.textarea.configure(yscrollcommand=self.scroll.set)
		self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.menubar = 	Menubar(self)
		self.statusbar = Statusbar(self)

		self.bind_shortcuts()

	def set_window_title(self, name=None):
		if name:
			self.master.title(name + " - Textium")
		else:
			self.master.title("Untitled - Textium")		

	def new_file(self, *args):
			self.textarea.delete(1.0, tk.END)
			self.filename = None
			self.set_window_title()

	def open_file(self, *args):
		self.filename = filedialog.askopenfilename(
				defaultextension=".*",
				filetypes=[("All Files", "*.*"),
							("Txt Files", "*.txt"),
							("Python", "*.py"),
							("Javascript", "*.js"),
							("Ruby", "*.ruby"),
							("HTML Documents", "*.html"),
							("HTML Documents", "*.htm"),
							("CSS Files", "*.css"),
							("PHP Files", "*.php"),
							("XML Files", "*.xml"),
							("C++", "*.cpp"),
							("Markdown Documents", "*.md")])
		if self.filename:
			self.textarea.delete(1.0, tk.END)
			with open(self.filename, "r") as f:
				self.textarea.insert(1.0, f.read())
		self.set_window_title(self.filename)

	def save(self, *args):
		if self.filename:
			try:
				textarea_content = self.textarea.get(1.0, tk.END)
				with open(self.filename, "w") as f:
					f.write(textarea_content)
				self.statusbar.update_status(True)
			except Exception as e:
				print(e)
		else:
			self.save_as()

	def save_as(self, *args):
		try:
			new_file = filedialog.asksaveasfilename(
				initialfile="Untitled.txt",
				defaultextension=".*",
				filetypes=[("All Files", "*.*"),
							("Txt Files", "*.txt"),
							("Python", "*.py"),
							("Javascript", "*.js"),
							("Ruby", "*.ruby"),
							("HTML Documents", "*.html"),
							("HTML Documents", "*.htm"),
							("CSS Files", "*.css"),
							("PHP Files", "*.php"),
							("XML Files", "*.xml"),
							("C++", "*.cpp"),
							("Markdown Documents", "*.md")])
			textarea_content = self.textarea.get(1.0, tk.END)
			with open(new_file, "w") as f:
				f.write(textarea_content)
			self.filename = new_file
			self.set_window_title(self.filename)
			self.statusbar.update_status(True)
		except Exception as e:
			print(e)


	def about(self):
		box_title = "About Textium"
		box_message = "Textium is a  very powerful text editor"
		messagebox.showinfo(box_title, box_message)

	def release(self):
		box_title = "Release Notes"
		box_message = "Version 2.6 - Skiyen"
		messagebox.showinfo(box_title, box_message)



	def bind_shortcuts(self):
		self.textarea.bind('<Control-s>', self.save)
		self.textarea.bind('<Control-S>', self.save_as)
		self.textarea.bind('<Control-n>', self.new_file)
		self.textarea.bind('<Control-o>', self.open_file)

if __name__ == "__main__":
	master = tk.Tk()
	pt = PyText(master)
	master.mainloop()