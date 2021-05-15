import sys
import serial
import time
from tkinter import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

counter = 0
counter_off = 0

ser = serial.Serial('COM1', 9600)


# Reads one line of data using ser.readline() function.

def read_data():
    receive_data = ser.readline()
    receive_data = receive_data.strip()
    receive_data = receive_data.decode()
    print(receive_data)
    return receive_data


def counter_label(labelchk, labelalt, labelhov, labelgs, labeltac, labelnav, labelhdg, labelas, labelhht, labelapp):
    counter = 1

    def count():
        global counter
        counter += 1
        receive_data = read_data()
        if receive_data == "chk on":
            labelchk.config(bg="green")
        elif receive_data == "chk off":
            labelchk.config(bg="orange")
        elif receive_data == "alt on":
            labelalt.config(bg="green")
        elif receive_data == "alt off":
            labelalt.config(bg="orange")
        elif receive_data == "hov on":
            labelhov.config(bg="green")
        elif receive_data == "hov off":
            labelhov.config(bg="orange")
        elif receive_data == "g/s on":
            labelgs.config(bg="green")
        elif receive_data == "g/s off":
            labelgs.config(bg="orange")
        elif receive_data == "app on":
            labelapp.config(bg="green")
        elif receive_data == "app off":
            labelapp.config(bg="orange")
        elif receive_data == "hht on":
            labelhht.config(bg="green")
        elif receive_data == "hht off":
            labelhht.config(bg="orange")
        elif receive_data == "a/s on":
            labelas.config(bg="green")
        elif receive_data == "a/s off":
            labelas.config(bg="orange")
        elif receive_data == "alt on":
            labelalt.config(bg="green")
        elif receive_data == "alt off":
            labelalt.config(bg="orange")
        elif receive_data == "hdg on":
            labelhdg.config(bg="green")
        elif receive_data == "hdg off":
            labelhdg.config(bg="orange")
        elif receive_data == "nav on":
            labelnav.config(bg="green")
        elif receive_data == "nav off":
            labelnav.config(bg="orange")
        elif receive_data == "tac on":
            labeltac.config(bg="green")
        elif receive_data == "tac off":
            labeltac.config(bg="orange")

        labelchk.after(1000, count)

    count()


# Sends one line of data using ser.write() function.
def send_data(output_value):
    # Transmit
    send_data = output_value
    ser.write(send_data.encode())


