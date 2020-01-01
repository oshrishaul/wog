def add_score(points):
    try:
        import WoG.Utils
        sc_r = open(WoG.Utils.SCORES_FILE_NAME, "r")
        sc_r = sc_r.read()
        if sc_r.isdecimal():
          current = int(sc_r) + int(points)
          current = str(current)
          sc_w = open(WoG.Utils.SCORES_FILE_NAME, "w+")
          sc_w.write(current)
          sc_w.seek(0)
          content = sc_w.read()
          print("Your total score is:",content)
          sc_w.close()
    except:
        sc_w = open(WoG.Utils.SCORES_FILE_NAME, "w+", encoding='utf-8')
        sc_w.write(str(points))
        sc_w.seek(0)
        content = sc_w.read()
        print("Your current score is:",content)
        sc_w.close()
