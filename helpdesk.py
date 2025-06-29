import tkinter as tk

def save_ticket():
    user = entry_user.get()
    issue = entry_issue.get()
    with open("tickets.txt", "+a") as f:
        f.write("User: {user}  | Issue: {issue} \n")

app = tk.Tk()
app.title("Help Desk")

tk.Label(app, text="User Name").pack()
entry_user =tk.Entry(app)
entry_user.pack()

tk.Label(app, text="İssue").pack()
entry_issue =tk.Entry(app)
entry_issue.pack()

tk.Button(app, text="Submit", command=save_ticket).pack()

app.mainloop()