import tkinter as tk
from tkinter import messagebox
import webbrowser  # <== kliklənən link üçün

# === GUI Window ===
root = tk.Tk()
root.title("🛒 Cyber Courses - Shopping Cart")
root.geometry("1200x580")
root.configure(bg="#2b2d3a")

# === Color Palette ===
bg_dark = "#2b2d3a"
bg_component = "#2a2a40"
text_main = "#f1f1f1"
text_muted = "#aaaaaa"
button_main = "#ff4c4c"
accent_blue = "#66bfff"
highlight_yellow = "#ffcc66"
border_color = "#3d3d5c"

# === Burger Menu ===
menu_visible = False
menu_frame = tk.Frame(root, bg=bg_component, width=200, height=580)

def open_help_window():
    help_win = tk.Toplevel(root)
    help_win.title("Help")
    help_win.geometry("400x200")
    help_win.configure(bg=bg_component)

    tk.Label(help_win, text="Need support or have a question?",
             font=("Arial", 11, "bold"), fg=accent_blue, bg=bg_component).pack(pady=10)

    tk.Label(help_win, text="📩 Email: emilmirzayev007@gmail.com",
             font=("Arial", 10), fg=text_main, bg=bg_component).pack(pady=5)

    insta_label = tk.Label(help_win, text="📸 Instagram: @mirzayev_emil",
                           font=("Arial", 10, "underline"), fg="#66bfff",
                           bg=bg_component, cursor="hand2")
    insta_label.pack(pady=5)

    insta_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.instagram.com/mirzayev_emil/"))

def toggle_menu():
    global menu_visible
    if not menu_visible:
        menu_frame.place(x=0, y=0)

        tk.Label(menu_frame, text="🔹 Menu", font=("Arial", 12, "bold"),
                 fg=accent_blue, bg=bg_component).place(x=10, y=10)

        tk.Button(menu_frame, text="ℹ️ About Us", font=("Arial", 10),
                  bg=bg_component, fg=text_main, bd=0,
                  command=lambda: messagebox.showinfo("About Us",
"""This platform offers hands-on training in cybersecurity and Python development.
We aim to provide affordable and accessible learning opportunities for all.

✅ Flexible learning
✅ Practical skills
✅ Self-paced & weekly courses

📣 Thank you for choosing us!
📞 Feel free to contact us after course completion for guidance or career support."""))\
            .place(x=10, y=50)

        tk.Button(menu_frame, text="📦 My Orders", font=("Arial", 10),
                  bg=bg_component, fg=text_main, bd=0,
                  command=lambda: messagebox.showinfo("My Orders",
"""To start your learning journey with us,
we highly recommend gaining IT Essentials knowledge first.

🎓 Once ready, explore our premium packages.
🎁 Need help? We can offer a FREE IT Starter Pack for beginners!

🖱️ Contact us to get started!"""))\
            .place(x=10, y=90)

        tk.Button(menu_frame, text="❓ Help", font=("Arial", 10),
                  bg=bg_component, fg=text_main, bd=0,
                  command=open_help_window)\
            .place(x=10, y=130)

        menu_visible = True
    else:
        menu_frame.place_forget()
        menu_visible = False

# === Burger Button ===
tk.Button(root, text="☰", font=("Arial", 14, "bold"),
          bg=bg_dark, fg=accent_blue, bd=0,
          command=toggle_menu).place(x=10, y=10)

# === Products ===
products = {
    "🛡️ Cybersecurity - Weekly": 90,
    "🔐 Cybersecurity - Self-study": 80,
    "🐍 Python from Scratch (30% OFF)": 70,
    "🤖 Build a Bot with Python": 95,
    "📊 Data Analysis with Python": 90,
    "🧠 Intro to Machine Learning": 110,
    "🌐 Web Security Basics": 85,
    "🧱 Firewall & Network Security": 100,
    "🔍 Pentesting Mini-Course (30% OFF)": 66.5,
    "📚 All-in-One Access (Monthly)": 150
}

selected = {}
quantities = {}

# === Title ===
tk.Label(root, text="📘 Course List", font=("Arial", 16, "bold"),
         fg=accent_blue, bg=bg_dark).place(x=300, y=20)

# === Course List ===
y_offset = 70
for name, price in products.items():
    var = tk.IntVar()
    qty = tk.IntVar(value=1)

    cb = tk.Checkbutton(root, text=f"{name} - ${price:.2f}", variable=var,
                        command=lambda: update_cart(),
                        bg=bg_dark, fg=text_main,
                        activebackground=bg_dark, selectcolor=bg_dark,
                        font=("Arial", 11))
    cb.place(x=300, y=y_offset)

    def decrease(q=qty): q.set(max(1, q.get() - 1)); update_cart()
    def increase(q=qty): q.set(q.get() + 1); update_cart()

    tk.Button(root, text="-", width=3, height=1, font=("Arial", 10),
              bg=button_main, fg="white", command=decrease).place(x=670, y=y_offset)

    tk.Label(root, textvariable=qty, width=3, font=("Arial", 11),
             bg=bg_dark, fg=text_muted).place(x=710, y=y_offset)

    tk.Button(root, text="+", width=3, height=1, font=("Arial", 10),
              bg=button_main, fg="white", command=increase).place(x=750, y=y_offset)

    selected[name] = var
    quantities[name] = qty
    y_offset += 35

# === Cart Title ===
tk.Label(root, text="🧺 Cart", font=("Arial", 14, "bold"),
         bg=bg_component, fg=accent_blue).place(x=920, y=30)

# === Cart Box ===
cart_box = tk.Text(root, width=30, height=20, state="disabled",
                   bg=bg_component, fg=text_main, font=("Arial", 10),
                   highlightbackground=border_color, highlightthickness=1)
cart_box.place(x=880, y=60)

# === Update Cart ===
def update_cart():
    cart_box.config(state="normal")
    cart_box.delete(1.0, tk.END)
    total = 0

    for name in selected:
        if selected[name].get() == 1:
            qty = quantities[name].get()
            price = products[name]
            line_total = qty * price
            total += line_total
            cart_box.insert(tk.END, f"{name}\n  x{qty} = ${line_total:.2f}\n\n")

    cart_box.insert(tk.END, f"🔢 Total: ${total:.2f}")
    cart_box.config(state="disabled")

# === Show Total ===
def show_total():
    total = 0
    for name in selected:
        if selected[name].get() == 1:
            qty = quantities[name].get()
            total += products[name] * qty
    messagebox.showinfo("Total Price", f"Total amount: ${total:.2f}\n\nThanks for shopping with us! 🛒\nSee you soon 👋")

# === Enter Button ===
tk.Button(root, text="💰 Enter", font=("Arial", 12, "bold"),
          bg=button_main, fg="white", width=15, height=2,
          command=show_total).place(x=950, y=470)

# === Motivation Quotes ===
tk.Label(root, text="🚀 Build skills. Build your future.",
         font=("Arial", 10, "italic"),
         fg=highlight_yellow, bg=bg_dark).place(x=930, y=520)

tk.Label(root, text="📘 Keep learning. Keep growing.",
         font=("Arial", 10, "italic"),
         fg=highlight_yellow, bg=bg_dark).place(x=930, y=540)

# === Start GUI ===
root.mainloop()
