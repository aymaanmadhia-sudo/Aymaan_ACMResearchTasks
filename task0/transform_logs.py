def add_suffix(day):
    if 11 <= day % 100 <= 13:
        return str(day) + "th"
    last = day % 10
    if last == 1:
        return str(day) + "st"
    elif last == 2:
        return str(day) + "nd"
    elif last == 3:
        return str(day) + "rd"
    else:
        return str(day) + "th"

def transform_logs(text):
    words = text.split()
    result = []

    for w in words:
        if "@" in w and "." in w:
            result.append("[HIDDEN]")
        elif w.count(".") == 3:
            parts = w.split(".")
            if all(p.isdigit() for p in parts):
                result.append("[IP-HIDDEN]")
            else:
                result.append(w)
        else:
            result.append(w)

    text = " ".join(result)

    months = ["","January","February","March","April","May","June",
              "July","August","September","October","November","December"]
    pieces = text.split()
    for i in range(len(pieces)-1):
        if "/" in pieces[i] and ":" in pieces[i+1]:
            try:
                d,m,y = pieces[i].split("/")
                h,mn = pieces[i+1].split(":")
                d,m,y,h,mn = int(d),int(m),int(y),int(h),int(mn)
                period = "AM" if h < 12 else "PM"
                h = h % 12 or 12
                nice = f"{add_suffix(d)} {months[m]} {y}, {h}:{mn:02d} {period}"
                pieces[i] = nice
                pieces[i+1] = ""
            except:
                pass
    text = " ".join([p for p in pieces if p])

    text = text.replace("ERROR", "[WARNING] ERROR")

    return text

if __name__ == "__main__":
    sample1 = "User xxxx@mail.com logged in at 23/08/2025 14:05. ERROR: session timeout."
    print("Input: ", sample1)
    print("Output:", transform_logs(sample1))

    sample2 = "Connection from 192.168.1.10 by aymaan@djsce.educ at 05/08/2026 09:30. ERROR: connection refused."
    print("\nInput: ", sample2)
    print("Output:", transform_logs(sample2))

    print("\nyou want to try")
    user_log=input()
    print("Output:", transform_logs(user_log))