def arinctx():
    window.title("ARINC Tx")
    label_heading1.place_forget()
    label_check = Label(window, text="CHECK", width=10, height=1)
    label_display = Label(window, text="Display", bg='red', width=12, height=1)
    label_hov = Label(window, text="HOV", width=10, height=1)
    label_g_s = Label(window, text="G/S", width=10, height=1)
    label_app = Label(window, text="APP", width=10, height=1)
    label_hht = Label(window, text="HHT", width=10, height=1)
    label_a_s = Label(window, text="A/S", width=10, height=1)
    label_alt = Label(window, text="ALT", width=10, height=1)
    label_hdg = Label(window, text="HDG", width=10, height=1)
    label_nav = Label(window, text="NAV", width=10, height=1)
    label_tac = Label(window, text="TAC", width=10, height=1)
    label_check.place(x=280, y=240)
    label_hov.place(x=280, y=170)
    label_g_s.place(x=410, y=170)
    label_app.place(x=540, y=170)
    label_hht.place(x=150, y=240)
    label_a_s.place(x=410, y=100)
    label_alt.place(x=150, y=100)
    label_hdg.place(x=280, y=100)
    label_nav.place(x=540, y=100)
    label_tac.place(x=150, y=170)

    # Send command variables

    chk_value = "CHK"
    hov_value = "HOV"
    gs_value = "G/S"
    app_value = "APP"
    hht_value = "HHT"
    as_value = "A/S"
    alt_value = "ALT"
    hdg_value = "HDG"
    nav_value = "NAV"
    tac_value = "TAC"

    def toggle1():
        if button_check.config('text')[-1] == 'OFF':
            button_check.config(text='ON', fg='orange')
            send_data(chk_value)
            print(chk_value)
        else:
            button_check.config(text='OFF', fg='orange')

    def toggle2():
        if button_hov.config('text')[-1] == 'OFF':
            button_hov.config(text='ON', fg='green')
            send_data(hov_value)
            print(hov_value)
        else:
            button_hov.config(text='OFF', fg='orange')

    def toggle3():
        if button_g_s.config('text')[-1] == 'OFF':
            button_g_s.config(text='ON', fg='green')
            send_data(gs_value)
            print(gs_value)
        else:
            button_g_s.config(text='OFF', fg='orange')

    def toggle4():
        if button_app.config('text')[-1] == 'OFF':
            button_app.config(text='ON', fg='green')
            send_data(app_value)
            print(app_value)
        else:
            button_app.config(text='OFF', fg='orange')

    def toggle5():
        if button_hht.config('text')[-1] == 'OFF':
            button_hht.config(text='ON', fg='green')
            send_data(hht_value)
            print(hht_value)
        else:
            button_hht.config(text='OFF', fg='orange')

    def toggle6():
        if button_a_s.config('text')[-1] == 'OFF':
            button_a_s.config(text='ON', fg='green')
            send_data(as_value)
            print(as_value)
        else:
            button_a_s.config(text='OFF', fg='orange')

    def toggle7():
        if button_alt.config('text')[-1] == 'OFF':
            button_alt.config(text='ON', fg='green')
            send_data(alt_value)
            print(alt_value)
        else:
            button_alt.config(text='OFF', fg='orange')

    def toggle8():
        if button_hdg.config('text')[-1] == 'OFF':
            button_hdg.config(text='ON', fg='green')
            send_data(hdg_value)
            print(hdg_value)
        else:
            button_hdg.config(text='OFF', fg='orange')

    def toggle9():
        if button_nav.config('text')[-1] == 'OFF':
            button_nav.config(text='ON', fg='green')
            send_data(nav_value)
            print(nav_value)
        else:
            button_nav.config(text='OFF', fg='orange')

    def toggle10():
        if button_tac.config('text')[-1] == 'OFF':
            button_tac.config(text='ON', fg='green')
            send_data(tac_value)
            print(tac_value)
        else:
            button_tac.config(text='OFF', fg='orange')

    def exit():
        button_check.place_forget()
        button_hov.place_forget()
        button_g_s.place_forget()
        button_app.place_forget()
        button_hht.place_forget()
        button_a_s.place_forget()
        button_alt.place_forget()
        button_hdg.place_forget()
        button_nav.place_forget()
        button_tac.place_forget()
        button_exit.place_forget()
        label_check.place_forget()
        label_display.place_forget()
        label_hov.place_forget()
        label_g_s.place_forget()
        label_app.place_forget()
        label_hht.place_forget()
        label_a_s.place_forget()
        label_alt.place_forget()
        label_hdg.place_forget()
        label_nav.place_forget()
        label_tac.place_forget()

    display_text = "Display Text"

    button_check = tk.Button(window, text="OFF", fg='orange', width=10, height=1, command=toggle1)
    button_hov = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle2)
    button_g_s = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle3)
    button_app = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle4)
    button_hht = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle5)
    button_a_s = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle6)
    button_alt = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle7)
    button_hdg = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle8)
    button_nav = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle9)
    button_tac = tk.Button(window, text="OFF", fg="orange", width=10, height=1, command=toggle10)
    button_send = tk.Button(window, text="Send display test", width=17, height=1, command=send_data(display_text))
    button_exit = tk.Button(window, text="EXIT", width=10, height=3, command=exit)
    text_box = Text(window, width=20, height=1 )
    display_text = text_box.get("1.0", "end-1c")
    print(display_text)

    text_box.place(x=200, y=380)
    text_box.pack()
    button_check.place(x=280, y=262)
    button_hov.place(x=280, y=192)
    button_g_s.place(x=410, y=192)
    button_app.place(x=540, y=192)
    button_hht.place(x=150, y=262)
    button_a_s.place(x=410, y=122)
    button_alt.place(x=150, y=122)
    button_hdg.place(x=280, y=122)
    button_nav.place(x=540, y=122)
    button_tac.place(x=150, y=192)
    button_send.place(x=380, y=380)
    button_exit.place(x=700, y=380)


