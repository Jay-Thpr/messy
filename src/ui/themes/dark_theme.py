COLORS = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "accent": "#ff00ff",
}

def style_button(btn):
    btn.config(bg=COLORS["accent"], fg=COLORS["fg"])