def arincrx():
    window.title("ARINC Rx")
    label_heading1.place_forget()

    label_check = Label(window, text="CHECK", width=10, height=1)
    label_hov = Label(window, text="HOV", width=10, height=1)
    label_g_s = Label(window, text="G/S", width=10, height=1)
    label_app = Label(window, text="APP", width=10, height=1)
    label_hht = Label(window, text="HHT", width=10, height=1)
    label_a_s = Label(window, text="A/S", width=10, height=1)
    label_alt = Label(window, text="ALT", width=10, height=1)
    label_hdg = Label(window, text="HDG", width=10, height=1)
    label_nav = Label(window, text="NAV", width=10, height=1)
    label_tac = Label(window, text="TAC", width=10, height=1)
    label_check1 = tk.Label(window, bg="orange", width=10, height=1)
    label_hov1 = tk.Label(window, bg="orange", width=10, height=1)
    label_g_s1 = tk.Label(window, bg="orange", width=10, height=1)
    label_app1 = tk.Label(window, bg="orange", width=10, height=1)
    label_hht1 = tk.Label(window, bg="orange", width=10, height=1)
    label_a_s1 = tk.Label(window, bg="orange", width=10, height=1)
    label_alt1 = tk.Label(window, bg="orange", width=10, height=1)
    label_hdg1 = tk.Label(window, bg="orange", width=10, height=1)
    label_nav1 = tk.Label(window, bg="orange", width=10, height=1)
    label_tac1 = tk.Label(window, bg="orange", width=10, height=1)
    label_check.place(x=280, y=240)
    label_hov.place(x=280, y=170)
    label_g_s.place(x=410, y=170)
    label_app.place(x=540, y=170)
    label_hht.place(x=150, y=240)
    label_a_s.place(x=410, y=100)
    label_alt.place(x=150, y=100)
    label_hdg.place(x=280, y=100)
    label_nav.place(x=540, y=100)
    label_tac.place(x=150, y=170)

    counter_label(label_check1, label_alt1, label_hov1, label_g_s1, label_tac1, label_nav1, label_hdg1,
                  label_a_s1, label_hht1, label_app1)

    def exit():
        label_check.place_forget()
        label_hov.place_forget()
        label_g_s.place_forget()
        label_app.place_forget()
        label_hht.place_forget()
        label_a_s.place_forget()
        label_alt.place_forget()
        label_hdg.place_forget()
        label_nav.place_forget()
        label_tac.place_forget()
        button_exit.place_forget()
        label_check1.place_forget()
        label_hov1.place_forget()
        label_g_s1.place_forget()
        label_app1.place_forget()
        label_hht1.place_forget()
        label_a_s1.place_forget()
        label_alt1.place_forget()
        label_hdg1.place_forget()
        label_nav1.place_forget()
        label_tac1.place_forget()
        label_heading1.place_forget()

    button_exit = tk.Button(window, text="EXIT", width=10, height=2, command=exit)
    button_exit.place(x=700, y=380)
    label_check1.config()
    label_hov1.config()
    label_g_s1.config()
    label_app1.config()
    label_hht1.config()
    label_a_s1.config()
    label_alt1.config()
    label_hdg1.config()
    label_nav1.config()
    label_tac1.config()
    label_check1.place(x=280, y=260)
    label_hov1.place(x=280, y=190)
    label_g_s1.place(x=410, y=190)
    label_app1.place(x=540, y=190)
    label_hht1.place(x=150, y=260)
    label_a_s1.place(x=410, y=120)
    label_alt1.place(x=150, y=120)
    label_hdg1.place(x=280, y=120)
    label_nav1.place(x=540, y=120)
    label_tac1.place(x=150, y=190)


def discrete():
    window.title("Discrete")
    label_heading1.place_forget()
    label_maint = Label(window, text="MAINT", width=10, height=1)
    label_yawr = Label(window, text="YAWR", width=10, height=1)
    label_test = Label(window, text="TEST", width=10, height=1)
    label_coll = Label(window, text="COLL", width=10, height=1)
    label_valid = Label(window, text="VALIDITY", width=10, height=1)
    label_yaw = Label(window, text="YAW", width=10, height=1)
    label_stab = Label(window, text="STAB", width=10, height=1)
    label_cys = Label(window, text="CYC", width=10, height=1)
    label_yawl = Label(window, text="YAWL", width=10, height=1)
    label_stab1 = Label(window, bg='green', width=10, height=1)
    label_cys1 = tk.Label(window, bg="green", width=10, height=1)
    label_yaw1 = tk.Label(window, bg="orange", width=10, height=1)
    label_coll1 = tk.Label(window, bg="orange", width=10, height=1)
    label_valid1 = tk.Label(window, bg="orange", width=10, height=1)
    label_test1 = tk.Label(window, bg="green", width=10, height=1)
    label_maint1 = tk.Label(window, bg="green", width=10, height=1)
    label_yawr1 = tk.Label(window, bg="green", width=10, height=1)
    label_yawl1 = tk.Label(window, bg="green", width=10, height=1)
    label_yawl.place(x=150, y=220)
    label_test.place(x=280, y=150)
    label_maint.place(x=410, y=150)
    label_yawr.place(x=540, y=150)
    label_valid.place(x=150, y=150)
    label_yaw.place(x=410, y=80)
    label_stab.place(x=150, y=80)
    label_cys.place(x=280, y=80)
    label_coll.place(x=540, y=80)

    def toggle1():
        if label_stab.config('text')[-1] == 'ON':
            label_stab1.config(bg='orange')

        else:
            label_stab1.config(bg='green')

    def toggle2():
        if label_cys.config('text')[-1] == 'ON':
            label_cys1.config(bg='orange')

        else:
            label_cys1.config(bg='green')

    def toggle3():
        if label_yaw.config('text')[-1] == 'OFF':
            label_yaw1.config(bg='green')

        else:
            label_yaw1.config(bg='orange')

    def toggle4():
        if label_coll.config('text')[-1] == 'OFF':
            label_coll1.config(bg='green')

        else:
            label_coll1.config(bg='orange')

    def toggle5():
        if label_valid.config('text')[-1] == 'OFF':
            label_valid1.config(bg='green')

        else:
            label_valid1.config(bg='orange')

    def toggle6():
        if label_test.config('text')[-1] == 'ON':
            label_test1.config(bg='orange')

        else:
            label_test1.config(bg='green')

    def toggle7():
        if label_maint.config('text')[-1] == 'ON':
            label_maint1.config(bg='orange')

        else:
            label_maint1.config(bg='green')

    def toggle8():
        if label_yawr.config('text')[-1] == 'ON':
            label_yawr1.config(bg='orange')

        else:
            label_yawr1.config(bg='green')

    def toggle9():
        if label_yawl.config('text')[-1] == 'ON':
            label_yawl1.config(bg='orange')

        else:
            label_yawl1.config(bg='green')

    def toggle_1():
        if button_stab.config('text')[-1] == 'ON':
            button_stab.config(text='OFF', fg='orange')

        else:
            button_stab.config(text='ON', fg='green')

    def toggle_2():
        if button_cys.config('text')[-1] == 'ON':
            button_cys.config(text='OFF', fg='orange')

        else:
            button_cys.config(text='ON', fg='green')

    def toggle_3():
        if button_yaw.config('text')[-1] == 'OFF':
            button_yaw.config(text='ON', fg='green')

        else:
            button_yaw.config(text='OFF', fg='orange')

    def toggle_4():
        if button_coll.config('text')[-1] == 'OFF':
            button_coll.config(text='ON', fg='green')

        else:
            button_coll.config(text='OFF', fg='orange')

    def toggle_5():
        if button_maint.config('text')[-1] == 'OFF':
            button_maint.config(text='ON', fg='green')

        else:
            button_maint.config(text='OFF', fg='orange')

    def toggle_6():
        if button_test.config('text')[-1] == 'ON':
            button_test.config(text='OFF', fg='orange')
        else:
            button_test.config(text='ON', fg='green')

    def exit():
        label_stab.place_forget()
        label_stab1.place_forget()
        label_cys.place_forget()
        label_cys1.place_forget()
        label_yaw.place_forget()
        label_yaw1.place_forget()
        label_coll.place_forget()
        label_coll1.place_forget()
        label_valid.place_forget()
        label_valid1.place_forget()
        button_exit.place_forget()
        label_test.place_forget()
        label_test1.place_forget()
        label_maint.place_forget()
        label_maint1.place_forget()
        label_yawr.place_forget()
        label_yawr1.place_forget()
        label_yawl.place_forget()
        label_yawl1.place_forget()
        label_stab2.place_forget()
        label_cys2.place_forget()
        label_yaw2.place_forget()
        label_coll2.place_forget()
        label_maint2.place_forget()
        label_test2.place_forget()
        button_stab.place_forget()
        button_cys.place_forget()
        button_yaw.place_forget()
        button_coll.place_forget()
        button_maint.place_forget()
        button_test.place_forget()
        label_heading1.place_forget()

    label_stab1.config(command=toggle1())
    label_cys1.config(command=toggle2())
    label_yaw1.config(command=toggle3())
    label_coll1.config(command=toggle4())
    label_valid1.config(command=toggle5())
    label_test1.config(command=toggle6())
    label_maint1.config(command=toggle7())
    label_yawr1.config(command=toggle8())
    label_yawl1.config(command=toggle9())
    label_stab2 = Label(window, text="STAB", width=10, height=1)
    label_cys2 = Label(window, text="CYS", width=10, height=1)
    label_yaw2 = Label(window, text="YAW", width=10, height=1)
    label_coll2 = Label(window, text="COLL", width=10, height=1)
    label_maint2 = Label(window, text="MAINT", width=10, height=1)
    label_test2 = Label(window, text="TEST", width=10, height=1)
    button_exit = tk.Button(window, text="EXIT", width=10, height=3, command=exit)
    button_stab = tk.Button(window, text="ON", fg="green", width=10, height=1, command=toggle_1)
    button_cys = tk.Button(window, text="ON", fg="green", width=10, height=1, command=toggle_2)
    button_yaw = tk.Button(window, text="ON", fg="green", width=10, height=1, command=toggle_3)
    button_coll = tk.Button(window, text="ON", fg="green", width=10, height=1, command=toggle_4)
    button_maint = tk.Button(window, text="ON", fg="green", width=10, height=1, command=toggle_5)
    button_test = tk.Button(window, text="ON", fg="green", width=10, height=1, command=toggle_6)
    label_yawl1.place(x=150, y=240)
    label_test1.place(x=280, y=170)
    label_maint1.place(x=410, y=170)
    label_yawr1.place(x=540, y=170)
    label_valid1.place(x=150, y=170)
    label_yaw1.place(x=410, y=100)
    label_stab1.place(x=150, y=100)
    label_cys1.place(x=280, y=100)
    label_coll1.place(x=540, y=100)
    label_stab2.place(x=150, y=300)
    label_cys2.place(x=300, y=300)
    label_yaw2.place(x=450, y=300)
    label_coll2.place(x=150, y=380)
    label_maint2.place(x=300, y=380)
    label_test2.place(x=450, y=380)
    button_exit.place(x=700, y=380)
    button_stab.place(x=150, y=322)
    button_cys.place(x=300, y=322)
    button_yaw.place(x=450, y=322)
    button_coll.place(x=150, y=402)
    button_maint.place(x=300, y=402)
    button_test.place(x=450, y=402)

window = tk.Tk()
menu = Menu(window)
window.title("AFCP-Testjig")
window.configure(background='#49A')
label_heading1 = tk.Label(window, text="AFCP TestJig Test Suit", bg="orange", width=40, height=10)
label_heading1.place(x=300, y=175)
window.config(menu=menu)
window.geometry("900x550")
submenu = Menu(menu)
menu.add_cascade(label="Select Feature to Test", menu=submenu)
submenu.add_command(label="ARINC Tx", command=arinctx)
submenu.add_separator()
submenu.add_command(label="ARINC Rx", command=arincrx)
submenu.add_separator()
submenu.add_command(label="DISCRETE I/O", command=discrete)
submenu.add_separator()

window.mainloop()

